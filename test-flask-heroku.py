from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return "Hello, Flask!"


if __name__ == "__main__":
    # Pas nécessaire avec Gunicorn en production
    # app.run(debug=True)
    app.run()
