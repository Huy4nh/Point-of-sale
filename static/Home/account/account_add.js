$(document).ready(function(){
    $('#add_account_link').click(function(event){
        event.preventDefault();
        $.ajax({
            url:'/add_account/',
            method:'GET',
            success:function(data){
                $('#content').html(data);
            },
            error: function(){
                $('#content').html('Error in load account form');
            }
        });
    });

    $(document).on('submit', '#account_form', function(event){
        event.preventDefault();
        var formData = new FormData(this);
        alert('wait for active');
        $.ajax({
            url:'/add_account/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                alert('Đăng ký thành công chờ tài khoản được kích hoạt vui lòng kích hoạt trong 1 phút')
                $('#account_form')[0].reset();
            },
            error: function(xhr){
                let errors= xhr.responseJSON.errors;
                let errorMessages = '';
                for (let field in errors){
                    errorMessages+= errors[field].join(', ') +'\n';
                }
                alert(errorMessages);
            }

        });
    });
});