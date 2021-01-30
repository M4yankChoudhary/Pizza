document.addEventListener('DOMContentLoaded', () => {

    getPrice();

    var items = [];

    $('.sub-size').change(function() {
        items = [];
        localStorage.setItem("addOnList", items);
        document.querySelector('#selected-add-ons').value = localStorage.getItem("addOnList");
        getPrice();
    });

    document.querySelectorAll('#add-item').forEach(button => {
        button.onclick = () => {

            var get_item = document.querySelector('#addon').value;
            var price = document.querySelector('#price').innerHTML;
            let total = parseFloat(get_item) + parseFloat(price);

            if(isNaN(price)) {
                location.reload();
            }

            var selectedAddOn = document.querySelector('#addon');
            var addOnName = selectedAddOn.options[selectedAddOn.selectedIndex].dataset.name;

            if(!isNaN(parseFloat(get_item))) {
                document.querySelector('#price').innerHTML = total.toFixed(2);
                items.push(addOnName);
                localStorage.setItem("addOnList", items);
                document.querySelector('#selected-add-ons').value = localStorage.getItem("addOnList");
            } else {
                alert("Please select from the list of Add-Ons.");
            }
        };
    
    });

    document.querySelector('#submit').onclick = () => {

        var size = document.querySelector('#size').value;

        $.ajax({

            type:"POST",
            url: "/subshandler/" + sub_id + "/" + size,
            data: {
                csrfmiddlewaretoken: csrftoken,
                'items' : items,
            },
            success : () => {
                location.reload();
            },
            error: function () {
                alert("Invalid Selections");
                location.replace(homepage);
            },
        });

    };


    // get the price of sub
    function getPrice() {

        let sub_size = document.querySelector('#size').value;

        $.ajax({

            type:"POST",
            url: "/subsprice/" + sub_id + "/" + sub_size,
            data: {
                csrfmiddlewaretoken: csrftoken, 
            },
            success: function(data) {
                document.querySelector('#price').innerHTML = data;
            },
            error: function () {
                document.querySelector('#price').innerHTML = "elected Size is not available";
            },
        });
    }

});