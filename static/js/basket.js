window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        console.log(t_href.name); // basket.id
        console.log(t_href.value); // basket.quantity

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result)
            }
        })
    })

    $('.add_product_button').on('click', function () {
        var product_id = $(this).attr('id');
        console.log(product_id);

        $.ajax({
            url: '/baskets/add/' + product_id + '/',
        })
    })

    $(document.body).on('click', '.remove_basket_button', function () {
        var id = $(this).attr('id');
        console.log(id);

        $.ajax({
            url: '/baskets/remove/' + id + '/',
            success: function (data) {
                $('.basket_list').html(data.result)
            }
        })
        return false;
    })
}
