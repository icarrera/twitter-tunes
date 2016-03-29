$(document).ready(function() {
    // console.log($('#trends > ul > li:first').attr('id'));
    update($('#trends > ul > li:first').attr('id'));
});

function update(trend){
    $.get('/youtube/' + trend, function(data){
        $('#iframe_' + trend).attr('src', data.url)
    })
}
