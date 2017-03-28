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
      $("#fileway1").change(function(){
      getFileName();
      });
      $("#fileway2").change(function(){
      getFileName2();
      });
      $("#fileway3").change(function(){
      getFileName3();
      });
      $("#fileway4").change(function(){
      getFileName4();
      });
      $("#fileway5").change(function(){
      getFileName5();
      });
      $("#fileway6").change(function(){
      getFileName6();
      });
      $("#fileway7").change(function(){
      getFileName7();
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
      $("#tasksAuthLogin").click(function(){
        //alert("BombardaMaxia");
        $("#parent_popup").css('display','block');
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

function getFileName () {

var file = document.getElementById('fileway1').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName1').innerHTML = 'Имя файла: ' + file;

}

function getFileName2 () {

var file = document.getElementById('fileway2').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName2').innerHTML = 'Имя файла: ' + file;

}

function getFileName3 () {

var file = document.getElementById('fileway3').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName3').innerHTML = 'Имя файла: ' + file;

}

function getFileName4 () {

var file = document.getElementById('fileway4').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName4').innerHTML = 'Имя файла: ' + file;

}

function getFileName5 () {

var file = document.getElementById('fileway5').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName5').innerHTML = 'Имя файла: ' + file;

}

function getFileName6 () {

var file = document.getElementById('fileway6').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName6').innerHTML = 'Имя файла: ' + file;

}

function getFileName7 () {

var file = document.getElementById('fileway7').value;

//file = file.replace(/\\/g, «/»).split('/').pop();

document.getElementById ('fileName7').innerHTML = 'Имя файла: ' + file;

}