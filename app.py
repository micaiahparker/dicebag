from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
