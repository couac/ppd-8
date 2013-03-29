function rechercher(recherche) {
  $.getJSON('/meta/' + recherche, function (data) {
    $('#results').empty()
    $.each(data, function (key, value) {
      var items = []
      $.each(value, function (index, value) {
        var elem = '<tr><td><span class="titre">' + value.titre + '</span><br>'
        if (value.auteur !== null)
          elem += '<span class="auteur">' + value.auteur + '</span><br>'
        elem += '</td>' +
          '<td>' +
            '<a href="/text/' + key + '/' + value.ident + '">' +
              '<div class="importer"></div>' +
            '</a>' +
          '</td>'
        items.push(elem + '</tr>')
      })
      if (items.length > 0)
        $('<table/>', {html: items.join('\n')}).appendTo('#results')
      else
        $('<p/>', {html: 'Aucun résultat trouvé.'}).appendTo('#results')
    })
  })
}

$(function () {
  $('form').submit(function () {
    var recherche = $('#barre').val()
    if (recherche.length > 0) {
      rechercher(recherche)
      $('#results').html($('<p/>', {html: 'Recherche en cours...'}))
    }
    return false
  })
})
