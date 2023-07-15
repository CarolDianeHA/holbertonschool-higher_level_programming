const doc = window.$;
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
