import requests
from bs4 import BeautifulSoup

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
      'ident': elem.find('a', {'class': 'link'})['href'].rsplit('/', 1)[1],
      'titre': elem.find('span', {'class': 'title'}).string,
      'auteur': auteur})
  return parsed

def text(ident):
  s = {'status': 'fail'}
  if not ident.isdigit():
    s['reason'] = 'not a digit'
    return s
  g = requests.get('http://www.gutenberg.org/ebooks/' + ident + '.txt.utf-8',
    headers={'User-Agent': 'Mozilla/5.0'})
  if not g.ok:
    s['reason'] = 'source http status error'
    return s
  p = requests.post('http://staging.tlhub.af83.com/api/documents/', g.text)
  if not p.ok:
    s['reason'] = 'api http status error'
    return s
  return {'status': 'done'}
