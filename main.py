from flask import Flask, request, render_template, send_file
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

@app.route('/cpp/<q>')
def cpp_q(q):
    f = open(f"cpp/p_{q}.cpp", "r")
    code = f.read()
    return code

@app.route('/cpp/<q>/read')
def cpp_read(q):
    f = open(f"cpp/p_{q}.cpp", "r")
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

@app.route("/pc")
def pc():
    #  send pc_pracs.xlsx
    return send_file("pc_pracs.xlsx")

@app.route('/query')
def query():
    q = request.args.get('q')
    ques = request.args.get('ques')

    if ques:
        ques = open(f"dms/Q{ques}.py", "r").read()
        q = f"{ques} \n\n{q.replace("-", " ")}"

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=q
    )
    
    return response.text

if __name__ == '__main__':
    app.run(debug=True)