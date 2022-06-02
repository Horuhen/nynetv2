function message_error(obj) {
    var html = ''
    if (typeof (obj) === 'object') {

        html += '<ul style="text-align: left">'
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html += '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'ERROR',
        html: html,
        icon: 'error'
    });
}

function ajax_with_confirm(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa-solid fa-info',
        content: content,
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'button',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Yes',
                btnClass: 'button is-primary',
                action: function () {
                    $.ajax({
                        url: url,// window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: 'No',
                btnClass: 'button is-danger',
                action: function () {

                }
            }
        }

    })
}

function alert_action(title, content, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa-solid fa-info',
        content: content,
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'button',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Yes',
                btnClass: 'button is-primary',
                action: function () {
                    callback();
                }
            },
            danger: {
                text: 'No',
                btnClass: 'button is-danger',
                action: function () {

                }
            }
        }

    })
}