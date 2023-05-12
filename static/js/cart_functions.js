$(document).ready(function() {
    // This code block executes when the DOM is ready
    // Event handler for the "Clear Cart" button click
    $('#clear-cart-btn').on('click', function(e) {
        e.preventDefault(); // Prevents the default behavior of the click event
        let command = 'clear'; // Specifies the command as 'clear'
        // AJAX request to the server
        $.ajax({
            url: '/user/cart/?command=' + command, // URL to send the request
            type: 'POST', // HTTP method to use
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                // Sends the CSRF token as data to the server
            },
            success: function (resp) {
                // This code block executes if the request is successful
                let newHtml = ``; // Empty string for new HTML content
                $('.item-row-start').html(newHtml); // Updates the HTML content of elements with the class 'item-row-start'
                $('#cart-total-price').text(resp.total_price); // Updates the text of the element with the id 'cart-total-price' with the total price value received in the response
                $('.cart-num-items').text(resp.num_of_items); // Updates the text of elements with the class 'cart-num-items' with the number of items received in the response
            },
            error: function(xhr, status, error) {
                // This code block executes if there is an error in the request
                console.error(error); // Logs the error to the console
            }
        });
    });

    // Event handler for the "Remove Item" button click
    $('.cart-remove-item').on('click', function(e) {
        e.preventDefault(); // Prevents the default behavior of the click event
        let command = 'remove'; // Specifies the command as 'remove'
        let itemId = $(this).val(); // Retrieves the value of the clicked button (assumed to be the item ID)
        let rowToRemove = $('#item-' + itemId); // Identify the specific row to remove
        // AJAX request to the server
        $.ajax({
            url: '/user/cart/?command=' + command + '&item=' + itemId, // URL to send the request, includes the command and item ID as parameters
            type: 'POST', // HTTP method to use
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                // Sends the CSRF token as data to the server
            },
            success: function (resp) {
                // This code block executes if the request is successful
                rowToRemove.remove(); // Remove the row from the DOM
                $('#cart-total-price').text(resp.total_price); // Updates the text of the element with the id 'cart-total-price' with the total price value received in the response
                $('.cart-num-items').text(resp.num_of_items); // Updates the text of elements with the class 'cart-num-items' with the number of items received in the response
            },
            error: function(xhr, status, error) {
                // This code block executes if there is an error in the request
                console.error(error); // Logs the error to the console
            }
        });
    });
    // Event handler for the change event on elements with the class 'item-quantity'
    $('.item-quantity').change(function (e) {
        e.preventDefault(); // Prevents the default
        let command = 'update-quantity'; // Specifies the command as 'update-quantity'
        let itemId = $(this).attr('id'); // Retrieves the ID of the changed element (assumed to be the item ID)
        let quantity = $(this).val(); // Retrieves the new value of the changed element (assumed to be the quantity)
        let myElement = 'cart-item-' + itemId; // Constructs the ID of the element to update
        let user_cart = 'checkout-button-link'; // Specifies the ID of the user cart element

        // AJAX request to the server
        $.ajax({
            url: '/user/cart/?command=' + command + '&item=' + itemId + '&quantity=' + quantity + '&element=' + myElement + '&user_cart=' + user_cart,
            // URL to send the request, includes the command, item ID, quantity, and element IDs as parameters
            type: 'POST', // HTTP method to use
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                // Sends the CSRF token as data to the server
            },
            success: function (resp) {
                // This code block executes if the request is successful
                $('#cart-total-price').text(resp.cart_price + ' kr'); // Updates the text of the element with the id 'cart-total-price' with the updated cart price received in the response
                $('#' + myElement).text(resp.item_price + ' kr'); // Updates the text of the element with the ID 'myElement' with the updated item price received in the response
                $('#checkout-btn').text(resp.user_cart); //id=".checkout-button-link"// Updates the text of the element with the id 'checkout-btn' with the updated user cart value received in the response
                $('#checkout-button-link').attr('href', '/user/checkout/?cart=' + resp.cart_id);
                // Updates the href attribute of the element with the id 'checkout-button-link' with the updated cart ID received in the response
                $('.cart-num-items').text(resp.num_of_items); // Updates the text of elements with the class 'cart-num-items' with the number of items received in the response
            },
            error: function(xhr, status, error) {
                // This code block executes if there is an error in the request
                console.error(error); // Logs the error to the console
            },
        });
    });
});
