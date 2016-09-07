/**
 * Created by yahui on 2016/9/5.
 */

$( document ).ready(function () {
    $("#blog_delete_button").click(function () {
        var id = $("p.hidden").text();//
        $.ajax({
            url:"/v01/blog/"+id,
            type:"DELETE",
            async: false,
            success:function () {
                top.location.href="/v01/blogs";
            },
            error:function () {


            }
        })
    });


});
