$(document).ready(function() {
    update($('#trends > ul > li:first'));
    $('#trends').on('click', 'li', function(){
        update($(this))
    })
});

function update(trend){
    console.log(trend.attr('id'))
    $.get('/youtube/' + trend.attr('id'), function(data){
        trend.children('article').children('iframe').attr('src', data.url)
    })
}
