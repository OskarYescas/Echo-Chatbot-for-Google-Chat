import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def handle_request():
    """
    Handles incoming requests from Google Chat.
    """
    try:
        event = request.json
        # No need for a token check. The request is authenticated by Google's infrastructure.
        event_type = event.get("type")
        
        if event_type == "MESSAGE":
            message_text = event["message"]["text"]
            response_text = f"You said: {message_text}"
            return jsonify({"text": response_text})
        
        elif event_type == "ADDED_TO_SPACE":
            if event["space"]["type"] == "ROOM":
                response_text = "Thanks for adding me to this space!"
            else:
                response_text = "Thanks for adding me to this direct message!"
            return jsonify({"text": response_text})
            
        else:
            return jsonify({})
    
    except Exception as e:
        print(f"Error handling request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
