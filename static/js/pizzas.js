$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('#search-bar').val();
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
        let categoryName = $(this).val();
        $.ajax({
            url: '/order/pizzas?category_filter=' + categoryName,
            type: 'GET',
            success: function(resp){
                console.log('button has been pressed')
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
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    })
});

