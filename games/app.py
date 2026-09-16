from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game board
board = [""] * 9


def check_winner():
    """
    Check whether X has won or the game is a draw.
    """

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if (
            board[a] != ""
            and board[a] == board[b]
            and board[b] == board[c]
        ):
            return board[a]

    # Check draw
    if all(cell != "" for cell in board):
        return "draw"

    return None


@app.route("/")
def home():
    """
    Main game page.
    """
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def make_move():
    """
    Process a player move.
    """

    data = request.get_json()

    if not data or "position" not in data:
        return jsonify({
            "error": "Position is required"
        }), 400

    position = data["position"]

    # Validate position
    if not isinstance(position, int):
        return jsonify({
            "error": "Invalid position"
        }), 400

    if position < 0 or position > 8:
        return jsonify({
            "error": "Position must be between 0 and 8"
        }), 400

    # Check if cell is already occupied
    if board[position] != "":
        return jsonify({
            "error": "Cell already occupied"
        }), 400

    # Player move
    board[position] = "X"

    winner = check_winner()

    return jsonify({
        "board": board,
        "winner": winner
    })


@app.route("/reset", methods=["POST"])
def reset_game():
    """
    Reset the game board.
    """

    global board

    board = [""] * 9

    return jsonify({
        "board": board,
        "winner": None
    })


@app.route("/health")
def health():
    """
    Docker health-check endpoint.
    """

    return jsonify({
        "status": "healthy",
        "service": "tic-tac-toe"
    }), 200


@app.route("/api/status")
def status():
    """
    Application status endpoint.
    """

    return jsonify({
        "application": "Docker Game Factory",
        "game": "Tic-Tac-Toe",
        "status": "running",
        "containerized": True
    }), 200


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
