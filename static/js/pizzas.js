$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('#search-bar').val();
        // Check the state of the order switch!
        let order
        let my_checkbox = $('#flexSwitchCheckDefault')
        if (my_checkbox.prop('checked')) {
            order = 'name'
        } else {
            order = 'price'
        }
        $.ajax({
            url: '/order/pizzas?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 24rem;">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image"/>
                                    <div class="card-body">
                                    <h4 class="card-title">${d.name}</h4>
                                    <p class="card-text">${d.description}</p>
                                </a>
                                </div>
                            </div>`
                });
                $('.pizza-catalog').html(newHtml.join(''));
                $('#search-bar').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
    $('.category-button').on('click', function(e) {
        e.preventDefault();
        // Strip 'current' class from all buttons in the set
        $('.category-button').removeClass('current');
        $(this).addClass('current');
        let categoryId = $(this).attr('id');
        // Check the state of the order switch!
        let order
        let my_checkbox = $('#flexSwitchCheckDefault')
        if (my_checkbox.prop('checked')) {
            order = 'name'
        } else {
            order = 'price'
        }
        $.ajax({
            url: '/order/pizzas?category_filter=' + categoryId + '&' + 'order_by' + order,
            type: 'GET',
            success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 24rem;">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image"/>
                                    <div class="card-body">
                                    <h4 class="card-title">${d.name}</h4>
                                    <p class="card-text">${d.description}</p>
                                </a>
                                </div>
                            </div>`
                });
                $('.pizza-catalog').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
    $('#my-checkbox').change(function() {
        if (this.checked) {
            // send AJAX request for when checkbox is checked
            $.ajax({
                url: '/my-endpoint-on',
                type: 'POST',
                success: function(data) {
                    console.log('Checkbox is checked');
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            });
        } else {
            // send AJAX request for when checkbox is not checked
            $.ajax({
                url: '/my-endpoint-off',
                type: 'POST',
                success: function(data) {
                    console.log('Checkbox is not checked');
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            });
        }
    });
});

