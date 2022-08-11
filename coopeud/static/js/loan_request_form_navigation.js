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

const apiUrl = 'http://localhost:8000/api/solicitudes/';

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
            alert('Invalid Data');
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
            "tel": personalDataForm['telephone'].value || null,
            "celphone": personalDataForm['celphone'].value,
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
                "tel": employmentDataForm['companyTel'].value,
                "tel_ext": employmentDataForm['companyTelExt'].value || null,
                "current_role": employmentDataForm['jobRol'].value,
                "start_date": employmentDataForm['hiringDate'].value,
                "monthly_salary": employmentDataForm['monthlyIncome'].value,
                "street": employmentDataForm['jobStreet'].value,
                "number": employmentDataForm['jobStreetNumber'].value,
                "building": employmentDataForm['jobBuildingName'].value,
                "town": employmentDataForm['jobCitySector'].value,
                "city": employmentDataForm['jobCity'].value,
                "state": employmentDataForm['jobTown'].value
            }
        }
    }

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(request)
    }).then(resp => {
            return resp.json()
    }).then(data => {
        console.log(data);
        personalDataForm.reset();
        employmentDataForm.reset();
        loanDataForm.reset();

    }).catch(error => console.log("Error"));


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
    
    return true;
}