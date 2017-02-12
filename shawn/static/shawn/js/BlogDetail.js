$(document).ready(function(){
    $("#status").click(function(){

        var jsondata = {
            path:$("#path").val(),
            status:$(this).val(),
            /*csrfmiddlewaretoken: csrftoken,*/
        }
        $.ajax({
            type: "POST",
            url: "/shawn/Auth",
            data: {data:JSON.stringify(jsondata)},
            dataType: "json",
            success: function(result){
                alert("adsddsa");
            },
            error: function (data)
            {
                alert("5775");
            }
        });

    });
});
