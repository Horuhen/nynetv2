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
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "dni"},
            {"data": "address"},
            {"data": "email"},
            {"data": "amount_invoices"},
            {"data": "amount_invoices"},// no borrar este duplicado
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/nynet/customers/edit/' + row.id + '/" class="has-text-success"><i class="fa-solid fa-pen-to-square"></i>Edit</a>';
                    buttons += '<a href="/nynet/customers/delete/' + row.id + '/" class="has-text-danger"><i class="fa-solid fa-trash"></i>Delete</a>'
                    return buttons
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    })
});