# 🩺 **Medivya — Medical Chatbot**

<p align="center">
<strong>An AI-powered medical chatbot for conversational healthcare information.</strong>
<br />
Built with Python, Flask, LangChain, OpenAI, and Pinecone.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10" />
<img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/LangChain-LLM%20Framework-1C3C3C?style=for-the-badge" alt="LangChain" />
<img src="https://img.shields.io/badge/Pinecone-Vector%20Database-00A98F?style=for-the-badge" alt="Pinecone" />
<img src="https://img.shields.io/badge/AWS-Cloud%20Deployment-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS" />
</p>

<p align="center">
<a href="https://github.com/SakshamRaj1/Medivya-Medical-Chatbot">Repository</a> ·
<a href="#-getting-started">Getting Started</a> ·
<a href="#-deployment-on-aws">AWS Deployment</a> ·
<a href="#-disclaimer">Disclaimer</a>
</p>

📌 Overview

Medivya is an AI-powered medical chatbot designed to answer users' medical and healthcare-related questions through a conversational web interface.

The project combines a Flask web application with LangChain, a large language model, and Pinecone vector storage to support retrieval-based question answering. Its indexing workflow prepares medical knowledge for retrieval, helping the application generate responses informed by the configured knowledge base.

The project also includes an AWS deployment workflow using Docker, Amazon Elastic Container Registry (ECR), Amazon EC2, and GitHub Actions for automating application deployment.

✨ Key Features
🩺 Conversational interface: Ask medical and healthcare-related questions in natural language.
🤖 LLM-powered responses: Use an integrated language model to generate answers.
🔎 Knowledge retrieval: Use LangChain and Pinecone to retrieve relevant information from an indexed medical knowledge base.
📚 Vector indexing pipeline: Generate and store embeddings for document retrieval using store_index.py.
🌐 Web application: Interact with the chatbot through a Flask-powered interface.
☁️ Cloud deployment: Support a container-based deployment workflow on AWS.
🔄 CI/CD automation: Use GitHub Actions and a self-hosted runner to automate deployment tasks.
🖥️ Application Preview
Home Page

<p align="center">
<img src="https://github.com/user-attachments/assets/eb4404a0-af52-436a-9dcc-0c29d7ca2f5c" alt="Medivya medical chatbot home page" width="100%" />
</p>

Medivya Responding to Medical Queries

<p align="center">
<img src="https://github.com/user-attachments/assets/51539686-e2fe-49be-a8df-2352a4c3b58d" alt="Medivya answering a user's medical query" width="100%" />
</p>

🛠️ Tech Stack
Technology	Purpose
Python 3.10	Core application logic
Flask	Web application and HTTP routing
LangChain	LLM orchestration and retrieval integration
OpenAI API	Language-model integration
Pinecone	Vector database for indexed knowledge retrieval
HTML, CSS, JavaScript	Web interface technologies, where used
Conda	Python environment management
Docker	Application containerization for deployment
AWS ECR	Container image storage
AWS EC2	Cloud compute for hosting
GitHub Actions	CI/CD workflow automation
Note: The original project notes mention Gemini as part of the technology stack, while the supplied configuration specifies OPENAI_API_KEY. This README documents the OpenAI configuration used in the setup instructions. Verify the actual model provider configured in the source code before documenting Gemini as an active integration.
🏗️ How It Works

At a high level, the application follows a retrieval-augmented question-answering workflow.

mermaid
flowchart TD
    A[Medical Documents] --> B[Document Processing and Embeddings]
    B --> C[Pinecone Vector Database]
    D[User Medical Question] --> E[Flask Web Application]
    E --> F[LangChain Retrieval Pipeline]
    C --> F
    F --> G[Language Model]
    G --> H[Response to User]

Workflow
Medical documents are processed by the indexing pipeline.
Document embeddings are generated and stored in Pinecone.
A user submits a question through the web interface.
The application retrieves relevant information from the configured vector index.
The language model uses the available context to generate a response.
The response is returned through the chatbot interface.

The exact document-processing, embedding, retrieval, and model configuration depends on the implementation in the repository.

🚀 Getting Started

Follow these steps to set up Medivya locally.

Prerequisites

Make sure you have the following installed or configured:

Git
Anaconda or Miniconda
Python 3.10
An OpenAI API key
A Pinecone account and API key

You will also need access to the configured Pinecone index and any model or embedding services required by the application.

Step 1: Clone the Repository

Open a terminal and run:

bash
git clone https://github.com/SakshamRaj1/Medivya-Medical-Chatbot.git
cd Medivya-Medical-Chatbot

Step 2: Create and Activate the Conda Environment

Create a dedicated environment with Python 3.10:

bash
conda create -n medivya python=3.10 -y
conda activate medivya


If Conda activation fails in Git Bash, initialize the appropriate shell from Anaconda Prompt:

bash
conda init bash


Restart the terminal and activate the environment again:

bash
conda activate medivya

Step 3: Install Dependencies

Install the packages specified by the project:

bash
python -m pip install --upgrade pip
pip install -r requirements.txt


