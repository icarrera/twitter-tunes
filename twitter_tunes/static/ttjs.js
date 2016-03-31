$(document).ready(function() {
    update_one($('#trends > ul > li:first'));
    $('#trends').on('click', 'li', function(){
      // $('li > article > iframe').toggle();
      update($(this));
      $(this).find('> article > .video-container').toggle();
      $(this).find('article > img').toggle()
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
            if(data.validated == 'true'){
                val_img = trend.find('article > img');
                val_img.attr('src', '../static/Twitter_tunes_logo_1.png');
                console.log(trend.attr('id') + ' has been validated.');
            }
            update_next(trend);
        })
    } else {
        update_next(trend);
    }
}

function update_next(cur_trend){
  next_trend_iframe = cur_trend.next().find('article > .video-container > iframe');
  if(check_loaded(next_trend_iframe)){
    update_one(cur_trend.next());
  }
}

function update_one(trend){
    iframe = trend.find('article > .video-container > iframe');
    $.get('/youtube/' + trend.attr('id'), function(data){
        iframe.attr('src', data.url);
        if(data.validated == 'true'){
            val_img = trend.find('article > img');
            val_img.attr('src', '../static/Twitter_tunes_logo_1.png');
            console.log(trend.attr('id') + ' has been validated.');
        }
    })
}
