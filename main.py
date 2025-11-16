# main.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Workout Bot is running!"

@app.route('/health')  
def health():
    return "✅ Healthy"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Starting server on port {port}")
    app.run(host='0.0.0.0', port=port)
