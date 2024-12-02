$(document).ready(function(){
    $('#view_accounts').click(function(event){
        event.preventDefault();
        loadProducts();
        function loadProducts(){
            $.ajax({
                url: '/accounts/',
                method: 'GET',
                success: function(data){
                    let content = '';
                    let group = 'Staff'
                    data.forEach(function(account){
                        if (account.is_admin == true){
                            let group ='Admin';
                        };
                        content += '<div class="col-sm-12 col-md-12 col-lg-6 col-xl-3" >'+
                                    '<div id=product-'+account.staff_id+' class="card" style="padding:20px;width: 18rem; height: 30rem;">'+
                                    '<div style="height: 250px;width: 250px;">'+
                                    '<img class="card-img-top" src="'+account.avatar+'" alt="'+account.username+'" style="max-height: 250px;max-width: 250px;">'+
                                    '</div>'+
                                    '<div class="card-body">'+
                                    '<h5 class="card-text">'+account.username+'</h4>'+
                                    '<p class="card-text">-Gmail: '+account.gmail+'</p>'+
                                    '<p class="card-text">-Chức vụ: '+group+'</p>'+
                                    '</div>'+
                                    '<div>'+
                                    '<p><button  class="delete_account" value="'+account.staff_id+'" style="padding-right:20px">DELETE</button> <button onlick="viewDetail('+account.staff_id+')">DETAIL</button></p>'+
                                    '</div>'+
                                    '</div>'+
                                    '</div>'
                            });
                        console.log(content);
                        $('#content').html(content);
                        $('.delete_account').click(function(staff_id){
                            staff_id=$('.delete_account').val();
                            urlne='/delete-account/0/'.replace('0',staff_id);
                            
                            fetch(urlne,{
                                method: 'POST',
                    
                            })
                            .then(response =>response.json())
                            .then(data=>{
                                
                            })
                            $('#view_accounts').click()
                        });
            },
        });
    };
    });
});

