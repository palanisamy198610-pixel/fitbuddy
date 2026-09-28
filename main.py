from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/fidbuddy", methods=["POST"])
def fidbuddy():
    data = request.get_json()

    message = data.get("message", "").lower()

    if "hello" in message or "hi" in message:
        reply = "Hi! 👋 I'm FidBuddy. How can I help you?"

    elif "skill" in message:
        reply = "You can add and manage your skills in SkillWallet."

    elif "wallet" in message:
        reply = "Your SkillWallet helps you manage your skills and achievements."

    elif "help" in message:
        reply = "Sure! Tell me what you need help with."

    else:
        reply = "I'm FidBuddy 🤖. Please tell me more about what you need."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
