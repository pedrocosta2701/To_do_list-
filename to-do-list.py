from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "admin@gmail.com" and password == "123":
            return "Login certo 🚀"
        else:
            return "Login errado ❌"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