If you need to use the environment as a Jupyter kernel, install ipykernel:

bash
conda install -n medivya ipykernel -y


This additional package is optional for running the web application unless your workflow requires it.

Step 4: Configure Environment Variables

Create a file named .env in the repository root directory.

Add your API credentials:

ini
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key


Replace the placeholders with your actual credentials.

Security best practices:

Never commit your .env file or API keys to GitHub.
Confirm .env is included in .gitignore.
Use GitHub Actions Secrets for deployment credentials.
Rotate any credentials that have been accidentally exposed.
Ensure the Pinecone index configuration and embedding dimensions match the implementation.

The application must load these variables from the environment using the configuration mechanism supported by the project.

Step 5: Build the Vector Index

Run the indexing script:

bash
python store_index.py


This step prepares the vector database for retrieval according to the project's indexing implementation.

Before running it, make sure that:

Your Pinecone API key is valid.
The configured Pinecone index exists or can be created by the script.
Required source documents are available.
Any embedding model dependencies and credentials are configured.

Run this step again only when necessary, such as when setting up a fresh index or updating the indexed documents.

Step 6: Start the Application

Launch the Flask application:

bash
python app.py


Open the local address configured by the Flask application in your browser.

The default Flask development address is often:

http://127.0.0.1:5000/

If the application specifies another port, use the address printed in your terminal or configured in app.py.

You should now be able to interact with Medivya through its web interface.

For local development, Flask's built-in server is convenient. Use an appropriately configured production server and secure deployment settings for public-facing environments.
⚙️ Configuration Reference
Variable	Description
OPENAI_API_KEY	API credential for the configured OpenAI integration
PINECONE_API_KEY	API credential for Pinecone
ECR_REPO	AWS ECR repository URI used by the deployment workflow
AWS_ACCESS_KEY_ID	AWS IAM access key for deployment
AWS_SECRET_ACCESS_KEY	AWS IAM secret access key
AWS_DEFAULT_REGION	AWS region containing the deployment resources

The AWS variables are required only if the corresponding deployment workflow uses them. Configure additional model, index, or embedding variables if the source code requires them.

☁️ Deployment on AWS

Medivya can be deployed using a container-based workflow involving Amazon EC2, Amazon ECR, Docker, and GitHub Actions.

The intended deployment process is:

Build a Docker image of the application.
Push the image to Amazon ECR.
Run the deployment workflow.
Pull the image onto the EC2 host.
Start or update the application container.

The following steps describe the infrastructure setup. Actual automation depends on the repository's Dockerfile and workflow configuration.

Step 1: Create an AWS IAM User

Sign in to the AWS Management Console.

Create an IAM identity for deployment with the minimum permissions required to:

Authenticate with Amazon ECR.
Push and pull container images.
Access the necessary EC2 deployment resources, if the workflow manages EC2 through the AWS API.

The original setup mentions these managed policies:

AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess

These policies are broad. For a more secure deployment, use narrowly scoped permissions limited to the required ECR repository and EC2 actions.

Do not store AWS access keys in source code or commit them to the repository.

Step 2: Create an Amazon ECR Repository

Open Amazon ECR in the AWS Console and create a repository named:

text
medicalbot


For the original configuration, the repository URI was:

text
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot


This URI is specific to the AWS account and region in the original setup. Use the URI displayed in your own ECR console if your account or region differs.

Step 3: Launch an EC2 Instance

Create an Ubuntu EC2 instance and configure its security group.

At a minimum:

Restrict SSH access to trusted IP addresses.
Allow inbound HTTP or HTTPS traffic as required by your deployment.
Avoid exposing unnecessary ports.
Use a suitable instance size for the application.
Keep the operating system and installed packages updated.
Step 4: Install Docker on EC2

Connect to the EC2 instance and install Docker.

Update the package index:

bash
sudo apt-get update -y
sudo apt-get upgrade -y


Install Docker using the official convenience script:

bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh


Allow the default Ubuntu user to access Docker:

bash
sudo usermod -aG docker ubuntu
newgrp docker


Verify the installation:

bash
docker --version
docker run hello-world


Review Docker's installation documentation and security guidance before using this approach on a production host.

Step 5: Configure a GitHub Actions Self-Hosted Runner

In your GitHub repository:

Open Settings.
Navigate to Actions → Runners.
Select New self-hosted runner.
Choose Linux and the appropriate architecture.
Follow the generated instructions to download, configure, and start the runner on the EC2 instance.

Use the commands provided by GitHub for your specific runner configuration.

Security note: A self-hosted runner executes workflow code on its host. Do not run untrusted pull-request workflows on a production deployment runner. Prefer a dedicated runner with restricted permissions and carefully controlled repository access.

Step 6: Configure GitHub Actions Secrets

Navigate to:

Repository → Settings → Secrets and variables → Actions

Add the following repository secrets or variables as appropriate.

Name	Purpose
AWS_ACCESS_KEY_ID	AWS deployment access key
AWS_SECRET_ACCESS_KEY	AWS deployment secret
AWS_DEFAULT_REGION	AWS region, such as us-east-1
ECR_REPO	Full ECR repository URI
PINECONE_API_KEY	Pinecone API key
OPENAI_API_KEY	OpenAI API key

