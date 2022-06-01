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
            {"data": "name"},
            {"data": "description"},
            {"data": "image"},
            {"data": "value"},
            {"data": "value"},// no borrar este duplicado
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/nynet/products/edit/' + row.id + '/" class="has-text-success"><i class="fa-solid fa-pen-to-square"></i>Edit</a>';
                    buttons += '<a href="/nynet/products/delete/' + row.id + '/" class="has-text-danger"><i class="fa-solid fa-trash"></i>Delete</a>'
                    return buttons
                }
            },
            {
                targets: [-3],
                class: 'text-center',
                render: function (data, type, row) {
                    return '<td>\n' +
                        '                <figure class="image is-24x24">\n' +
                        '                    <img src="' + row.image + '" alt="Image"/>\n' +
                        '                </figure>\n' +
                        '            </td>'
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                render: function (data, type, row) {

                    return '<td>$   '+ Humanize.intcomma(row.value) +' </td>';
                }
            },
            {
                targets: [2],
                class: 'text-center',
                render: function (data, type, row) {

                    return '<td>'+ Humanize.truncate(row.description, 50) +' </td>';
                }
            },
            
        ],
        initComplete: function (settings, json) {

        }
    })
});
