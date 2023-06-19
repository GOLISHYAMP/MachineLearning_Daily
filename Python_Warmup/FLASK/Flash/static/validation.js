var email = document.forms['form']['email'];
var password = document.forms['form']['password'];

var emailerror = document.getElementById('emailerror');
var passworderror = document.getElementById('passworderror');

function validated(){
    if(email.value.length < 9){
        email.style.border = "5px solid red";
        emailerror.style.display="block";
        email.focus();
        return false;
    }
}