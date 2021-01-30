document.addEventListener('DOMContentLoaded', () => {

    var cartItems = [];
    
    //localStorage.setItem("cart_items", cartItems);


    document.querySelectorAll('#place-order').forEach(button => {
    button.onclick = () => {

        var items = document.querySelector('.cart-items').innerHTML;
        cartItems.push(items.replace(/\n/g, ''));

        $.ajax({

            type:"POST",
            url: "/placeorder",
            data: {
                csrfmiddlewaretoken: csrftoken,
                'items' : cartItems,
            },
            /*success: function() {
                location.replace(homepage);
            },*/
        });
    }
    });

});