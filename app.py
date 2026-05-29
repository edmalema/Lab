from flask import Flask, render_template, request, url_for, session, flash, jsonify
import os
import mysql.connector
from dotenv import find_dotenv, load_dotenv

app = Flask(__name__)

app.secret_key = "SuperSecretKey"


@app.route("/ping/<navn>", methods=["GET"])
def ping(navn):
    print(navn)
    return render_template("ping.html", navn = navn)