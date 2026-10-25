# 🩺 **Medivya - AI Medical Chatbot**

<p align="center">
<strong>An AI-powered chatbot for medical information and healthcare-related questions.</strong>
<br />
Built with Python, Flask, LangChain, Gemini, and Pinecone.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10" />
<img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/LangChain-LLM%20Framework-1C3C3C?style=for-the-badge" alt="LangChain" />
<img src="https://img.shields.io/badge/Gemini-Google%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini" />
<img src="https://img.shields.io/badge/Pinecone-Vector%20Database-00A98F?style=for-the-badge" alt="Pinecone" />
</p>

<p align="center">
<a href="https://github.com/SakshamRaj1/Medivya-Medical-Chatbot">📂 Repository</a> ·
<a href="#-getting-started">🚀 Getting Started</a> ·
<a href="#-how-it-works">⚙️ How It Works</a> ·
<a href="#-disclaimer">⚠️ Disclaimer</a>
</p>

## 📖 About the Project

Medivya is an AI-powered medical chatbot designed to help users explore medical and healthcare-related questions through a conversational web interface.

Built using Flask, LangChain, Google's Gemini API, and Pinecone, the project combines language-model capabilities with vector-based information retrieval to support context-aware responses.

The application includes a document-indexing workflow that stores embeddings in Pinecone, enabling the chatbot to retrieve relevant information from its configured knowledge base.

## ✨ Features

💬 Interactive chat interface — Ask medical questions in natural language.

🤖 AI-generated responses — Generate answers using Google's Gemini language model.

🔎 Semantic search — Retrieve relevant information using Pinecone vector search.

🧠 LLM orchestration — Integrate retrieval and language-model workflows through LangChain.

🌐 Web-based application — Access the chatbot through a Flask-powered interface.

📚 Document indexing — Generate and store embeddings using store_index.py.

🐍 Python-based development — Maintain and extend the application using a familiar Python stack.

## 🖥️ Application Preview
## Home Page

<p align="center">
<img src="https://github.com/user-attachments/assets/eb4404a0-af52-436a-9dcc-0c29d7ca2f5c" alt="Medivya medical chatbot home page" width="100%" />
</p>

## Medivya Responding to Medical Queries

<p align="center">
<img src="https://github.com/user-attachments/assets/51539686-e2fe-49be-a8df-2352a4c3b58d" alt="Medivya responding to a user's medical query" width="100%" />
</p>

## 🛠️ Tech Stack
Technology	Purpose
```
Python 3.10	Core programming language
Flask	Web application framework
LangChain	Language-model integration and retrieval orchestration
Google Gemini API	AI-generated responses
Pinecone	Vector database for semantic retrieval
Conda	Python environment management
HTML, CSS, JavaScript	Web interface technologies, where applicable
```

## ⚙️ How It Works

Medivya uses a document-indexing and question-answering workflow.

mermaid
flowchart TD
    A[Medical Documents] --> B[Document Processing]
    B --> C[Embedding Generation]
    C --> D[Pinecone Vector Database]
    E[User Question] --> F[Flask Web Application]
    F --> G[LangChain Retrieval Pipeline]
    D --> G
    G --> H[Google Gemini API]
    H --> I[Response to User]

Workflow
Document processing: Prepare the medical documents used by the application.
Embedding generation: Convert the documents into vector representations.
Vector storage: Store the embeddings in Pinecone for semantic retrieval.
User interaction: Accept a medical question through the web interface.
Context retrieval: Retrieve relevant information from the configured vector index.
Response generation: Use Gemini to generate a response based on the available context and configured prompt.

The exact retrieval and generation behavior depends on the application's implementation and configuration.

## 🚀 Getting Started

Follow these instructions to run Medivya locally.

Prerequisites

Install or configure the following:
```
Git
Anaconda or Miniconda
Python 3.10
A Google Gemini API key
A Pinecone account and API key
Step 1: Clone the Repository
```
Open your terminal and execute:
```
bash
git clone https://github.com/SakshamRaj1/Medivya-Medical-Chatbot.git
cd Medivya-Medical-Chatbot
```
Step 2: Create a Conda Environment

Create a dedicated environment using Python 3.10:
```
bash
conda create -n medivya python=3.10 -y
```

Activate the environment:
```
bash
conda activate medivya
```

If Conda is not recognized in Git Bash, open Anaconda Prompt and run:
```
bash
conda init bash
```

Restart Git Bash and activate the environment again:
```
bash
conda activate medivya
```
Step 3: Install Dependencies

Install the packages listed in requirements.txt:
```
bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you also want to use the environment as a Jupyter kernel, install ipykernel:
```
bash
conda install -n medivya ipykernel -y
```

This additional package is optional for running the Flask application unless your development workflow requires it.

Step 4: Configure Environment Variables
```
Create a .env file in the root directory of the repository.

