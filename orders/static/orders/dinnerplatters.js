document.addEventListener('DOMContentLoaded', () => {

    getPrice();


    $('.platter-size').change(function() {
        getPrice();
    });

    // get the price of dinner platters
    function getPrice() {

        let dp_size = document.querySelector('#size').value;

        $.ajax({

            type:"POST",
            url: "/dinnerplatters/price/" + dp_id + "/" + dp_size,
            data: {
                csrfmiddlewaretoken: csrftoken, 
            },
            success: function(data) {
                document.querySelector('#price').innerHTML = data;
            },
            error: function () {
                document.querySelector('#price').innerHTML = "elected item not available";
            },
        });
    }

});