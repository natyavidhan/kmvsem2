from flask import Flask

app = Flask(__name__)

@app.route('/<q>')
def home(q):
    f = open(f"Q{q}.py", "r")
    code = f.read()
    return code

if __name__ == '__main__':
    app.run(debug=True)