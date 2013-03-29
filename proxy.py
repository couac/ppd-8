from bottle import route, redirect, static_file, run

@route('/')
def index():
  redirect('/rechercher.html')

@route('/:fichier')
def static(fichier):
  return static_file(fichier, root='static')

from gutenberg import meta as g_meta
from manybooks import meta as m_meta

@route('/meta/:query')
def meta(query):
  reply = {}
  reply['gutenberg'] = g_meta(query)
  reply['manybooks'] = m_meta(query)
  return reply

from gutenberg import meta as g_text
from manybooks import meta as m_text

@route('/text/:source/:ident')
def text(source, ident):
  return {'gutenberg': g_text,
          'manybooks': m_text}[source](ident)

if __name__ == '__main__':
  run(host='localhost', port=8080, debug=True, reloader=True)
