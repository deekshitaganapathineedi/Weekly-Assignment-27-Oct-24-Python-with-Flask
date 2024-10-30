from flask import Flask, request, render_template

app = Flask(__name__)
feedbacks = []

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        feedback = request.form.get('feedback')
        feedbacks.append({'name': name, 'feedback': feedback})
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
