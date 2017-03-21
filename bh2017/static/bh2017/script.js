 $(document).ready(function() {

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

var csrftoken = getCookie('csrftoken');

    $( "input" ).prop('required',true);
    $("form").submit(function(e) {

    var ref = $(this).find("[required]");

    $(ref).each(function(){
        if ( $(this).val() == '' )
        {
            alert("Все поля должны быть заполнены!");

            $(this).focus();

            e.preventDefault();
            return false;
        }
    });  return true;
    });
    $( "#id_email" ).change(function() {
        //alert( "Handler for .click() called." );
        var email = $("#id_email").val();
        //alert(email);
        $.post(
              "/mailCheck/",
          {
                'email': email,
          },
            onAjaxSuccess
                );
     });
     $("#loginWrap").click(function(){
        //alert("BombardaMaxia");
        $("#parent_popup").css('display','block');
     });
     $( "#id_passwordCheck" ).change(function() {
        //alert( "Handler for .click() called." );
        var A = $("#id_passwordCheck").val();
        var B = $("#id_password").val();
        if (A == B){
            $( "#registrationButton" ).prop('disabled',false);
            $( "#registrationButton" ).animate({
                 width: "150px"
             }, 50, function(){
            $( "#registrationButton" ).attr('value','РЕГИСТРАЦИЯ');
        });
        }
        else {
            $( "#registrationButton" ).prop('disabled',true);
            $( "#registrationButton" ).animate({
                width: "236px"
                }, 50, function(){
            $( "#registrationButton" ).attr('value','Пароль и проверка пароля должны совпадать');
                });
        }
      });
      $("#nextButton").click(function( event ) {
        event.preventDefault();
        var link = $("#nextButton").attr('href');

        jQuery.ajax({
                'type': 'POST',
                'url': '/loadmorepartner/'+link,
                'data': {},
                'success': function(data){
                            var arr = data.split('///');
                            $("#partnerList").append(arr[0]);
                            $("#nextButton").attr('href',arr[1]);
                            if (arr[1]=='Last')
                            {
                            $("#nextButton").hide();
                            }
                    }
                });
            });
});




function onAjaxSuccess(data)
{
  // Здесь мы получаем данные, отправленные сервером и выводим их на экран.
  //alert(data);
  if (data == 'False'){
    $( "#registrationButton" ).prop('disabled',true);
    $( "#registrationButton" ).animate({
        width: "300px"
    }, 50, function(){
    $( "#registrationButton" ).attr('value','Этот почтовый ящик уже занят');
    });
    }
  else {
    $( "#registrationButton" ).prop('disabled',false);
    $( "#registrationButton" ).animate({
        width: "150px"
    }, 50, function(){
    $( "#registrationButton" ).attr('value','РЕГИСТРАЦИЯ');
    });
  }
}
function loadingpartner(data)
{
    alert('Bang');
    alert(data);
    $("#partnerList").append(data);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}