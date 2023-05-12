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
            url: '/order/pizzas?search_filter=' + searchText + '&order_by=' + order,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 23%;height: 36rem">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image" style="height: 300px">
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">${d.description}</p>
                                        <h3 class="card-text position-absolute bottom-0 end-0 m-2">${d.price} kr</h3>                                    
                                    </div>
                                </a>
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
        // Get the id of the clicked button
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
            url: '/order/pizzas?category_filter=' + categoryId + '&order_by=' + order,
            type: 'GET',
            success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 23%;height: 36rem">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image" style="height: 300px">
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">${d.description}</p>
                                        <h3 class="card-text position-absolute bottom-0 end-0 m-2">${d.price} kr</h3>
                                    </div>
                                </a>
                            </div>`
                });
                $('.pizza-catalog').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
    $('#flexSwitchCheckDefault').change(function() {
        if (this.checked) {
            // send AJAX request for when checkbox is checked
            let order = 'name';
            let categoryId = $('.current').attr('id')
            $.ajax({
                url: '/order/pizzas?category_filter=' + categoryId + '&order_by=' + order,
                type: 'GET',
                success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 23%;height: 36rem">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image" style="height: 300px">
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">${d.description}</p>
                                        <h3 class="card-text position-absolute bottom-0 end-0 m-2">${d.price} kr</h3>
                                    </div>
                                </a>
                            </div>`
                });
                $('.pizza-catalog').html(newHtml.join(''));
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            });
        } else {
            // send AJAX request for when checkbox is not checked
            let order = 'price';
            let categoryId = $('.current').attr('id');
            $.ajax({
                url: '/order/pizzas?category_filter=' + categoryId + '&order_by=' + order,
                type: 'GET',
                success: function(resp){
                let newHtml = resp.data.map(d => {
                    return `<div class=" well card pizza" style="width: 23%;height: 36rem">
                                <a href="/order/pizzas/${d.id}" class="link-offset-2 link-underline link-underline-opacity-0">
                                    <img class="card-img-top" src="${d.firstImage}" alt="search image" style="height: 300px">
                                    <div class="card-body">
                                        <h4 class="card-title">${d.name}</h4>
                                        <p class="card-text">${d.description}</p>
                                        <h3 class="card-text position-absolute bottom-0 end-0 m-2">${d.price} kr</h3>                                    
                                    </div>
                                </a>
                            </div>`
                });
                $('.pizza-catalog').html(newHtml.join(''));
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            });
        }
    });
});

