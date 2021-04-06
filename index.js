var i = 0

var Lst = [];

window.onload = init;


async function init() {
    var r = await fetch('http://localhost:8080/amt', {
        method: 'POST',
    }).then(resp => resp.text()).then((data) => { return data; });
    r = parseInt(r, 10);
    for (var a = 0; a < r; a++) {
        Lst.push(new Audio('audio' + i + '.mp3'));
    }
}

function Next() {
    Lst[i].play();
    i++;
}