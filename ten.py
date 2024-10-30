from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    far= None
    if request.method == 'POST':
        celsius = float(request.form.get('celsius'))
        far= (celsius * 9/5) + 32
    return render_template('convert.html', fahrenheit=far)

if __name__ == '__main__':
    app.run(debug=True)
