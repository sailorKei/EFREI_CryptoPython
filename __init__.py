from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #index

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/get_key')
def get_key():
    return f"Voici la clé générée pour cette session : {key.decode()}"

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decrypt(token):
    try:
        message = f.decrypt(token.encode())
        return f"Valeur décryptée : {message.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"

@app.route('/encrypt_custom/<key>/<message>')
def encrypt_custom(key, message):
    try:
        f_custom = Fernet(key.encode())
        token = f_custom.encrypt(message.encode())
        return f"Message encrypté avec votre clé : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement personnalisé : {str(e)}"

@app.route('/decrypt_custom/<key>/<token>')
def decrypt_custom(key, token):
    try:
        f_custom = Fernet(key.encode())
        message = f_custom.decrypt(token.encode())
        return f"Message décrypté avec votre clé : {message.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage personnalisé : {str(e)}"

                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
