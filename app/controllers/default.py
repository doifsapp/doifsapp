from flask import render_template, request
from app import app
import json

@app.route("/")
def home(): 
    return render_template("basic.html")

@app.route('/page-busca')
def page_de_busca():
    return render_template("page_de_busca.html")

@app.route("/painel-de-analise")
def painel_de_analise():
    return render_template("painel_de_analise.html")

@app.route("/painel-grafico")
def painel_grafico():
    return render_template("painel_grafico.html")


