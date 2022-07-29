/*$(document).ready(function(){
	// códigos jQuery a serem executados quando a página carregar
    $.ajax({
        url: "",
        type: "get",
        contentType: "application/json",
        data: {
        intention: 'url',
        },
        success: function (url) {
            console.log('url fora: ', url);
            redirectUrl(url);
        }
    })

});
*/
function Redirect() {
    
    $.ajax({
        url: "",
        type: "get",
        contentType: "application/json",
        data: {
        intention: 'url',
        },
        success: function (url) {
            redirectUrl(url);
        }
    })
}

function redirectUrl(url) {
    
    window.location.href = url.res
}
