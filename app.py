from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Uzair from Python Flask!'

app.run(host='0.0.0.0', port=5000)
