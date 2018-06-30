$(document).ready(function(){

            var form = $('#cnct-form');

            form.on('submit',function(e){
                e.preventDefault();

                //const formData = new FormData(this);

                $.ajax({
                    method:'POST',
                    url:'/add_contact/',
                    data: {
                        cnct_id:$('#usr_id').val(),
                        //chat_id:$('#chat_id').val(),
                        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                    },
                    success: function(result){
                        alert('Created new Contact');
                        //const chat = $('#chat');
                        //chat.append(result.renderedTemplate);
                        //form.find("input[type=text], textarea").val('');
                    }
                });

            });

        });