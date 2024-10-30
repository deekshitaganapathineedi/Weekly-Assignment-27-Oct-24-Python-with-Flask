from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "abc", "age": 25, "city": "lmn"},
    {"name": "uvw", "age": 30, "city": "lmn"},
    {"name": "xyz", "age": 35, "city": "lmn"}
]

@app.route('/table')
def table():
    return render_template('table.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
