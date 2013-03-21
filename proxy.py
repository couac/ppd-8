import requests
from bs4 import BeautifulSoup
from bottle import route, response, run, static_file
from json import dumps

@route('/meta/:query')
def meta(query):
  r = requests.get('http://www.gutenberg.org/ebooks/search/',
    params={'query': query},
    headers={'User-Agent': 'Mozilla/5.0'})
  soup = BeautifulSoup(r.text)
  results = soup.find_all('li', {'class': 'booklink'})
  parsed = []
  for elem in results:
    auteur = elem.find('span', {'class': 'subtitle'})
    if auteur is not None:
      auteur = auteur.string
    parsed.append({
      'titre': elem.find('span', {'class': 'title'}).string,
      'auteur': auteur})
  response.content_type = 'application/json'
  return dumps(parsed)

@route('/:fichier')
def recherche(fichier):
  return static_file(fichier, root='static')

if __name__ == '__main__':
  run(host='localhost', port=8080, debug=True, reloader=True)
