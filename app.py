from flask import Flask, render_template, request
import os
from gptpdf import parse_pdf

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Recomendado: mover para variável de ambiente em produção
OPENAI_API_KEY = "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"  # substitua pela sua chave real

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("pdf_file")
    if not file or not file.filename.endswith(".pdf"):
        return "Arquivo inválido", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    markdown_output, _ = parse_pdf(file_path, api_key=OPENAI_API_KEY)

    return render_template("index.html", markdown=markdown_output)

if __name__ == "__main__":
    app.run(debug=True)
