
$(document).ready(function(){
    //alert("adadadadsa");
    var path = $("#path").val();
    var id = $("#id").val();
    //alert(id);
    $.ajax({
        type:"GET",
        url: path+"/comment",
        data: {"id":id},
        cache: false,
        dataType:"json",
        success: function(data){
            //alert("11");
            $.each(data, function(index,comment){
                $("#comments").append("<p>"+comment+"</p>");
                //alert("dadsds");
            });
        },
        error: function(data){
            alert("2");
        },
    });

    //alert("adadadadsa");
    $("#login1,#login2,#signup1,#signup2,#logout").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
    $("#reply").click(function(){
        //alert($("#path").val());
        $.ajax({
            type: "post",
            url: $("#path").val()+"/comment",
            data: {"text": $("#text").val()},
            dataType:"json",
            cache: false,
            success: function(data){
                //alert("0");
                $("#comments").empty();
                //alert("1");
                $.each(data, function(index,comment){
                    $("#comments").append("<p>"+comment+"</p>");
                    //alert("dadsds");
                });
            },
            error: function(data){
                alert("2");
            },
        });
    })
});
