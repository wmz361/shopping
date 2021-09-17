function toindex(){
    // document.form1.action="./indexLogined1.html";
    document.form1.submit();
}
function cancel(){
    document.form1.action="#";
    document.form1.submit();
}
function toRegister(){
    document.form1.action={{url_for('webBP.register')}};
    document.form1.submit();
}
