from flask import Flask, request, render_template
import os

from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dms/<q>')
def home(q):
    f = open(f"dms/Q{q}.py", "r")
    code = f.read()
    return code

@app.route('/dms/<q>/read')
def read(q):
    f = open(f"dms/Q{q}.py", "r")
    code = f.read()
    return """<!doctype html>
<html>
<head>
    <title>Document</title>
</head>
<body>
<pre>""" + code + """</pre>
</body>
</html>"""

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