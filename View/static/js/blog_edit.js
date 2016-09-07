/**
 * Created by yahui on 2016/9/5.
 */
$(document).ready(function () {




$("#eidt_blog_button").click(function () {

    var title= $("#blog_title").val();
    var content = $("#blog_content").val();
    var id=$("p.hidden").text();
    alert(id);
    if (title == ""){
        $("#edit_blog_message").text("标题不能为空");
        return;
    }
    $.ajax({
        url:"/v01/blog/"+id,
        type: "PUT",
        async: false,
        contentType: "application/json",
        data: JSON.stringify({
            title:title,
            content:content
        }),
        dataType: "html",
        success: function (data) {
            top.location.href="/v01/blog/"+id;
        },
        error: function (obj,info) {
            console.log(obj.message);
           $("#edit_blog_message").text(info);
        }
    });
});







});