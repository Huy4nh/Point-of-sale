$(document).ready(function(event){
    $("#create_transaction").click(function(event){
        event.preventDefault();
        $.ajax({
            url:'/create_transaction/',
            method:'GET',
            success:function(data){
                $('#content').html(data);
                $.ajax({
                    url:'/show_item/',
                    type:'GET',
                    success:function(data){
                        let content=$('#your_cart').html()+data
                        $('#your_cart').html(content);
                    }
                });
                $('#tran_to_customer').click(function(e){
                    e.preventDefault();
                    $.ajax({
                        url:'/submit_transaction/',
                        type:'GET',
                        success:function(data){
                            $('#content').html(data);
                            $('#customer_phone_input').on('input',function(){
                                var phone_number = $(this).val();
                                if (phone_number.length >= 10){
                                    $.ajax({
                                        url:'/check_customer_phone/',
                                        type:'POST',
                                        data:{'phone': phone_number},
                                        datatype: 'json',
                                        success: function(data){
                                            $('#name').val(data.name);
                                            $('#address').val(data.address);
                                        }
                                    });
                                };
                            });

                            $(document).on('submit','#customer_input',function(e){
                                e.preventDefault();
                                var form= new FormData(this);
                                $.ajax({
                                    url:'/submit_transaction/',
                                    type:'POST',
                                    data:form,
                                    processData: false,
                                    contentType: false, 
                                    success:function(data){
                                        $('#purchasing_wait').click();
                                        alert('Vui lòng chờ thanh toán với nhân viên để hoàn thành giao dịch');
                                    }
                                });
                            });

                            $('#back_tran').click(function(event){
                                $("#create_transaction").click();
                            });
                        }

                    });
                });
            },
            error: function(){
                $('#content').html('Error in load account form');
            }
        });
    });

    $(document).on('submit', '#transaction_form', function(e){
        e.preventDefault();
        var formdata=new FormData(this);
        $.ajax({
            url:'/create_transaction/',
            type:'POST',
            data:formdata,
            processData: false,
            contentType: false, 
            success:function(data){
                $.ajax({
                    url:'/show_item/',
                    type:'GET',
                    success:function(data){
                        $('#your_cart').html(data);
                    }
                });
            },
            error:function(){
                alert('This product not exist in system: \n"Please add it by click "thêm sản phẩm" then provide need info"');
            }
        })
    });

});