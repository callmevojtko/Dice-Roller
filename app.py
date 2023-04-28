from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number_picked = request.json['numberPicked']
        dice_rolls = roll_dice(int(number_picked))
        return jsonify(dice_rolls)
    return render_template('index.html')


def roll_dice(amount_of_dice):
    possible_faces = [1, 2, 3, 4, 5, 6]
    results = []
    for _ in range(amount_of_dice):
        roll = random.choice(possible_faces)
        results.append(roll)
    return results


if __name__ == '__main__':
    app.run(debug=True)
