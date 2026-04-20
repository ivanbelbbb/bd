from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "ЗАЙДИ НА /hello/<твое имя>"

@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Привет, {name}!</h1>"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000) 