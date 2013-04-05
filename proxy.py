from bottle import route, redirect, static_file, request, run
from importlib import import_module

@route('/')
def index():
  redirect('/rechercher.html')

@route('/:fichier')
def static(fichier):
  return static_file(fichier, root='static')

sources = {
  'gutenberg': import_module('gutenberg'),
  'manybooks': import_module('manybooks')}

@route('/meta/:source/:query')
def meta(source, query):
  if source in sources:
    return {
      'source': source[0].capitalize() + source[1:],
      'results': sources[source].meta(query)}

@route('/text/:source/:ident')
def text(source, ident):
  if source in sources:
    return sources[source].text(ident)

if __name__ == '__main__':
  run(host='localhost', port=8080, debug=True, reloader=True)
