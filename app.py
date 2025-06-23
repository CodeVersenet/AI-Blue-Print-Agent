import os
from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.preview.language_models import TextGenerationModel

# Set Vertex AI credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my-hackathon-project-2025-3a7fb6137e43.json"

# Initialize Vertex AI
vertexai.init(project="my-hackathon--project-2025", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison")

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    idea = request.form.get("idea")
    if not idea:
        return jsonify({"error": "No idea provided"}), 400
    response = model.predict(idea, temperature=0.7, max_output_tokens=256)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
