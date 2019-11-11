from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
# from pathlib import Path

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # folder = Path("user_uploads")
        f.save("user_uploads/" + secure_filename(f.filename))
    return """
    <h1>File uploaded. Backend not ready yet</h1>
    """


if __name__ == "__main__":
    app.run(debug=True)
