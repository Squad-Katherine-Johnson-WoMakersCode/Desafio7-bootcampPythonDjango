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
    
    response = urllib.request.urlopen(url)
    data = response.read()
    profile = json.loads(data)
    
    # Consome os episódios
    episodes = []
    for episode_url in profile['episode']:
        response = urllib.request.urlopen(episode_url)
        episode_data = response.read()
        episode = json.loads(episode_data)
        episodes.append(episode)

    return render_template('profile.html', profile=profile, episodes=episodes)

"""Função para pegar as urls dos personagens"""
def get_character_urls(character_urls):
    characters = []
    
    for url in character_urls:
        response = urllib.request.urlopen(url)
        character_data = response.read()
        character_dict = json.loads(character_data)
        
        character = {
            "name": character_dict["name"],
            "image": character_dict["image"],
            "id": character_dict["id"]
        }
        
        characters.append(character)
    
    return characters

"""Rota para listagem de localizações e dimensões"""
@app.route("/locations")  #listagem dos episódios
def get_list_locations():
    
    #variável url que vai receber a url da api que eu quero consumir
    url = "https://rickandmortyapi.com/api/location" 
    
    #response para usar a classe da lib request para abrir a url definida acima
    response = urllib.request.urlopen(url) 
    
    #criar uma variável para fazer a leitura do resultado
    locations = response.read()
    
    #criar uma variável que vai formatar para um formato json
    dict = json.loads(locations)
    
    locations = []
    
    for location in dict["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension" : location["dimension"]
        }

        locations.append(location)
        
    return render_template("locations.html", locations=dict["results"])

"""Rota para localização por id"""
@app.route("/location/<id>")  
def get_location(id):
    
    url = "https://rickandmortyapi.com/api/location/" + id
    
    response = urllib.request.urlopen(url) 
    
    data = response.read()
    
    dict = json.loads(data)
    
    residents = get_character_urls(dict["residents"])
        
    return render_template("location.html", location=dict, residents=residents)

"""Rota para localização de episódios"""
@app.route('/episodes')
def list_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes = json.loads(data)['results']
    return render_template('episodes.html', episodes=episodes)


"""Rota para localização de episódio por id"""
@app.route('/episodes/<int:episode_id>')
def episode_profile(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)
    return render_template('episode_profile.html', episode=episode)