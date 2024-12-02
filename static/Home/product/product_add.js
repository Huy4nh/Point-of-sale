$(document).ready(function(){
    $('#add_product_link').click(function(event){
        event.preventDefault();
        $.ajax({
            url: '/add_product/',
            method: 'GET',
            success: function(data) {
                $('#content').html(data);
            },
            error: function(){
                $('#content').html('<p>Error loading form.</p>');
            }
        });
    });

    $(document).on('submit', '#product_form', function(event){
        event.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: '/add_product/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                alert(formData)
                alert('success')
                $('#product_form')[0].reset();
            },
            error: function(xhr) {
                let errors = xhr.responseJSON.errors;
                let errorMessages = '';
                for (let field in errors) {
                    errorMessages += errors[field].join(', ') + '\n';
                }
                alert(errorMessages);
            }
        });
    });
});