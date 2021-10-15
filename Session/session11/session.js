const title = document.querySelector('#title');
const divs = document.querySelectorAll('div');

console.log(divs);

for(let i = 0; i < divs.length; i++){
    const currentDiv = divs[i];
    currentDiv.style.fontSize = `${(i+1) * 7}px`;
    currentDiv.innerHTML = `${i+1}번째 div`;
}

alert('에러입니다.');

// divs.forEach((div, i)=>{
//     div.innerHTML = `${i+1}번째 div`;
//     div.style.fontSize = `${(i+1) * 7}px`
// });