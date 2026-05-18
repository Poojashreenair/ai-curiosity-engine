import os
from dotenv import load_dotenv  # 1. Import load_dotenv
from flask import Flask, request, jsonify, render_template
from google import genai
from pydantic import BaseModel
from typing import List

# 2. Call load_dotenv() to read your .env file
load_dotenv() 

app = Flask(__name__)

# The client will now automatically find the GEMINI_API_KEY from the .env file!
client = genai.Client()

# 1. Define the Strict JSON Schema using Pydantic
class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str

class DoubtResponse(BaseModel):
    explanation: str
    quiz: List[QuizQuestion]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve_doubt():
    data = request.get_json()
    student_doubt = data.get('doubt', '')

    if not student_doubt:
        return jsonify({"error": "Please provide a doubt."}), 400

    # 2. The Prompt
    prompt = f"""
    You are an enthusiastic Computer Science tutor for young students. 
    A student has asked: '{student_doubt}'.
    
    RULE 1: You must ONLY answer questions related to Computer Science, coding, math, or technology. 
    If the question is unrelated (e.g., history, biology, general advice), politely say: "I am a CS Curiosity Engine! I only know about computers, coding, and tech. Try asking me how a website works!" and generate a dummy 1-question quiz.
    
    RULE 2: Provide a fun, clear, and concise explanation suitable for a middle/high school level. Use emojis if helpful.
    
    RULE 3: Generate a 3-question multiple-choice quiz based ONLY on your explanation.
    """

    try:
        # 3. Call the Gemini API and force structured output
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': DoubtResponse,
            }
        )
        # response.text is guaranteed to be a valid JSON string matching our schema
        return response.text, 200, {'Content-Type': 'application/json'}
        
    except Exception as e:
        print("🚨 AI ERROR TRIGGERED 🚨")
        print(str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)