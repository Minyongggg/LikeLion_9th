const parent = document.querySelector(".parent");
const son1 = document.querySelector("#son1");
const son2 = document.querySelector("#son2");
const children = parent.querySelectorAll(".child")
const body = document.querySelector("body");

console.log(children);
console.dir(children);



// for (let i=0; i < children.length; i++){
//     children[i].classList.add("red");
// }

// for (const child of children) {
//     child.classList.add("blue");
// }

// children.forEach( child => {
//     child.classList.add("red");
// });

// const classRed = child => child.classList.add("red");
// classRed(son1);


// children.forEach(classRed);

const sj = document.createElement("div");
const yn = document.createElement("p");
yn.textContent = "저는 예나입니다";

sj.appendChild(yn)
document.body.appendChild(sj)

sj.setAttribute("id", "sj");
// sj.setAttribute("class", "parent");
// sj.classList.add("parent")


console.log(body)