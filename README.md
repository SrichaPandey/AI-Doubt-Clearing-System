# AI-Doubt-Clearing-System
AI-driven real-time Q&amp;A system for interactive workshops, bridging learning gaps during live sessions.

# Advanced AI Doubt Clearing System

Developed during IBM Call for Code 2024 Hackathon.

An AI-powered, real-time, scalable question-answering system designed for live classrooms, workshops, and self-learning platforms.

## Features
- Accepts user-defined contexts (e.g., lecture slides, notes)
- Handles multiple questions in a single request
- Provides AI-generated answers along with confidence scores
- Scalable architecture for real-time educational applications

## Tech Stack
- Python 3.9+
- Flask (Web framework)
- HuggingFace Transformers (distilBERT model)

## How It Works
- Users POST their context (lecture content) and list of questions to `/ask`
- AI model returns high-confidence answers dynamically

## Example Request (JSON)
```json
{
    "context": "Machine learning is a subset of AI focused on building systems that learn from data.",
    "questions": [
        "What is machine learning?",
        "Is machine learning different from AI?"
    ]
}


**Status:** Hackathon prototype completed. Further enhancements planned for full deployment.
