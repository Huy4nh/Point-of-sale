$(document).ready(function(){
    $('#view_products').click(function(event){
        event.preventDefault();
        loadProducts();
        function loadProducts(){
            $.ajax({
                url: '/products/',
                method: 'GET',
                success: function(data){
                    let content = '';
                    data.forEach(function(product){
                        content += '<div class="col-sm-12 col-md-12 col-lg-6 col-xl-3" >'+
                                    '<div id=product-'+product.barcode+' class="card" style="padding:20px;width: 18rem; height: 30rem;">'+
                                    '<div style="height: 250px;width: 250px;">'+
                                    '<img class="card-img-top" src="'+product.product_image+'" alt="'+product.product_name+'" style="max-height: 250px;max-width: 250px;">'+
                                    '</div>'+
                                    '<div class="card-body">'+
                                    '<h5 class="card-text">'+product.product_name+'</h4>'+
                                    '<h6 class="card-text">-Import price: '+product.import_price+'</h6>'+
                                    '<h6 class="card-text">-Retail price: '+product.retail_price+'</h6>'+
                                    '</div>'+
                                    '<div>'+
                                    '<p><button type="button"  class="delete-button" value="'+product.barcode+'" style="padding-right:20px">DELETE</button> <button onlick="viewDetail('+product.barcode+')">DETAIL</button></p>'+
                                    '</div>'+
                                    '</div>'+
                                    '</div>'
                            });
                        $('#content').html(content);
                        $('.delete-button').click(function(){
                            barcode=$(this).val();
                            urlne='/delete-product/0/'.replace('0',barcode);
                            $.ajax({
                                url:urlne,
                                method:'POST',
                                data:barcode,
                                success: function(data){
                                    alert('qweiqweiui');
                                    $('#view_products').click();
                                }
                            });
                        });
            },
        });
    };
    });
});

