
let placeholder = document.querySelector("#questions");
let out = "";
for(let i = 0; i < 10; i++){
    out += `<div><h3> Question Number ${i+1}</h3>
                <p> Question Goes Here </p>
    
    </div> `
}

placeholder.innerHTML = out;
