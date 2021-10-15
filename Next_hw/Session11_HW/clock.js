const clockContent = document.querySelector('.now');

const getCurrentTime = () => {
const date = new Date();
// console.log(date);
const year = date.getFullYear();
const month = date.getMonth()+1;
const day = date.getDate();
const hours = date.getHours();
const minutes = date.getMinutes();
const seconds = date.getSeconds();

    const time = `${year}년 ${month<10?'0'+month:month}월 ${day<10?'0'+day:day}일 ${hours<10?'0'+hours:hours}시${minutes<10?'0'+minutes:minutes}분${seconds<10?'0'+seconds:seconds}초`
clockContent.innerText = time;

};

const initClock = () => {
    getCurrentTime();
    setInterval(getCurrentTime, 1000);
};

initClock();
