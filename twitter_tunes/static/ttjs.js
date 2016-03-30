$(document).ready(function() {
    update_first($('#trends > ul > li:first'));
    $('#trends').on('click', 'li', function(){
        update($(this))
    })
});

function check_loaded(iframe){
    if(iframe.attr('src') == '../static/loading.gif'){
        return true;
    } else {
        return false;
    }
}

function update(trend){
    iframe = trend.children('article').children('iframe')
    if(check_loaded(iframe)){
        console.log('loading...')
        $.get('/youtube/' + trend.attr('id'), function(data){
            iframe.attr('src', data.url)
        })
    } else {
        console.log('src is loaded')
    }
}

function update_first(trend){
    iframe = trend.children('article').children('iframe')
    $.get('/youtube/' + trend.attr('id'), function(data){
        iframe.attr('src', data.url)
    })
}
