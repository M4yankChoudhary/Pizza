document.addEventListener('DOMContentLoaded', () => {

    var items = [];

    $('.pizza-values').change(function(){

        var selectedTopping = document.querySelector('#topping');
        var number = selectedTopping.options[selectedTopping.selectedIndex].dataset.number;
        const topping_section = document.querySelector('.topping-section');
        topping_section.setAttribute("hidden", true);
        
        document.querySelector('#user-toppings').value = "";
        items = [];

        if (parseInt(number) >= 1) {
            
            document.querySelector('#user-toppings').value = "";
            const topping_section = document.querySelector('.topping-section');
            topping_section.removeAttribute("hidden");
        
        }

        var pizza_size = document.querySelector('#size').value;
        var pizza_topping = document.querySelector('#topping').value;
        
    
    $.ajax({

        type:"POST",
        url : "/price/" + pizza_id  +  "/" + pizza_size + "/" + pizza_topping,

        data: {
            csrfmiddlewaretoken: csrftoken,
        },

        success: function(data) {
            document.querySelector('#price').innerHTML = data;
        }

    });  
    });

    document.querySelectorAll('#add').forEach(button => {
        button.onclick = () => {

            var selectedTopping = document.querySelector('#topping');
            var number = selectedTopping.options[selectedTopping.selectedIndex].dataset.number;
            
            var getvalue = document.querySelector(".addtopping").value;

            if(number > 0) {

                if(items.length < parseInt(number)) {
                    items.push(getvalue);
                    localStorage.setItem("number-toppings", items);
                    document.querySelector('#user-toppings').value = localStorage.getItem("number-toppings");
                } else {
                    alert("max toppings");
                }   
            }
        };
    
    });
});
