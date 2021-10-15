const input = document.querySelector("#city");
const button = document.querySelector("#submit");
const weatherBox = document.querySelector("#weatherBox");

const API_KEY = "bf37bf6c21911fbcac7102f7c3eb7751";

button.addEventListener("click", async () => {
  const city = input.value;

  const res = await axios.get(
    `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${API_KEY}`
  );
  // console.log(res);

  const name = res.data.city.name;
  const tomorrow = [];
  for (let i = 5; i < 13; i++) {
    tomorrow.push(res.data.list[i]); //3시간별 기상정보
  }
  console.log(tomorrow);

  weatherBox.innerHTML = "";

  for (let i = 0; i < 8; i++) {
    const html = `
    <div class='box'>
      <div>${name}</div>
      <div>${i * 3}:00</div>
      <img class="icon" src="http://openweathermap.org/img/w/${
        tomorrow[i].weather[0].icon
      }.png">
      <div>${Math.round(tomorrow[i].main.temp - 273.15)}°C</div>
      <div>${tomorrow[i].weather[0].main}</div>
    </div>
    `;
    weatherBox.insertAdjacentHTML("Beforeend", html);
  }
});
