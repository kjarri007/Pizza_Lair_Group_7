$(document).ready(function() {
    $('#clear-cart-btn').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/cart/clear',
            type: 'POST',
            success: function(response) {
                location.reload();
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});