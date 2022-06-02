
$(function () {
    $('#table').DataTable({
        responsive: true,
        destroy: true,
        deferRender: true,

        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata',
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "list_of_products"},
            {"data": "employee"},
            {"data": "customer"},
            {"data": "date_joined"},
            {"data": "subtotal"},
            {"data": "iva"},
            {"data": "total"},
            {"data": "total"},// no borrar este duplicado
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<a href="/nynet/invoices/delete/' + row.id + '/" class="has-text-danger"><i class="fa-solid fa-trash"></i>Delete</a>'
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    })
});
