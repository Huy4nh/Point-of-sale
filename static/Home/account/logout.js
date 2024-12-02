$(document).ready(function(){
    $('#logout').click(function(event){
    $.ajax({
        url:'/logout/',
        type: 'POST',
        success:function(){
            window.location.href = '/';
        },
        error: function(xhr){
            alert('Đã xảy ra lỗi khi logout');
        }
    });
});


});