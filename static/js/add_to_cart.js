let btn = document.querySelectorAll(".add_to_cart_btn button")

btn.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})

function addToCart(e){
    let product_id = e.target.value
    let url = "add_to_cart/"
    let data = {id:product_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(data)
    })
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
        })
        .catch(error=>{
            console.log(error)
        })
}