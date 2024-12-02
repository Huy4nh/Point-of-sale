$(document).ready(function(){
    $('#changePasswordBtn').click(function(){
        $.ajax({
            type: 'GET',
            url: '/load_password_form/',
            success: function(response){
                $('#content').html(response);
            }
        });
    });

    $('#changeUsernameBtn').click(function(){
        $.ajax({
            type: 'GET',
            url: '/load_username_form/',
            success: function(response){
                $('#content').html(response);
            }
        });
    });

    $(document).on('submit', '#changePasswordForm', function(e){
        e.preventDefault();
        var form = $(this);
        $.ajax({
            type: 'POST',
            url: '/change-password/',
            data: form.serialize(),
            success: function(response){
                $('#passwordMessage').html('<div class="alert alert-success">Password changed successfully!</div>');
            },
            error: function(response){
                $('#passwordMessage').html('<div class="alert alert-danger">Failed to change password.</div>');
            }
        });
    });

    $(document).on('submit', '#changeUsernameForm', function(e){
        e.preventDefault();
        var form = $(this);
        $.ajax({
            type: 'POST',
            url: '/change-username/',
            data: form.serialize(),
            success: function(response){
                $('#usernameMessage').html('<div class="alert alert-success">Username changed successfully!</div>');
            },
            error: function(response){
                $('#usernameMessage').html('<div class="alert alert-danger">Failed to change username.</div>');
            }
        });
    });
});