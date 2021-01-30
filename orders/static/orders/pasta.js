document.addEventListener('DOMContentLoaded', () => {
    
    $.ajax({

        type:"POST",
        url: "/pastaprice/" + pasta_id,
        data: {
            csrfmiddlewaretoken: csrftoken, 
        },
        success: function(data) {
            document.querySelector('#price').innerHTML = data;
        },
    });

})