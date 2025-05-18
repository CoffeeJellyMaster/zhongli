from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return {"message": "Hello from Flask on Render!"}

if __name__ == "__main__":
    app.run(debug=True)
