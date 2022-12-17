var element = document.getElementById("key-0")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "0";
});
var element = document.getElementById("key-1")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "1";
});

var element = document.getElementById("key-2")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "2";
});

var element = document.getElementById("key-3")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "3";
});

var element = document.getElementById("key-4")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "4";
});

var element = document.getElementById("key-5")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "5";
});


var element = document.getElementById("key-6")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "6";
});

var element = document.getElementById("key-7")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "7";
});

var element = document.getElementById("key-8")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "8";
});

var element = document.getElementById("key-9")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "9";
});

var element = document.getElementById("key-decimal")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + ".";
});

var element = document.getElementById("key-delete")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML.slice(0,document.getElementById("output").innerHTML.length-1);
});

var element = document.getElementById("key-add")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "+";
});

var element = document.getElementById("key-subtract")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "-";
});

var element = document.getElementById("key-multiply")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "x";
});

var element = document.getElementById("key-divide")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = document.getElementById("output").innerHTML + "/";
});

var element = document.getElementById("key-equals")
element.addEventListener("click", function() {
    document.getElementById("output").innerHTML = calculateResult();
});

function calculateResult() {
    var equation = document.getElementById("output").innerHTML
    document.getElementById("output").innerHTML = eval(equation)
}