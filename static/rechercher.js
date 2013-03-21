function rechercher(recherche) {
  $.getJSON('/meta/' + recherche, function(data) {
    var items = []
    $.each(data, function(index, value) {
      var elem = '<li><span class="titre">' + value.titre + '</span><br>'
      if (value.auteur !== null)
        elem += value.auteur
      items.push(elem + '</li>')
    })
    if (items.length > 0)
      $('#results').html($('<ul/>', {html: items.join('\n')}))
    else
      $('#results').html('<p>Aucun résultat trouvé.</p>')
  })
}

$(function () {
  $('form').submit(function () {
    var recherche = $('#barre').val()
    if (recherche.length > 0) {
      rechercher(recherche)
      $('#results').html('<p>Recherche en cours...</p>')
    }
    return false
  })
})
