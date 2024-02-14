from flask import Flask, render_template, request
from utils import Password

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html', password='Your Password')

@app.route('/new_password', methods=['POST'])
def new_password():
    add_uppercase = False
    add_special = False
    if 'has_uppercase' in request.form:
        add_uppercase = True
    if 'has_special' in request.form:
        add_special = True
    new_password = Password.Password(has_uppercase=add_uppercase, has_special=add_special)
    new_password.generate()
    return render_template('homepage.html', password=new_password.content)

if __name__ == "__main__":
    app.run(debug=True)