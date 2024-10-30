from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Keep going.",
    "Stay positive.",
    "You got this!",
    "Choose joy.",
    "Dream big."
]

@app.route('/quote')
def quote():
    selected_quote = random.choice(quotes)
    return render_template('quote.html', quote=selected_quote)

if __name__ == '__main__':
    app.run(debug=True)
