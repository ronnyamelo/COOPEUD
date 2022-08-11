const sendLoanRequestBtn = document.getElementById("sendLoanRequest");


sendLoanRequestBtn.addEventListener('click', function(event) {
    event.preventDefault();
    alert("text: " + sendLoanRequestBtn.innerText);
})