Add your API credentials:

ini
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholders with your actual credentials.

Important security practices:

Never upload your .env file or API keys to GitHub.
Add .env to your .gitignore file.
Ensure the application loads these variables correctly.
Configure the required Pinecone index and embedding settings to match the source code.
```
Your .gitignore should include at least:

gitignore
.env
__pycache__/
*.py[cod]
.venv/
```

Keep any existing project-specific ignore rules intact.

Step 5: Build the Pinecone Index

Run the indexing script:
```
bash
python store_index.py
```

This script is intended to process the configured documents and store their embeddings in Pinecone.

Before running it, ensure that:

Your Pinecone API key is valid.
The required source documents are available.
The Pinecone index exists or can be created by the script.
The configured embedding model and index dimensions are compatible.

You generally need to run the indexing process during initial setup and again when the indexed knowledge base needs to be updated.

Step 6: Start the Flask Application

Run:
```
bash
python app.py
```

Once the Flask server starts, open the local URL shown in your terminal.

The default Flask development address is commonly:
```
http://127.0.0.1:5000/
```
If your application uses a different port, follow the URL printed in the terminal or the configuration in app.py.

## 🎉 Medivya is now running locally!

** 🔑 Environment Variables**
```
Variable	Description
PINECONE_API_KEY	API key for accessing Pinecone
GEMINI_API_KEY	API key for accessing Google Gemini
```
Additional variables may be necessary depending on the model, embedding provider, or Pinecone index configuration in the source code.

## 🧰 Troubleshooting
```
conda: command not found
```
Open Anaconda Prompt and run:
```
bash
conda init bash
```

Restart Git Bash, then activate the environment:
```
bash
conda activate medivya
```
Missing API key errors
Verify that .env is located in the expected directory.
Check that the variable names match those used by the application.
Confirm that the application loads the environment variables.
Ensure that the API credentials are valid.
Pinecone indexing errors
Verify your Pinecone API key.
Confirm that the correct index is configured.
Check the embedding model and vector dimensions.
Ensure the source documents required by the indexing script exist.
Flask application does not open
Check the terminal for Python errors.
Verify that the Flask application starts successfully.
Open the exact URL and port printed in the terminal.
Check whether another process is already using the configured port.

## 🔒 Security and Privacy

Because Medivya processes healthcare-related questions and uses external AI services, security and privacy should be considered carefully.

Keep all API keys out of source control.
Avoid logging secrets or sensitive user inputs.
Review how prompts and retrieved documents are sent to external services.
Do not submit identifiable patient information unless the system has been appropriately assessed and secured for that purpose.
Use appropriate authentication, access controls, and HTTPS before exposing the application publicly.


## 🔮 Future Improvements

Potential enhancements for the project include:

Displaying references or sources for retrieved medical information.
Improving error handling and input validation.
Adding automated tests for the retrieval pipeline and Flask routes.
Evaluating response accuracy against a curated medical question dataset.
Adding request logging and monitoring without collecting unnecessary sensitive information.
Implementing rate limiting and authentication for public deployments.

These are suggested future enhancements, not claims about existing functionality.

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

Fork the repository.
```
Create a new branch:
bash
git checkout -b feature/your-feature
```
Implement and test your changes.
Commit your work:
```
bash
git add .
git commit -m "Add: describe your changes"
```
```
Push your branch:
bash
git push origin feature/your-feature
```
Open a pull request describing the changes.

Please do not include API keys, private credentials, or real patient data in commits, issues, or screenshots.

## **⚠️ Disclaimer**

Medivya is an educational AI project and is not a substitute for professional medical advice, diagnosis, or treatment.

AI-generated medical information may be incomplete, inaccurate, outdated, or inappropriate for an individual's circumstances.

Consult a qualified healthcare professional for personal medical concerns.
Do not use chatbot responses as the sole basis for medical decisions.
In an emergency, contact local emergency services or seek immediate medical attention.
Do not delay professional evaluation or treatment based on a chatbot response.

The application does not guarantee clinical accuracy and should not be considered a clinically validated medical device.

## 👨‍💻 Author

Saksham Raj

GitHub: @SakshamRaj1

Repository: Medivya — Medical Chatbot

📄 License

Check the repository for a LICENSE file to determine the applicable terms for using, modifying, or distributing this project.

If no license is present, consider adding one before inviting others to reuse or redistribute the code.

<p align="center">
<strong>Medivya — Exploring AI-powered medical information.</strong>
<br />
<sub>Built with Python, LangChain, Gemini, Pinecone, and Flask.</sub>
</p>
