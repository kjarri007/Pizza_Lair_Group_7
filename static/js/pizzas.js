$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        let searchText = $('search-box').val();
        $.ajax({
            url: '/pizzas?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="well candy">
                                <a href="/pizzas/${d.id}">
                                    <img class="pizza-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                        </div>`
                });
                $('.pizzas').html(newHtml.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error){
                // TODO: Show toaster
                console.error(error);
            }
        })
    });
});