from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld_views():
    return 'Hello, World! 001'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9999)
