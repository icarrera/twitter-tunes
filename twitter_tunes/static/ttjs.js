$(document).ready(function() {
    update_one($('#trends > ul > li:first'));
    $('#trends').on('click', 'li', function(){
      // $('li > article > iframe').toggle();
      update($(this));
      $(this).find('> article > .video-container').toggle();
    })
});

function check_loaded(iframe){
    if(iframe.attr('src') == '../static/loading.gif'){
        return true;
    }
    return false;
}

function update(trend){
    iframe = trend.find('article > .video-container > iframe');
    if(check_loaded(iframe)){
        $.get('/youtube/' + trend.attr('id'), function(data){
            iframe.attr('src', data.url);
            update_next(trend);
        })
    } else {
        update_next(trend);
    }
}

function update_next(cur_trend){
  next_trend_iframe = cur_trend.next().find('article > .video-container > iframe');
  // next_trend_iframe = cur_trend.next().children('article').children('.video-container').children('iframe');
  if(check_loaded(next_trend_iframe)){
    update_one(cur_trend.next());
  }
}

function update_one(trend){
    iframe = trend.find('article > .video-container > iframe');
    $.get('/youtube/' + trend.attr('id'), function(data){
        iframe.attr('src', data.url);
    })
}
