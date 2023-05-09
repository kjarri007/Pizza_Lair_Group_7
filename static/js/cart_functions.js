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
    $('.cart-remove-item').on('click', function(e) {
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
                let newHtml = resp.data.map(d => {
                    return `<tr>
                                <td class="p-4">
                                    <div class="media align-items-center">
                                        <h2 class="d-block">${d.product.name}</h2>
                                        <img src="${d.product.productimg_set.first.image}" class="d-block mg-fluid" style="height: 16rem" alt="cart image">
                                        <div class="media-body">
                                    </div>
                                    </div>
                                </td>
                                <td class="text-right font-weight-semibold align-middle p-4">${d.product.price}</td>
                                <td class="align-middle p-4"><input type="number" step="1" min="1" max="99" class="form-control text-center" value="${d.quantity}"></td>
                                <td class="text-right font-weight-semibold align-middle p-4">${d.price}</td>
                                <td class="text-center align-middle px-0"><button id="cart-remove-item" class="shop-tooltip close float-none text-danger" data-original-title="Remove">X</button></td>
                              </tr>`
                })
                $('.item-row-start').html(newHtml.join(''));
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
        $.ajax({
            url: '/user/cart/?command=' + command + '&item=' + itemId + '&quantity=' + quantity,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
             success: function (resp) {
                $('#cart-total-price').text(resp.cart_price + ' kr');
                $('#' + myElement).text(resp.item_price + ' kr')
                // $('#checkout-btn').text(resp.num_of_items);
            },
            error: function(xhr, status, error) {
                console.error(error);
            },
        });
    });
});