from flask  import Flask, render_template,json, jsonify,  current_app as app
import requests
import os

app = Flask(__name__ , static_folder="static" )

# the professtionalway to create a server directory for an api
@app.route('/movies', methods=['GET']) 
#endpoint 
json_info =''
def catherine_json():
    #computer finds the pathway
    Catherine_info = os.path.join(app.static_folder,'data', 'Catherine.json')
#computer acually reads informations, the r stands for reading meaning the computer is reading information at the  location
    with open(Catherine_info, 'r') as jsondata:
        movies = json.load(jsondata)
    return render_template('movie.html')

@app.route('/api/v1/movies', methods=['GET'])
def api_movies_all():
    json_info =''
    movies_path = os.path.join(app.stastic_folder, 'data', 'movies.json')
with open(movies_path,'r')as raw_json:
    #using with allows for opening and closing of file
    with open(movies_data, 'r') as raw_json:
       movies = json.load(raw_json)
    #no need to return an html template
       return jsonify(raw_json)


#movies_path = os.path.join(app.stastic_folder, 'data', 'movies.json')
#with open(movies_path,'r')as raw_json:
#@app.route('/api/v1/movies/movie_title', methods=[GET])
#def index():
    #name = "Catherine"
    #group_names=[]
                      
#albums_data = os.path.join(app.static_folder, 'data', 'albums.json')

#@app.route('/api/v1/albums/all', methods=['GET'])
#def api_albums_all():
    #using with allows for opening and closing of file
 #   with open(albums_data, 'r') as jsondata:
  #      albums = json.load(jsondata)
    #no need to return an html template
   # return jsonify(albums)


#@app.route('/')
#def index():
  # name "Catherine"
  # group_name= ['Tiana','Cooper','Catherine' 'Richlove' ]
 #@app.route('/richlove')
# def Richlove():
     #return render_template('richlove.html')


#@app.route('/nasa')
#def show_nasa_pic():
    #today = str(date.today())
   # response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)
    #data = response.json()
    #return render_template('nasa.html',data=data)
 

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
     
