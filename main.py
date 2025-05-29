from flask import Flask, request
import os

from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

app = Flask(__name__)

@app.route('/dms/<q>')
def home(q):
    f = open(f"Q{q}.py", "r")
    code = f.read()
    return code

@app.route('/query')
def query():
    q = request.args.get('q')
    if not q:
        return "No query provided", 400
    
    print(f"Received query: {q}")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=q
    )
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)