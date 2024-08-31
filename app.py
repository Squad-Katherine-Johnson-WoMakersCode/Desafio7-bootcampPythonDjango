from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)


"""Listagem dos personagens"""
@app.route("/")  #rota principal/página inicial - listagem dos personagens
def get_list_character_page():
    
    #esta variável vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character" 

    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


"""Detalhes do personagem"""
@app.route("/profile/<id>")  #rota para personagem específico
def get_profile(id):
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/character/" + id
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)

    return render_template("profile.html", profile = dict)