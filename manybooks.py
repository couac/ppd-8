import requests
from bs4 import BeautifulSoup

def meta(query):
  r = requests.get('http://manybooks.net/search.php',
    params={'search': query})
  soup = BeautifulSoup(r.text)
  results = soup.find_all('div', {'class': 'grid_12'})
  parsed = []
  for elem in results:
    parsed.append({
      'ident': elem.find('a')['href'].rsplit('/', 1)[1].rsplit('.', 1)[0],
      'titre': elem.find('a').string,
      'auteur': elem.find('p').contents[-1].strip()})
  return parsed

def text(ident):
  return {'status': 'fail'}
