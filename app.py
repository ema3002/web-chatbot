from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import PyPDF2
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = Flask(__name__)

messages = [
    {"role": "system", "content": "You are a helpful assistant named Baymax."}
]

pdf_text = ""

def chat(user_input):
    if pdf_text:
        # PDF mode — PDF থেকে উত্তর দেবে
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are Baymax, a helpful assistant.
Answer questions based on this document:

{pdf_text}

If the answer is not in the document, say 'This is not in the document.'"""
                },
                {"role": "user", "content": user_input}
            ]
        )
    else:
        # Normal chat mode
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })

    return response.choices[0].message.content

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json["message"]
    reply = chat(user_input)
    return jsonify({"reply": reply})

@app.route("/upload", methods=["POST"])
def upload():
    global pdf_text
    file = request.files["pdf"]
    reader = PyPDF2.PdfReader(file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text()
    return jsonify({"message": "✅ PDF loaded! Now ask me anything about it."})

@app.route("/clear", methods=["POST"])
def clear():
    global pdf_text
    pdf_text = ""
    return jsonify({"message": "PDF cleared! Back to normal chat."})

if __name__ == "__main__":
    app.run(debug=True)
