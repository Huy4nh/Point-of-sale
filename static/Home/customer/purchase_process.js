$(document).ready(function(){
    $('#purchasing_wait').click(function(event){
        $.ajax({
            url:'/purchase_wait/',
            method:'GET',
            success:function(data){
                $('#content').html(data);
                $('.purchase').click(function(event){
                    var phone_number=$('.purchase').val();
                    $.ajax({
                        url:'/purchase_wait/',
                        type:'POST',
                        data:{'phone_number':phone_number},
                        success:function(data){
                            $('#purchasing_wait').click();
                        },
                        error: function(){
                            $('#content').html('Error in load account form');
                        }
                    });
                });
            },
            error: function(){
                $('#content').html('Error in load account form');
            }
        });
    });
});