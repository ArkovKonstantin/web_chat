$(document).ready(function() {
// Тут пишем код
	var input = $('input[name=q]');
	input.on('keyup', function(e) {
		//console.log(e.target.value);
		//alert('успех')
		$.ajax({
            type: 'POST',
            url: '/search/', //Путь к обработчику
            data: {
				query:$('#id_q').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
			},
            //response: 'text',
            success: function(result){
                const ulist = $('#usr_list');
                // отчистить
                ulist.empty();
                ulist.append(result.renderedTemplate);
                //console.log(result);
           }
       });
	});

});
