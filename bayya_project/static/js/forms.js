let firstName = $('#id_first_name')
let lastName = $('#id_last_name')
let email = $('#id_email')
let password1 = $('#id_password1')
let password2 = $('#id_password2')
let country = $('#id_country')
let submit = $('#submit')
let phoneNumber = $('phone_name')
let referers_email = $('referers_email')
let bitcoin_add_or_bank_acct = $('bitcoin_add_or_bank_acct')
let bank_name = $('bank_name')


submit.click(function(){
    
    if (firstName.val() == "" || lastName.val() == "" || email.val() == "" || 
    password1.val() == "" || password2.val() == "" || country.val() == "" || 
    bank_name.val() || phoneNumber.val() || referers_email.val() || 
    bitcoin_add_or_bank_acct.val()){
        Swal.fire({
            title: 'FIELDS EMPTY!!',
            text: 'Please check the missing field!!',
            icon: 'warning',
            confirmButtonText: 'OK'
        });
    }
});

myForm.submit(function(e){
    if(password1.val() !== password2.val()){
        e.preventDefault();
        Swal.fire({
            title: "PASSWORDS DON'T MATCH!!",
            text: 'Please check your password and try again!!',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }

});

submit.click(function(e){
    e.preventDefault()
    let emailaddr = email.val();
    $.ajax({
        url:'/ajax/validate_email',
        method: 'POST',
        data:{
            "email": emailaddr,
        },
        datatype:'json',
        success:function(data){
            if(data.is_taken){
                Swal.fire({
                    title: "USER EXISTS!!",
                    text: 'A User with that email already exists!',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        }

    });
});