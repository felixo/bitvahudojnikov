 $(document).ready(function() {
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
