from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

chat_history = []

def chatbot_reply(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "how are you" in user_input:
        return "I'm fine! Thanks for asking."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_message", methods=["POST"])
def get_message():
    data = request.get_json()
    user_msg = data.get("message")

    bot_reply = chatbot_reply(user_msg)

    chat_history.append({"user": user_msg, "bot": bot_reply})

    return jsonify({"reply": bot_reply, "history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)

