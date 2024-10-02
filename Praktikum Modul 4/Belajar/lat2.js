function luas() {
    let r = Number(document.getElementById("r").value);
    let luas = 4/3*3.14*r*r*r;
    document.getElementById("luas").innerHTML = luas ;
}

function volume() {
    let r = Number(document.getElementById("r").value);
    let volume = 4*3.14*r*r;
    document.getElementById("volume").innerHTML = volume ;
}
