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
            {"data": "customer"},// no borrar este duplicado
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/nynet/invoices/edit/' + row.id + '/" class="has-text-success"><i class="fa-solid fa-pen-to-square"></i>Edit</a>';
                    buttons += '<a href="/nynet/invoices/delete/' + row.id + '/" class="has-text-danger"><i class="fa-solid fa-trash"></i>Delete</a>'
                    return buttons
                }
            }
        ],
        initComplete: function (settings, json) {

        }
    })
});
