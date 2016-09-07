/**
 * Created by yahui on 2016/8/31.
 */
$( document ).ready(function () {
    var check_code_flag = false;
    $(".require").focusout(function () {
        var id_text = $(this).attr("id");
        var lable_tag ="#"+id_text+"_label";
        if ($(this).val()==""){
           $(lable_tag).text("不能为空");
        }
    });
    $("#check_code").focusout(function () {
        var check_code_val = $("#check_code").val();

   $.ajax({
            type: "POST",
            async: false,
            contentType: "application/json",
            url: "/v01/check_code",
            data: JSON.stringify({
            check_code:check_code_val
            }),
            dataType: "json",
            success: function (data) {
                check_code_flag=true;
            },
            error: function (obj, error_info) {
                code_flag= false;
                $("#error_check_code").text("验证码错误");
            }

});
    });



    $("#login").click(function () {
        $(".require").each(function () {
             var id_text = $(this).attr("id");
             var lable_tag = id_text+"_label";
            if ($(this).val()==""){
                $(lable_tag).text("不能为空");
            }
        });
        var user_name=$("#username").val();
        var passwd = $("#userpwd").val();
        var check_code = $("#check_code").val();


        if (check_code_flag){
            $.ajax({
            type: "POST",
            async: false,
            contentType: "application/json",
            url: "/v01/login",
            data: JSON.stringify({
                user_name:user_name,
                password:passwd,
                check_code:check_code
            }),
            dataType: "html",
            success: function (data) {
                top.location.href="/v01/home";
            },
            error: function (obj,info) {
                console.log(obj.message);
               $("#error_all").text(info);
            }

});





        }



    });

    $("#signup").click(function () {
        top.location.href="/v01/signup";
    });

$("#reload_check_code").click(function () {
    var timestamp = new Date().getTime();
    $("#check_code_imag").attr("src",$("#check_code_imag").attr('src') + '?' +timestamp );
});































});
