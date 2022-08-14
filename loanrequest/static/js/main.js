const orderingParams = {};
const filterParams = {};

const States = {
    None: 0,
    Ascending: 1,
    Descending: 2,
    
}

class OrderingParam {
    constructor(name) {
        this.name = name || '';
        this.state = States.None;
    }

    transition() {
        this.state = ++this.state % 3
    };

    getParam() {
        if (this.state == States.Ascending) {
            return `+${this.name}`
        }
        else if (this.state == States.Descending) {
            return `-${this.name}`
        }

        return '';
    }
}

const orderByDate = new OrderingParam('date');
const orderByAmount = new OrderingParam('amount_requested');

document.getElementById('orderByDate').addEventListener('click', function (event) {
    addOrderingParam(orderByDate);
    changeIcon(orderByDate.state, document.getElementById('orderDateIcon'), {
        [`${States.None}`]: "empty-icon",
        [`${States.Ascending}`]: "bi-sort-up",
        [`${States.Descending}`]: "bi-sort-down"
    })

});

document.getElementById('orderByAmount').addEventListener('click', function (event) {
    addOrderingParam(orderByAmount);
    changeIcon(orderByAmount.state, document.getElementById('orderAmountIcon'), {
        [`${States.None}`]: "empty-icon",
        [`${States.Ascending}`]: "bi-sort-numeric-up",
        [`${States.Descending}`]: "bi-sort-numeric-down-alt"
    })
});

const addOrderingParam = function (orderingParam) {
    orderingParam.transition();
    orderingParams[orderingParam.name] = orderingParam.getParam();
}


const changeIcon = function (state, element, classes) {
    const transitions = {
        [`${States.None}`]: { from: States.Descending, to: States.Ascending },
        [`${States.Ascending}`]: { from: States.None, to: States.Descending },
        [`${States.Descending}`]: {from: States.Ascending, to: States.None }
    }
   
    element.classList.remove(classes[transitions[state].from])
    element.classList.add(classes[state]);
}