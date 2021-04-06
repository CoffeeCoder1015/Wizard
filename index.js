var i = 0
var amt = 0;
var Lst = [];

window.onload = init;


async function init() {
    var r = await fetch('http://localhost:8080/amt', {
        method: 'POST',
    }).then(resp => resp.text()).then((data) => { return data; });
    amt = parseInt(r, 10);
    for (var a = 0; a < amt; a++) {
        Lst.push(new Audio('audio' + a + '.mp3'));
    }
    console.log(Lst);
}

function Next() {
    if (i >= amt) {
        i = 0;
    }
    Lst[i].play();
    document.getElementById("idn").innerHTML=i+1;
    i++;
    console.log(i);
}

function Reset() {
    i = 0;
}