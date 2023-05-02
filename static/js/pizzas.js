$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('#search-bar').val();
        $.ajax({
            url: '/order/pizzas?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="well pizza">
                                <a href="/order/pizzas/${d.id}">
                                    <img class="card-img-top" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
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
});