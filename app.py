from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files/<filename>')
def file(filename):
    return render_template('filename.json',filename=filename)
