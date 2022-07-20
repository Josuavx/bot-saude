document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("input");
    inputField.addEventListener("keydown", (e) => {
        if (e.code === "Enter") {
            let input = inputField.value;
            inputField.value = "";
            
            $.ajax({
                url: '',
                type: 'get',
                contentType: 'application/json',
                data: {
                    input_text: input //$(this).text()
                },
                success: function(response){
                    $('.messages').text(response.res)
                }
            })

        }
    });
});




/*
$(document).ready(function () {

    jQuery('#input').keypress(function(event){

        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
            alert('You pressed a "enter" key in textbox');
            
            result = event
            console.log(event)

            $.ajax({
                url: '',
                type: 'get',
                contentType: 'application/json',
                data: {
                    input_text: 'Ok' //$(this).text()
                },
                success: function(response){
                    $('.messages').text(response.nome)
                }
            })
        }
    
    });

*/

/*
$('.btn').click(function() {
    $.ajax({
        url: '',
        type: 'get',
        contentType: 'application/json',
        data: {
            button_text: $(this).text()
        },
        success: function(response){
            $('.btn').text(response.nome)
        }
    })

})





})
*/