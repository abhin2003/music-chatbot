from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "play" in user_message:
        response = "🎵 Playing your requested song..."
    elif "lyrics" in user_message:
        response = "📝 Fetching lyrics..."
    elif "recommend" in user_message or "mood" in user_message:
        response = "🎧 Recommending music based on mood..."
    elif "search" in user_message:
        response = "🔍 Searching for song or artist..."
    else:
        response = "❓ Sorry, I didn't understand that."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
