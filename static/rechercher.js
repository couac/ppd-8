function search(source, query) {
  $.getJSON('/meta/' + source + '/' + query, function (data) {
    var items = []
    $.each(data.results, function (index, value) {
      var elem = '<article>' +
        '<h3 class="titre">' + value.titre + '</h3>'
      if (value.auteur !== null)
        elem += '<p class="auteur">' + value.auteur + '</p>'
      elem += '<aside>' +
        '<a href="/text/' + source + '/' + value.ident + '">' +
          '<div class="importer"></div>' +
        '</a>'
      items.push(elem + '</aside></article>')
    })
    if (items.length > 0) {
      $('#' + source).html('<h2>Results from ' + data.source + ' (' + items.length + ')</h2>')
      $('#' + source).append(items.join('\n'))
    } else
      $('#' + source).html('<p>Nothing found :-(</p>')
  })
}

$(function () {
  $('form').submit(function () {
    var query = $('#barre').val()
    if (query.length > 0) {
      $('#results').empty()
      $('input[type="checkbox"]:checked').each(function () {
        source = $(this).attr('name')
        $('#results').append('<section id="' + source + '">' +
          '<p>Loading from ' + $(this).next().text() + ' . . .</p></section>')
        search(source, query)
      })
    }
    return false
  })
})
