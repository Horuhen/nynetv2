$('.btnsend').on('click',function (url_page){
    $.ajax({
        url: url_page,
        type: 'POST',
        data: {},
        dataType: 'json'
    }).done(function (data){
        console.log(data);
    }).fail(function (jqXHR, textStatus,errorThrown){
        alert(textStatus+': '+errorThrown);
    }).always(function (data){

    });
});