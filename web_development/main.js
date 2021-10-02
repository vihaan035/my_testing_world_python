'use strict';
console.log("hallo0");
var plusButton=document.getElementById('plus');
console.log("hallo");
plusButton.addEventListener('click', function(){
    console.log("hallo2");
    var a=document.getElementById('fn');
    var b = document.getElementById('sn');
    var c = document.getElementById('result');
    c.innerHTML=a.value+b.value;
});