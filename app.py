# app.py

from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load HuggingFace Question Answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Advanced AI Doubt Clearing System API. Use POST /ask to submit your questions."

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    context = data.get('context')
    questions = data.get('questions')
    
    if not context:
        return jsonify({'error': 'No context provided'}), 400
    if not questions:
        return jsonify({'error': 'No questions provided'}), 400
    if not isinstance(questions, list):
        return jsonify({'error': 'Questions must be provided as a list'}), 400

    responses = []
    for question in questions:
        result = qa_pipeline({'question': question, 'context': context})
        responses.append({
            'question': question,
            'answer': result['answer'],
            'confidence': result['score']
        })
    
    return jsonify({'responses': responses})

if __name__ == '__main__':
    app.run(debug=True)
