import os
import re
import uuid
import psutil
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, session, url_for
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from markupsafe import Markup, escape

from src.helper import download_hugging_face_embeddings
from src.prompt import *  # provides system_prompt

load_dotenv()

app = Flask(__name__)
# Signs the session cookie. Set SECRET_KEY in your .env file.
app.secret_key = os.environ.get("SECRET_KEY", "tobtach-lacidem")

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

# RAG chain (unchanged)

embeddings = download_hugging_face_embeddings()

index_name = "medivya-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Update this line in app.py
chatModel = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite", 
    google_api_key=GEMINI_API_KEY
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Conversation storage

CHATS = {}
MAX_MESSAGES = 40
MAX_LENGTH = 1000

SUGGESTIONS = [
    ("Symptoms of type 2 diabetes", "Early signs and when to get tested",
     "What are the common symptoms of type 2 diabetes?"),
    ("Treating high blood pressure", "Lifestyle changes and medication",
     "How is high blood pressure treated?"),
    ("Causes of Angioplasty", "atherosclerosis, heart disease, and other conditions",
     "What causes one to go through Angioplasty?"),
    ("What is Addison’s disease", "Common and serious effects",
     "What is Addison’s disease and how it is caused by histoplasmosis,?"),
]

def get_history():
    chat_id = session.get("chat_id")
    if chat_id not in CHATS:
        chat_id = session["chat_id"] = uuid.uuid4().hex
        CHATS[chat_id] = []
    return CHATS[chat_id]

def now():
    return datetime.now().strftime("%H:%M")

# Template filter: safe, light formatting of the model's answer

BULLET = re.compile(r"^\s*[*-]\s+")

def _inline(text):
    """Escape HTML, then turn **bold** into <strong>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", str(escape(text)))

@app.template_filter("answer")
def format_answer(text):
    out, para, items = [], [], []

    def flush():
        if para:
            out.append("<p>" + "<br>".join(para) + "</p>")
            para.clear()
        if items:
            out.append("<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>")
            items.clear()

    for line in str(text).strip().splitlines():
        match = BULLET.match(line)
        if not line.strip():
            flush()
        elif match:
            if para:
                flush()
            items.append(_inline(line[match.end():]))
        else:
            if items:
                flush()
            para.append(_inline(line))
    flush()
    return Markup("".join(out))

# Routes

@app.route("/")
def index():
    return render_template("chat.html", messages=get_history(), suggestions=SUGGESTIONS)

@app.post("/ask")
def ask():
    msg = request.form.get("msg", "").strip()[:MAX_LENGTH]
    if msg:
        history = get_history()
        history.append({"role": "user", "text": msg, "time": now()})
        try:
            response = rag_chain.invoke({"input": msg})
            history.append({"role": "bot", "text": str(response["answer"]), "time": now()})
        except Exception:
            app.logger.exception("RAG chain failed")
            history.append({
                "role": "bot",
                "text": "Could not get an answer. Please try again in a moment.",
                "time": now(),
                "error": True,
            })
        del history[:-MAX_MESSAGES]
    # Redirect so refreshing the page doesn't resubmit the question.
    return redirect(url_for("index"))

@app.post("/new")
def new_chat():
    CHATS.pop(session.pop("chat_id", None), None)
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

@app.route('/ram-usage')
def ram_usage():
    process = psutil.Process(os.getpid())
    memory = process.memory_info()

    return {
        'rss_mb': round(memory.rss / (1024 ** 2), 2),
        'vms_mb': round(memory.vms / (1024 ** 2), 2)
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

