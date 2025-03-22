# MCQ Generator Web App

This project is a **Flask-based web application** that allows users to upload a **PDF file**, extract text from it, and generate **multiple-choice questions (MCQs)** using an **NLP model hosted on Google Colab**.

## Features
- **Upload PDF Files**: Users can upload a PDF, and the app extracts text.
- **MCQ Generation**: The extracted text is sent to a Google Colab server, which returns auto-generated multiple-choice questions.
- **Display MCQs**: The generated questions and their options are displayed on a web page.
- **Uses Pretrained Models**: The backend utilizes NLP models like T5 and Sense2Vec to generate MCQs and distractors.

## Project Structure
```
/mcq-generator
├── app.py                # Flask application
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── result.html       # Results page
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── .gitignore            # Ignore unnecessary files
```

## Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/mcq-generator.git
cd mcq-generator
```

### 2️⃣ Create a Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application
```sh
python app.py
```
The app will be available at `http://127.0.0.1:5000/`.

## Google Colab Integration
The application communicates with a **Google Colab backend** for question generation.

🔹 **Set up the Colab server**: Run the Colab notebook and obtain an `ngrok` URL.  
🔹 **Update `COLAB_SERVER_URL`** in `app.py` to the latest ngrok URL.

## Example Workflow
1. User uploads a **PDF**.
2. Flask extracts text from the PDF.
3. The extracted text is sent to the **Colab server**.
4. The Colab backend processes the text and generates **MCQs**.
5. The MCQs are displayed on a results page.


---
🚀 **Developed with Flask & NLP Models** 🚀