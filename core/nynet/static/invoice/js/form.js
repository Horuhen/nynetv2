var tblProducts;
var vents = {
    items: {
        employee: '',
        customer: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        date_joined: '',
        products: [],
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.amount * parseFloat(dict.price);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;
        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));

    },
    add: function (item) {
        this.items.products.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        tblProducts = $('#table').DataTable({
            responsive: true,
            destroy: true,
            data: this.items.products,
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "price"},
                {"data": "amount"},
                {"data": "subtotal"},// no borrar este duplicado
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a href="#" rel="remove" class="has-text-danger"><i class="fa-solid fa-trash"></i>Delete</a>'

                    }
                },
                {
                    targets: [2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$   ' + Humanize.intcomma(data);

                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<input type="number" name="amount" class="input is-small" autocomplete="off" value="' + data + '">'

                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$ ' + Humanize.intcomma(data);

                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        })
    },
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
            event.preventDefault();
            console.clear()
            ui.item.amount = 1;
            ui.item.subtotal = 0.00;
            vents.add(ui.item);
            console.log(vents.items);
            $(this).val('')
        }
    });
    $('input[name="iva"]').change(function () {
        vents.calculate_invoice();
    });
    $('.btnRemoveAll').on('click', function () {

        alert_action('Notification', 'Are you sure of delete all items?', function () {
            vents.items.products = [];
            vents.list();
        })

    });
    $('#table tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products.splice(tr.row, 1);
            vents.list();
        })
        .on('change keyup', 'input[name="amount"]', function () {
            console.clear()
            var amount = parseInt($(this).val())
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            vents.items.products[tr.row].amount = amount;
            vents.calculate_invoice()
            $('td:eq(4)', tblProducts.row(tr.row).node()).html('$ ' + Humanize.intcomma(vents.items.products[tr.row].subtotal));

        });


})