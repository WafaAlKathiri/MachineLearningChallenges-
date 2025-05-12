import os
import logging
from flask import Flask, request, jsonify, render_template
from model_utils import translate_sentence  

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    """Render the index.html file."""
    return render_template("index.html")

@app.route("/health")
def health_check():
    """Provide a simple health check route."""
    return jsonify({"status": "healthy"}), 200

@app.route("/v1/translate", methods=["POST"])
def translate():
    """Provide translation API route."""
    logging.info("Translation request received!")
    user_input = request.form.get("sentence")  # Accepting form data
    if not user_input:
        logging.error("No sentence provided!")
        return jsonify({"error": "No sentence provided"}), 400

    translated_sentence = translate_sentence(user_input)
    logging.info(f"Translated sentence: {translated_sentence}")

    # Render the output page
    return render_template("output.html", input_sentence=user_input, translated_sentence=translated_sentence)


def main():
    """Run the Flask app."""
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()