For sensitive values, use GitHub Actions Secrets. Non-sensitive configuration can be stored as Actions Variables if the workflow is designed to read variables.

Never print secrets in workflow logs.

Step 7: Run the CI/CD Pipeline

Once the infrastructure, runner, secrets, and workflow are configured:

Push your changes to the branch monitored by the workflow.
Open the Actions tab in GitHub.
Check that the workflow builds the Docker image.
Confirm that the image is pushed to ECR.
Verify that the EC2 deployment step pulls and runs the updated image.
Check the application logs and access the application through the configured endpoint.

A successful image build alone does not guarantee a successful deployment. Verify that the container starts correctly and can access its required environment variables and external services.

Deployment Flow
mermaid
flowchart TD
    A[Developer Pushes Code] --> B[GitHub Actions Workflow]
    B --> C[Build Docker Image]
    C --> D[Push Image to Amazon ECR]
    D --> E[EC2 Deployment Runner]
    E --> F[Pull Latest Image]
    F --> G[Start or Update Container]
    G --> H[Medivya Web Application]

🔐 Security Considerations

Because the application integrates external AI and database services, keep the following practices in mind:

Store credentials in environment variables or a managed secrets service.
Exclude .env files and private credentials from version control.
Apply least-privilege IAM permissions.
Protect the EC2 host and self-hosted runner.
Use HTTPS for public deployments.
Avoid logging API keys or sensitive user inputs.
Review how chat messages are processed, stored, and transmitted before collecting personal or medical information.
Monitor API usage and set appropriate spending limits where supported.
🧪 Troubleshooting
Conda command not found

Open Anaconda Prompt and run:

bash
conda init bash


Restart Git Bash and activate the environment:

bash
conda activate medivya

Missing or invalid API key

Verify that the .env file is in the expected directory and contains valid credentials. Check that the application loads the variables correctly.

Pinecone index or embedding errors

Verify that the index configuration matches the embedding model's expected dimensions and that the correct index is being used.

Application starts but the page is inaccessible

Check the address and port printed in the terminal. Confirm that the Flask application started successfully and that any firewall or security group rules permit the required traffic.

Docker deployment fails

Check the GitHub Actions logs, Docker build output, ECR authentication, image URI, and EC2 container logs. Ensure the deployed container receives the required runtime environment variables.

🔮 Future Improvements

Potential enhancements for Medivya include:

Add automated tests for the web application and retrieval pipeline.
Improve source attribution so users can inspect the medical information behind a response.
Add input validation, rate limiting, and robust error handling.
Evaluate answer quality and retrieval accuracy using a curated test dataset.
Improve accessibility and mobile responsiveness.
Add structured application logging and health checks.
Strengthen deployment automation with health verification and rollback support.
Provide clearer uncertainty communication for medical questions.

These are suggested improvements, not claims that the features are already implemented.

🤝 Contributing

Contributions and suggestions are welcome.

Fork this repository.
Create a feature branch:
bash
git checkout -b feature/your-feature

Make your changes and test them locally.
Commit your changes:
bash
git add .
git commit -m "Add: describe your changes"

Push the branch:
bash
git push origin feature/your-feature

Open a pull request describing your changes.

Please do not include API keys, private information, or real patient data in commits, issues, screenshots, or test fixtures.

⚠️ Disclaimer

Medivya is an educational software project and is not a substitute for professional medical advice, diagnosis, or treatment.

AI-generated medical responses may be incomplete, inaccurate, outdated, or inappropriate for an individual's circumstances. Do not rely on this application alone to make medical decisions.

Consult a qualified healthcare professional for personal medical concerns.
In an emergency, contact local emergency services or seek immediate medical care.
Do not use the application to delay professional evaluation or treatment.
Do not submit personally identifiable or sensitive health information unless the system has been appropriately assessed and secured for that purpose.

The developers make no guarantee that generated responses are clinically accurate or suitable for any particular patient.

👨‍💻 Author

Saksham Raj

GitHub: @SakshamRaj1
Project: Medivya — Medical Chatbot
📄 License

Refer to the repository's license file, if present, for the terms governing use, modification, and redistribution.

<p align="center">
<strong>Medivya — Bringing conversational AI to medical information.</strong>
<br />
<sub>Built for learning, experimentation, and responsible AI development.</sub>
</p>

# Medivya: Medical-Chatbot

## Home Page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/eb4404a0-af52-436a-9dcc-0c29d7ca2f5c" />


## Medivya responding to user medical queries
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/51539686-e2fe-49be-a8df-2352a4c3b58d" />


# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/SakshamRaj1/Medivya-Medical-Chatbot.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medivya python=3.10 -y
```

```bash
conda activate medivya
```


```bash
# Run in Anaconda Prompt if Git bash shows: command not found
conda init bash
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
conda install -n medivya ipykernel
```

### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Gemini
- Pinecone
- Flask



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY
