from flask import Flask,render_template

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def index():
    return "Зайди на сервер /hello/имя"

@app.route("/hello/<name>")
def hello(name):
    return render_template('index.html',name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)