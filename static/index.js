let c1_red = Math.floor(Math.random()*255);
let c1_green = Math.floor(Math.random()*255);
let c1_blue = Math.floor(Math.random()*255);
let c2_red = Math.floor(Math.random()*255);
let c2_green = Math.floor(Math.random()*255);
let c2_blue = Math.floor(Math.random()*255);

function changeColor(){
    document.querySelector('.testsite').style.backgroundColor = `rgb(${c1_red}, ${c1_blue}, ${c1_red}`;
    document.querySelector('.testsite').style.color = `rgb(${c2_red}, ${c2_blue}, ${c2_red}`;
}

function isDistinct() {
    const url = "/yeet"
    const method = "POST"
    const body = JSON.stringify({c1_red, c1_green, c1_blue, 
                                 c2_red, c2_green, c2_blue, distinct:true})
    const cb = response => {
        location.reload();
        return false;
    }
    retrieve(url, method, body, cb);
}

function notDistinct() {
    const url = "/yeet"
    const method = "POST"
    const body = JSON.stringify({c1_red, c1_green, c1_blue, 
                                 c2_red, c2_green, c2_blue, distinct: false})
    const cb = response => {
        location.reload();
        return false;
    }
    retrieve(url, method, body, cb);
}

function retrieve(url, method, body, callback, token){
    const options = {
        method: method,
        mod: 'cors',
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
    }
    if (body){
        options.body = JSON.stringify(body);
    }
    if (token){
        options.headers["X-CSRF-Token"] = token;
    }
    fetch(url, options)
        .then(response => {
            if (response.ok){
                return response.json();
            } else {
                throw new Error();
            }
        })
        .then(callback)
        .catch(error => console.log(error.message))
}