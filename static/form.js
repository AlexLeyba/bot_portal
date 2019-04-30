function incrementValue() {
    var value = parseInt(document.getElementById('id_positive').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('id_positive').value = value;
}

function incrementValue1() {
    var value = parseInt(document.getElementById('id_negative').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('id_negative').value = value;
}

function incrementValue2() {
    var value = parseInt(document.getElementById('id_neutral').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('id_neutral').value = value;
}

function incrementValue3() {
    var value = parseInt(document.getElementById('id_notapplicable').value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById('id_notapplicable').value = value;
}