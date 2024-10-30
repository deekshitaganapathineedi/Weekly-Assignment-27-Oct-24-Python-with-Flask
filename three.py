from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        result = num1 + num2
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
