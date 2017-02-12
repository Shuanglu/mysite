$(document).ready(function(){
    $("#search").click(function(){
        var text = $("#search").val();
        window.location.href = "/shawn/Search/?text="+text;
    });

    $(".header").click(function(){
        var id = $("#id").val();
        window.location.href = "/shawn/Blog/"+id;
    });

});
