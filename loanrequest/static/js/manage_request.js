const approveRequestBtn = document.getElementById('approve-request');
const denyRequestBtn = document.getElementById('deny-request');
const cancelRequestBtn = document.getElementById('cancel-request');
const completeRequestBtn = document.getElementById('complete-request');
const requestUrl = document.getElementById('request-url')

function getCsrfToken() {
    return document.cookie.split(';').find(x => x.startsWith('csrftoken='))?.split('=')[1];
}
async function sendRequest(url, payload, method) {
    const response = await fetch(url, {
        method: method,
        body: JSON.stringify(payload),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        },
        redirect: 'follow'
    })

    return response;
}

const requestStatus = {
    approved: "APROBADO",
    denied: "RECHAZADO",
    canceled: "CANCELADO",
    completed: "COMPLETADO"
}

if (approveRequestBtn) {
    approveRequestBtn.addEventListener('click', function (event) {
        const form = document.forms['loan-request'];
        let payload =  {
            amount_approved: form['amount_approved'].value.replace(/,/g, ''),
            term: form['loan_term'].value,
            status: requestStatus.approved,
            approved_date: getDate()
        };
        sendRequest(requestUrl.value, payload, "PATCH").then(res => {
            handleResponse(res);
        });
    }, false);
}

if (denyRequestBtn) {
    denyRequestBtn.addEventListener('click', function (event) {
        let payload = {
            status: requestStatus.denied,
            denied_date: getDate()
        };

        sendRequest(requestUrl.value, payload, "PATCH").then(res => {
            handleResponse(res);
        });
    }, false);
}

if (cancelRequestBtn) {
    cancelRequestBtn.addEventListener('click', function (event) {
        let payload = {
            status: requestStatus.canceled,
            cancelation_date: getDate()
        };

        sendRequest(requestUrl.value, payload, "PATCH").then(res => {
            handleResponse(res);
        });
    }, false);
}

if (completeRequestBtn) {
    completeRequestBtn.addEventListener('click', function (event) {
        let payload = {
            status: requestStatus.completed,
            completed_date: getDate()
        };

        sendRequest(requestUrl.value, payload, "PATCH").then(res => {
            handleResponse(res);
        });
    }, false)
}

function getDate() {
    return new Date(Date.now()).toISOString();
}

function showErrorMsg() {
    alert("error");
}

function handleResponse(response) {
    if (response.ok) {
        window.location.reload();
    }
    else {
        showErrorMsg();
    }
}