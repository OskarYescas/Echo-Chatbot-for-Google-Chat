import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Retrieve the verification token from environment variables
# This token is set in Cloud Run during deployment.
VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")

@app.route("/", methods=['POST'])
def handle_request():
    """
    Handles incoming requests from Google Chat.
    """
    try:
        event = request.json

        # --- Security Check: Validate the verification token ---
        if event.get("token") != VERIFICATION_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401

        # --- Process the message ---
        event_type = event.get("type")

        if event_type == "MESSAGE":
            # Get the message text from the payload
            message_text = event["message"]["text"]

            # Create the response message
            response_text = f"You said: {message_text}"

            # Google Chat expects a specific JSON format for the response
            return jsonify({"text": response_text})

        elif event_type == "ADDED_TO_SPACE":
            # Respond with a welcome message when added to a space
            if event["space"]["type"] == "ROOM":
                response_text = "Thanks for adding me to this space!"
            else:
                response_text = "Thanks for adding me to this direct message!"

            return jsonify({"text": response_text})

        else:
            return jsonify({}) # Acknowledge other event types

    except Exception as e:
        print(f"Error handling request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
