$(document).ready(function(){

            var form = $('#message-form');

            form.on('submit',function(e){
                e.preventDefault();

                //const formData = new FormData(this);

                $.ajax({
                    method:'POST',
                    url:'/chat/message_create/',
                    data: {
                        text:$('#text').val(),
                        chat_id:$('#chat_id').val(),
                        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()

                    },
                    success: function(result){
                        //alert('Created new message');
                        const chat = $('#chat');
                        chat.append(result.renderedTemplate);
                        form.find("input[type=text], textarea").val('');
                    }
                });

            });

        });

