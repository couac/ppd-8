function search(source, query) {
  $.getJSON('/meta/' + source + '/' + query, function (data) {
    var items = []
    $.each(data.results, function (index, value) {
      var elem = '<tr><td><span class="titre">' + value.titre + '</span><br>'
      if (value.auteur !== null)
        elem += '<span class="auteur">' + value.auteur + '</span><br>'
      elem += '</td>' +
        '<td>' +
          '<a href="/text/' + source + '/' + value.ident + '">' +
            '<div class="importer"></div>' +
          '</a>' +
        '</td>'
      items.push(elem + '</tr>')
    })
    if (items.length > 0)
      $('#' + source).html($('<table/>', {html: items.join('\n')}))
    else
      $('#' + source).html($('<p/>', {html: 'Nothing found :-('}))
  })
}

$(function () {
  $('form').submit(function () {
    var query = $('#barre').val()
    if (query.length > 0) {
      $('#results').html('<table><tr></tr></table>')
      $('form > input[type="checkbox"]:checked').each(function () {
        source = $(this).attr('name')
        $('#results > table tr:first-child').append('<td id="' + source + '"><p>Loading . . .</td>')
        search(source, query)
      })
    }
    return false
  })
})
