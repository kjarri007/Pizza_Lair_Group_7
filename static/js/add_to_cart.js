$(document).ready(function(){
    $('.add_to_cart_btn').on('click', function (e) {
        let productId = $(this).val();
        let quantity = $('#num_of_items').val();
        $.ajax({
            url: "user/cart/"
        })
    })
})
    let btn = $(".add_to_cart_btn button");
    btn.click(function(e) {
        addToCart(e);
    });

    function addToCart(e) {
        let product_id = e.target.value;
        let url = "add_to_cart/";
        let data = {id: product_id};

        $.ajax({
            url: url,
            type: "POST",
            contentType: "application/json",
            success: function(data) {
                $("#num_of_items");
                console.log(data);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
