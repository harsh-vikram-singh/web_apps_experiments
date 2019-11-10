from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/upload_data")
def upload_data():
    return render_template("upload_data.html")


if __name__ == "__main__":
    app.run(debug=True)
