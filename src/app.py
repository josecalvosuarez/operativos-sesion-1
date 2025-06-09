from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    welcome = os.getenv("WELCOME_MSG", "¡Hola desde el contenedor!")
    return f"<h1>{welcome}</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
