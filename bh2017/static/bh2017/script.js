 $(document).ready(function() {
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


});



function onAjaxSuccess(data)
{
  // Здесь мы получаем данные, отправленные сервером и выводим их на экран.
  //alert(data);
  if (data == 'False'){
    $( "input[type|='submit']" ).prop('disabled',true);
    $( "input[type|='submit']" ).animate({
        width: "236px"
    }, 50, function(){
    $( "input[type|='submit']" ).attr('value','Этот почтовый ящик уже занят');
    });
    }
  else {
    $( "input[type|='submit']" ).prop('disabled',false);
    $( "input[type|='submit']" ).animate({
        width: "150px"
    }, 50, function(){
    $( "input[type|='submit']" ).attr('value','РЕГИСТРАЦИЯ');
    });
  }
}
