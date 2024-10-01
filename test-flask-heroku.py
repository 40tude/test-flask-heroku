import logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)  # set logging level. Msg>= info are recorded


@app.route("/")
def home() -> str:
    # DEBUG, INFO, WARNING, ERROR, CRITICAL
    app.logger.info("access to home page")
    return "Hello, Flask!"


# This code is NOT executed while on Heroku
if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
