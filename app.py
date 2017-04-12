from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def index():
    return jsonify({'msg': 'Hello!'})

if __name__ == "__main__":
    app.run()
