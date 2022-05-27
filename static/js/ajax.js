$('.form').on('submit',function (e){
    e.preventDefault();
    var parameters = $(this).serializeArray();

    $.ajax({
        url: '{{ create_url }}',
        type: 'POST',
        data: parameters,
        dataType: 'json'
    }).done(function (data){
        if(!data.hasOwnProperty('error')){
            location.href = '{{ list_url}}';
            return false;
        }
        message_error(data)
    }).fail(function (jqXHR, textStatus,errorThrown){
        alert(textStatus+': '+errorThrown);
    }).always(function (data){

    });
});