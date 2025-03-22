from flask import Flask, request, render_template, jsonify
import PyPDF2
import requests

app = Flask(__name__)

# Replace this with your Colab server URL
COLAB_SERVER_URL = "https://5491-34-86-229-26.ngrok-free.app/generate"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']

    # Ensure a file is uploaded
    if not file.filename.endswith('.pdf'):
        return "Only PDF files are allowed", 400

    # Extract text from the PDF
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        return f"Error reading the PDF: {e}", 500

    # Send text to Colab for processing
    try:
        response = requests.post(COLAB_SERVER_URL, json={"text": text})
        if response.status_code != 200:
            return f"Error from Colab: {response.text}", 500

        # Ensure that the response has the correct data
        questions = response.json().get("questions", [])
        
        # Check if the questions contain both the options and answers
        if not questions:
            return "No questions generated from the content.", 500
    except Exception as e:
        return f"Error connecting to Colab: {e}", 500

    # Parse the questions and options into a structured format
    parsed_questions = []
    for question in questions:
        # Parse the question string to extract the options and the correct answer
        question_text = question.strip().split("\n")
        
        # Separate the options and correct answer
        options = []
        correct_answer = ""
        for i, line in enumerate(question_text):
            if line.startswith("(a)") or line.startswith("(b)") or line.startswith("(c)") or line.startswith("(d)"):
                options.append(line.strip())
            if line.startswith("Correct answer is"):
                correct_answer = line.split(":")[1].strip()

        parsed_questions.append({
            "question": question_text[0],
            "options": options,
            "correct_answer": correct_answer
        })

    return render_template('result.html', questions=parsed_questions)

if __name__ == '__main__':
    app.run(debug=True)
