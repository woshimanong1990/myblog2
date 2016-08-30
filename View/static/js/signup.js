/**
 * Created by yahui on 2016/8/30.
 */
$( document ).ready(function() {
    var empty_flag = false;
    var exist_flag = false;
    var code_flag = false;
    $(".require").focusin(function () {
        var tag_id = $(this).attr("id");
        var change_tag = "#error_" + tag_id;
        $(change_tag).text("*");
    })

    $(".require").focusout(function () {
        var text_v = $(this).val();
        if (text_v == undefined || text_v == "" || text_v == null) {
            var tag_id = $(this).attr("id");
            var error_name = "";
            switch (tag_id) {
                case "user_name":
                    error_name = "用户名";
                    break;
                case "password":
                    error_name = "密码";
                    break;
                case "check_passwd":
                    error_name = "确认密码";
                    break;
                case "email":
                    error_name = "邮箱";
                    break;
                case "check_code":
                    error_name = "验证码";
                    break;

            }
            var change_tag = "error_" + tag_id;
            var change_element = "#" + change_tag;
            // alert(change_element);
            $(change_element).text(error_name + "不能为空");
            empty_flag = false;
            return
        } else {
            empty_flag = true
        }
    });
    $(".check_exit").focusout(function () {
        var tar_name = $(this).attr("name");
        var vale_name = $(this).val();
        if (vale_name == "") {
            exist_flag = false;
            return
        }
        var params = {};
        params[tar_name] = vale_name;
        params["_xsrf"] = getCookie("_xsrf");
        $.ajax({
            type: "POST",
            async: false,
            contentType: "application/json",
            url: "/v01/check_user",
            data: JSON.stringify(params),
            dataType: "json",
            success: function (data) {
                exist_flag = false;
                // alert('success');
                var error_name = "";
                switch (tar_name) {
                    case "user_name":
                        error_name = "用户名";
                        break;
                    case "phone":
                        error_name = "手机号";
                        break;
                    case "email":
                        error_name = "邮箱";
                        break;
                }
                $("#error_" + tar_name).text(error_name + "已存在，请更换别的" + error_name);

            },


            error: function (obj, error_info) {
                // alert('error');
                exist_flag = true;

            },
        });
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
                //alert("checke_code_success");
                code_flag = true;
            },
            error: function (obj, error_info) {
                code_flag= false;
                $("#error_check_code").text("验证码错误");
            }

});

});

$("#check_code_button").click(function () {
    var timestamp = new Date().getTime();
    $("#check_code_imag").attr("src",$("#check_code_imag").attr('src') + '?' +timestamp );
});













 $("#submit").click(function () {
     // alert("df");
     var pasw1= $("#password").val();
     var pasw2= $("#check_passwd").val();
     if (pasw1 != pasw2){
         $(".error_message_all").text("两次密码不一致");
     }
        alert(""+empty_flag +exist_flag +code_flag);
        if (empty_flag && exist_flag && code_flag) {

            //$("#form").attr("action","/v01/users");
            //$("#form").attr("method","post");
            $("#form").submit();
        }
        if(!empty_flag){
            $(".require").each(function () {
                var error_ele="";
                switch ($(this).attr("name")){
                    case "user_name":
                    error_ele = "用户名";
                    break;
                case "password":
                    error_ele = "密码";
                    break;
                case "check_passwd":
                    error_ele = "确认密码";
                    break;
                case "email":
                    error_ele = "邮箱";
                    break;
                case "check_code":
                    error_ele = "验证码";
                    break;

                }
                if($(this).val() == ""){
                    $("#error_"+$(this).attr("name")).text("请输入"+error_ele)
                }
            });
            }
    });












    });
function getCookie(name) {
    var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return c ? c[1] : undefined;
}