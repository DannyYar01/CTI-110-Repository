"use strict";
var $ = function(id) { return document.getElementById(id); };

var saveRegistration = function() {
    sessionStorage.date = $("date").value;

    sessionStorage.customerType = $("business").value;
    if ($("personal").checked) {
        sessionStorage.customerType = $("personal").value;
    }
    if ($("government").checked) {
        sessionStorage.customerType = $("government").value;
    }

    sessionStorage.paymentType = $("po").value;
    if ($("cash").checked) {
        sessionStorage.paymentType = $("cash").value;
    }
    if ($("credit").checked) {
        sessionStorage.paymentType = $("credit").value;
    } 

    sessionStorage.emailAddress = $("email_address").value;
    sessionStorage.firstName = $("first_name").value;
    sessionStorage.lastName = $("last_name").value;
    sessionStorage.phone = $("phone").value;
    sessionStorage.stateCode = $("state_code").value;
    sessionStorage.zipCode = $("zip_code").value;

    // submit form
    $("confirmation_form").submit();
};

window.onload = function() {
    $("submit_request").onclick = saveRegistration;
};