from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="minlab2_db",
            user="tarik",
            password="tarik"
        )
        return "Connexion à PostgreSQL réussie 🎉"
    except Exception as e:
        return f"Erreur de connexion : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
