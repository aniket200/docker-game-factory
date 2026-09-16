from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "snake"
    }), 200


@app.route("/api/status")
def status():
    return jsonify({
        "application": "Docker Game Factory",
        "game": "Snake",
        "status": "running",
        "containerized": True
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
