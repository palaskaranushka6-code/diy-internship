from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/explore/')
def explore():
    return "Welcome to Explore Page 🚀"

if __name__ == '__main__':
    app.run(debug=True)