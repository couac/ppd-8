import requests
from bs4 import BeautifulSoup
from bottle import route, response, run
from json import dumps

@route('/meta/:query')
def meta(query):
  r = requests.get('http://www.gutenberg.org/ebooks/search/',
    params={'query': query},
    headers={'User-Agent': 'Mozilla/5.0'})
  soup = BeautifulSoup(r.text)
  results = soup.find_all('li', {'class': 'booklink'})
  response.content_type = 'application/json'
  return dumps([{
    'auteur': elem.find('span', {'class': 'subtitle'}).string,
    'titre': elem.find('span', {'class': 'title'}).string}
    for elem in results])

if __name__ == '__main__':
  run(host='localhost', port=8080, debug=True, reloader=True)
