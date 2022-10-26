'use strict'

let timeHeader = document.querySelector("#time");

let today = new Date();
let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

timeHeader.innerHTML = `Current time is ${time}`