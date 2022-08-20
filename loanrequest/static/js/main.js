const state = {
    None: 0,
    Ascending: 1,
    Descending: 2,
}

const transitions = {
    [`${state.None}`]: { from: state.Descending, to: state.Ascending },
    [`${state.Ascending}`]: { from: state.None, to: state.Descending },
    [`${state.Descending}`]: { from: state.Ascending, to: state.None }
}

class OrderingParam {
    constructor(name) {
        this.name = name;
        this.state = state.None;
    }

    transition() {
        this.state = transitions[this.state].to
    };

    getParam() {
        if (this.state == state.Ascending) {
            return `${this.name}`
        }
        else if (this.state == state.Descending) {
            return `-${this.name}`
        }
        return '';
    }
}
const orderByDate = new OrderingParam('request_date');
const orderByAmount = new OrderingParam('amount_requested');

document.getElementById('orderByDate').addEventListener('click', function (event) {
    orderByDate.transition();
    let url = getUrl();
    url.searchParams.set('ordering', orderByDate.getParam());
    event.target.href = url.href
});

document.getElementById('orderByAmount').addEventListener('click', function (event) {
    orderByAmount.transition();
    let url = getUrl();
    url.searchParams.set('ordering', orderByAmount.getParam());
    event.target.href = url.href
});

function changeIcon(currentState, element, classes) {
    let oldClass = classes[transitions[currentState].from];
    let newClass = classes[currentState]
    element.classList.remove(oldClass)
    element.classList.add(newClass);
}

function getUrl() {
    return new URL(window.location.href);
}

function setInitialValues() {
    let url = getUrl();

    // ordering
    if (url.searchParams.has('ordering')) {
        let order = url.searchParams.get('ordering');

        // date
        if (order.includes('request_date')) {
            orderByDate.state = state.Ascending;
        }

        if (order.includes('-request_date')) {
            orderByDate.state = state.Descending;
        }

        changeIcon(orderByDate.state, document.getElementById('orderDateIcon'), {
            [`${state.None}`]: "empty-icon",
            [`${state.Ascending}`]: "bi-sort-up",
            [`${state.Descending}`]: "bi-sort-down"
        });

        // amount
        if (order.includes('amount_requested')) {
            orderByAmount.state = state.Ascending;
        }

        if (order.includes('-amount_requested')) {
            orderByAmount.state = state.Descending;
        }

        changeIcon(orderByAmount.state, document.getElementById('orderAmountIcon'), {
            [`${state.None}`]: "empty-icon",
            [`${state.Ascending}`]: "bi-sort-numeric-up",
            [`${state.Descending}`]: "bi-sort-numeric-down-alt"
        });
    }

    // amount ordering

    // filters
    let counter = 0;
    let filters = [
        'status',
        'applicant__first_name__icontains',
        'applicant__last_name__icontains',
        'applicant__id_number__icontains',
        'request_date__gte',
        'request_date__lte',
        'amount_requested__gte',
        'amount_requested__lte',
    ]
    const form = document.forms['filters']

    filters.forEach(x => {
        form[x].value = searchParam(x) || "";
        form[x].value && counter++;
    });

    // date and amount should acount for only one filter
    form['request_date__gte'].value && form['request_date__lte'].value && --counter;
    form['amount_requested__gte'].value && form['amount_requested__lte'].value && --counter;

    document.getElementById('filterCount').innerText = counter;
}

function searchParam(name) {
    params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParam, prop) => searchParam.get(prop)
    })

    return params[name]
}

setInitialValues();
