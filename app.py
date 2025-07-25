from flask import Flask, render_template
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables only in development
if os.getenv('ENVIRONMENT') == 'development':
    load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Production configuration
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)