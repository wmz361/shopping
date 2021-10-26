function toindex(){
    // document.form1.action="./indexLogined.html";
    document.form1.submit();
}
function cancel(){
    document.form1.action="#";
    document.form1.submit();
}
function toRegister(){
    document.form1.action={{url_for('loginBP.register')}};
    document.form1.submit();
}
