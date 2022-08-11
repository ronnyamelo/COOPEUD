const firstSectionItems = document.getElementsByClassName('form-first-section');
const secondSectionItems = document.getElementsByClassName('form-second-section');
const finalSectionItems = document.getElementsByClassName('form-final-section');

const backToFirstSectionBtn = document.getElementById('backToFirstSection');
const backToSecondSectionBtn = document.getElementById('backToSecondSection');
const toSecondSectionBtn = document.getElementById('toSecondSection');
const toFinalSectionBtn = document.getElementById('toFinalSection');

toSecondSectionBtn.addEventListener('click', function (event) {
    hideElements(firstSectionItems);
    showElements(secondSectionItems);
    scrollTo(position.top)
    event.preventDefault()
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

toFinalSectionBtn.addEventListener('click', function (event) {
    hideElements(secondSectionItems);
    showElements(finalSectionItems);
    scrollTo(position.top);
})

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