from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        a= request.form.get('username')
        b= request.form.get('password')
        if a== "user" and b=="password":
            return "Welcome, user!"
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
