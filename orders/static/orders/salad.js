document.addEventListener('DOMContentLoaded', () => {
    
    $.ajax({

        type:"POST",
        url: "/saladprice/" + salad_id,
        data: {
            csrfmiddlewaretoken: csrftoken, 
        },
        success: function(data) {
            document.querySelector('#price').innerHTML = data;
        },
    });

})