import openai
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_AI_KEY")  # Replace with your real key
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get("message", "")
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or gpt-4
            messages=[
                {"role": "system", "content": "You are Mr AR, a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500
        )
        response_text = completion.choices[0].message.content
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
