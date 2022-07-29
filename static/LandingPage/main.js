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
