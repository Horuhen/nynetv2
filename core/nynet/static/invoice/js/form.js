var vents = {
    items: {
        employee: '',
        customer: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        date_joined: '',
        products: [],
    }
};

$(function () {
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            console.log(ui.item);
        }
    });
})