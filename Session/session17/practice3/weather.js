const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#weatherBox");

const API_KEY = "bf37bf6c21911fbcac7102f7c3eb7751";

button.addEventListener("click", async () => {
  // input에 입력된 도시명을 사용하여 적절한 uri로 날씨정보 요청
  // response받아서 weatherBox에 적절하게 넣어준다.
  // innerHTML활용!
  // weatherBox html template 예시
  /*
    `<div class="name">${name}</div>
     <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
     <div class="main">${main}</div>
     <div class="description">${description}</div>
     <div class="temp">${temp}°C</div>`
  */
  const cityName = input.value;
  const res = await axios.get(
    `http://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${API_KEY}`
  );
  console.log(res);
  setWeatherBox(res.data);
});

const setWeatherBox = ({ name, main, weather }) => {
  const temp = Math.round(main.temp - 275);
  weatherBox.innerHTML = `
  <div class="name">${name}</div>
  <img class="icon" src="http://openweathermap.org/img/w/${weather[0].icon}.png">
  <div class="main">${weather[0].main}</div>
  <div class="description">${weather[0].description}</div>
  <div class="temp">${temp}°C</div>
  `;
};
