from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def start():
    return "this is my first vercel deployment"

@app.route("/trial")
def trial():
    return render_template('index.html')


    
    