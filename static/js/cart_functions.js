$(document).ready(function() {
    $('#clear-cart-btn').on('click', function(e) {
        e.preventDefault();
        let command = 'clear';
        $.ajax({
            url: '/user/cart/?command=' + command,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (resp) {
                let newHtml = ``
                $('.item-row-start').html(newHtml);
                $('#cart-total-price').text(resp.total_price);
                $('.cart-num-items').text(resp.num_of_items);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    $('#remove-item-btn').on('click', function(e) {
        e.preventDefault();
        let command = 'remove';
        let itemId = $(this).val();
        $.ajax({
            url: '/user/cart/?command=' + command + '&item=' + itemId,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (resp) {
                $('#cart-item-' + itemId).remove();
                let newHtml = ``;
                $('.item-row-start').html(newHtml);
                $('#cart-total-price').text(resp.total_price);
                $('.cart-num-items').text(resp.num_of_items);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    $('.item-quantity').change(function (e) {
        e.preventDefault();
        let command = 'update-quantity'
        let itemId = $(this).attr('id');
        let quantity = $(this).val();
        let myElement = 'cart-item-' + itemId
        let user_cart = 'checkout-button-link'
        $.ajax({
            url: '/user/cart/?command=' + command + '&item=' + itemId + '&quantity=' + quantity + '&element=' + myElement + '&user_cart' + user_cart,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
             success: function (resp) {
                $('#cart-total-price').text(resp.cart_price + ' kr');
                $('#' + myElement).text(resp.item_price + ' kr');
                $('#checkout-btn').text(resp.user_cart);
                $('#checkout-button-link').attr('href', '/user/checkout/?cart=' + resp.cart_id);
            },
            error: function(xhr, status, error) {
                console.error(error);
            },
        });
    });
});