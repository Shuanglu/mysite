$(document).ready(function(){
    $("#login1").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
    $("#login2").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
    $("#signup1").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
    $("#signup2").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
    $("#logout").click(function(){
        var status = $(this).val();
        var path = $("#path").val();
        window.location.href = "/shawn/Auth/?status="+status+"&path="+path;
    });
});
