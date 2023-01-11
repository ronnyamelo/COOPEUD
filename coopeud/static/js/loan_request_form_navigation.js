const firstSectionItems = document.getElementsByClassName('form-first-section');
const secondSectionItems = document.getElementsByClassName('form-second-section');
const finalSectionItems = document.getElementsByClassName('form-final-section');

const backToFirstSectionBtn = document.getElementById('backToFirstSection');
const backToSecondSectionBtn = document.getElementById('backToSecondSection');
const toSecondSectionBtn = document.getElementById('toSecondSection');
const toFinalSectionBtn = document.getElementById('toFinalSection');
const sendLoanRequestBtn = document.getElementById('sendLoanRequest')

const personalDataForm = document.forms['personalDataForm'];
const employmentDataForm = document.forms['employmentDataForm'];
const loanDataForm = document.forms['loanDataForm'];

const successMsg = document.getElementById('success');
const requestContainer = document.getElementById('requestContainer');
// requestContainer.hidden = true;

toSecondSectionBtn.addEventListener('click', function (event) {
    if (!isValidForm(personalDataForm)) {
        return;
    }

    hideElements(firstSectionItems);
    showElements(secondSectionItems);
    scrollTo(position.top)
    event.preventDefault()
});

toFinalSectionBtn.addEventListener('click', function (event) {
    if (!isValidForm(employmentDataForm)) {
        return;
    }

    hideElements(secondSectionItems);
    showElements(finalSectionItems);
    scrollTo(position.top);
})

sendLoanRequestBtn.addEventListener('click', function (event) {
    if (!isValidForm(personalDataForm) || 
        !isValidForm(employmentDataForm) || 
        !isValidForm(loanDataForm)) {
            return;
    }

    let request = {
        "loan_type": loanDataForm['loanType'].value,
        "amount_requested": loanDataForm['requestedAmount'].value,
        "term": loanDataForm['loanTerm'].value,
        "referer": loanDataForm['referrer'].value.trim() || null,
        "status": "VALIDANDO",
        "applicant": {
            "first_name": personalDataForm['firstName'].value,
            "last_name": personalDataForm['lastName'].value,
            "id_number": personalDataForm['idNumber'].value,
            "id_type": personalDataForm['idType'].value,
            "nationality": personalDataForm['nationality'].value,
            "birth_date": personalDataForm['dateOfBirth'].value,
            "tel": personalDataForm['telephone'].value.replace(/-/g,'') || null,
            "celphone": personalDataForm['celphone'].value.replace(/-/g,''),
            "facebook": personalDataForm['facebook'].value || null,
            "twitter": personalDataForm['twitter'].value || null,
            "instagram": personalDataForm['instagram'].value || null,
            "email": personalDataForm['email'].value,
            "address": {
                "street": personalDataForm['homeStreet'].value,
                "number": personalDataForm['homeNumber'].value,
                "building": personalDataForm['homeBuildingName'].value || null,
                "apartment": personalDataForm['homeAppartmentNumber'].value || null,
                "town": personalDataForm['homeTown'].value || null,
                "city": personalDataForm['homeCity'].value || null,
                "state": personalDataForm['homeState'].value || null
            },
            "employment_data": {
                "employment_type": employmentDataForm['employmentType'].value,
                "company_name": employmentDataForm['companyName'].value,
                "tel": employmentDataForm['companyTel'].value.replace(/-/g,''),
                "tel_ext": employmentDataForm['companyTelExt'].value || null,
                "current_role": employmentDataForm['jobRol'].value,
                "start_date": employmentDataForm['hiringDate'].value,
                "monthly_salary": employmentDataForm['monthlyIncome'].value,
                "other_income": employmentDataForm['otherIncome'].value,
                "street": employmentDataForm['jobStreet'].value,
                "number": employmentDataForm['jobStreetNumber'].value,
                "building": employmentDataForm['jobBuildingName'].value || null,
                "town": employmentDataForm['jobCitySector'].value,
                "city": employmentDataForm['jobCity'].value,
                "state": employmentDataForm['jobTown'].value
            }
        }
    }

    fetch('/crear_solicitud/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        body: JSON.stringify(request)
    }).then((accepted) => {
        // console.log(request);
        if (!accepted.ok) {
            document.getElementById('errorAlert').hidden = false;
        }
        else{
            personalDataForm.reset();
            employmentDataForm.reset();
            loanDataForm.reset();
            document.getElementById('errorAlert').hidden = true;
            requestContainer.hidden = true;
            successMsg.hidden = false;
        }
    })
});

backToFirstSectionBtn.addEventListener('click', function (event) {
    hideElements(secondSectionItems);
    showElements(firstSectionItems);
    scrollTo(position.top);
    event.preventDefault();
});

backToSecondSectionBtn.addEventListener('click', function (event) {
    hideElements(finalSectionItems);
    showElements(secondSectionItems);
    scrollTo(position.top);
    event.preventDefault();
});

let hideElements = function (htmlCollection) {
    for (const element of htmlCollection) {
        element.hidden = true;
    }
}

let showElements = function (htmlCollection) {
    for (const element of htmlCollection) {
        element.hidden = false;
    }
}

let scrollTo = function (position) {
    window.scrollTo(position.x, position.y)
}

let position = { top: { x: 0, y: 0 } }

let isValidForm = function (form) {
    if (!form.checkValidity()){
        form.classList.add("was-validated");
        return false;
    }
    
    form.classList.remove("was-validated");
    return true;
}

// length validation should depend on id type
const idTypeSelector = document.getElementById('idType');
const idNumberField = document.getElementById('idNumber');

idTypeSelector.addEventListener('change', function(event) {
    if (event.target.value == 'E') {
        idNumberField.minLength = 9;
    }
    else {
        idNumberField.minLength = 11;
    }
}, false)

function getCsrfToken() {
    return document.cookie.split(';').find(x => x.startsWith('csrftoken')).split('=')[1]
}