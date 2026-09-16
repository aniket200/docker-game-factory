from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"
game_over = False


def check_winner():
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
            and board[a] == board[c]
        ):
            return board[a]

    if all(cell != "" for cell in board):
        return "draw"

    return None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def make_move():

    global current_player
    global game_over

    data = request.get_json()

    if not data or "position" not in data:
        return jsonify({
            "error": "Position is required"
        }), 400

    position = data["position"]

    if not isinstance(position, int):
        return jsonify({
            "error": "Invalid position"
        }), 400

    if position < 0 or position > 8:
        return jsonify({
            "error": "Position must be between 0 and 8"
        }), 400

    if game_over:
        return jsonify({
            "error": "Game is already over"
        }), 400

    if board[position] != "":
        return jsonify({
            "error": "Cell already occupied"
        }), 400

    # Place current player's symbol
    board[position] = current_player

    # Check winner
    winner = check_winner()

    if winner:

        game_over = True

        return jsonify({
            "board": board,
            "winner": winner,
            "current_player": current_player,
            "game_over": True
        })

    # Switch player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return jsonify({
        "board": board,
        "winner": None,
        "current_player": current_player,
        "game_over": False
    })


@app.route("/reset", methods=["POST"])
def reset_game():

    global board
    global current_player
    global game_over

    board = [""] * 9

    current_player = "X"

    game_over = False

    return jsonify({
        "board": board,
        "current_player": current_player,
        "winner": None,
        "game_over": False
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "service": "tic-tac-toe"
    }), 200


@app.route("/api/status")
def status():

    return jsonify({
        "application": "Docker Game Factory",
        "game": "Tic-Tac-Toe",
        "status": "running",
        "containerized": True,
        "current_player": current_player
    }), 200


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
