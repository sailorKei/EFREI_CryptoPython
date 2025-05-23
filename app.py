from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenue dans votre atelier Crypto Python Klorane !'

if __name__ == '__main__':
    app.run()

@app.route("/encrypt/<text>")
def encrypt(text):
    token = cipher.encrypt(text.encode())
    return token.decode()
