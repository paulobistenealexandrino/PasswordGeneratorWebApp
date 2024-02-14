from flask import Flask, render_template
from utils import Password

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html', password='Your Password')

@app.route('/new_password', methods=['POST'])
def new_password():
    new_password = Password.Password()
    new_password.generate()
    return render_template('homepage.html', password=new_password.content)

if __name__ == "__main__":
    app.run(debug=True)