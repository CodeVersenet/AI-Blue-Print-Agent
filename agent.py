import vertexai
from vertexai.preview.language_models import TextGenerationModel

vertexai.init(project="my-hackathon--project-2025", location="us-central1")

model = TextGenerationModel.from_pretrained("text-bison")

response = model.predict(
    "Explain what an AI Agent does in the context of software development.",
    temperature=0.7,
    max_output_tokens=256,
)

print("AI Response:", response.text)
