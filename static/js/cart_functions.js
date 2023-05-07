$(document).ready(function() {
    $('#clear-cart-btn').on('click', function(e) {
        e.preventDefault();
        let command = 'clear'
        $.ajax({
            url: '/cart?command=' + command,
            type: 'POST',
            success: function (resp) {
                let newHtml = `<h1>Your Pizza Cart Is EMPTY!!!</h1>`
            $('.item-row-start').html(newHtml.join(''));
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});