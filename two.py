from flask import Flask, render_template
app = Flask(__name__)
@app.route('/bio')
def bio():
    return render_template('bio.html', name="abc", age=25, hobbies="Reading")

if __name__ == '__main__':
    app.run(debug=True)
