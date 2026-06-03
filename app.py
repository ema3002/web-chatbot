from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    ai_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_reply})
    return ai_reply

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json["message"]
    reply = chat(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)