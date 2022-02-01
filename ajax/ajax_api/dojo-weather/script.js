const api_key = "fc09c6098578cd7f289b7eb35ef74d44"
const cityLocation = {
    Burbank: {name:"Burbank",lat:34.1816482,lon:-118.3258554},
    Chicago: {name:"Chicago",lat:41.8755616, lon:-87.6244212},
    Dallas: {name:"Dallas", lat:32.7762719, lon:-96.7968559},
    SanJose: {name:"San Jose", lat:37.3361905, lon:-121.890583}
}

function loadPage() {
    setDay()
    loadCity("SanJose")
}

function dayOfWeek(day) {
    let days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    return days[day]
}

function setDay() {
    day2 = document.getElementById('day2_day')
    day3 = document.getElementById('day3_day')
    let today = new Date()
    let tomorrow = new Date(today)
    tomorrow.setDate(today.getDate() + 1)
    day2.innerText = dayOfWeek(tomorrow.getDay())
    let day3Date = new Date(today)
    day3Date.setDate(today.getDate() + 2)
    day3.innerText = dayOfWeek(day3Date.getDay())
}

async function loadCity(cityName) {
    console.log(cityName);
    alert("Loading weather report...")
    let city = cityLocation[cityName]
    let weather = await getWeatherData(city.lat, city.lon)
    let city_header = document.getElementById('city')
    city_header.innerText = city.name
    for(let i = 0; i < 4; i++) {
        let temperatures = []
        temperatures.push(weather.daily[i].temp.min)
        temperatures.push(weather.daily[i].temp.max)
        setTemperature(i,temperatures)
        setWeatherImage(i,weather.daily[i].weather[0].main)
        setDescription(i,weather.daily[i].weather[0].description);
    }
}

function setTemperature(day,temperatures){
    let dayMin = document.getElementById(`day${day}_low`)
    let dayMax = document.getElementById(`day${day}_high`)
    dayMin.innerText = Math.round(temperatures[0])
    dayMax.innerText = Math.round(temperatures[1])
}

function setWeatherImage(day,weatherCondition) {
    let dayCondition = document.getElementById(`day${day}_condition`)
    if (weatherCondition === "Clear") {
        dayCondition.src = "images/some_sun.png"
    } else if (weatherCondition === "Clouds") {
        dayCondition.src = "images/some_clouds.png"
    } else {
        dayCondition.src = "images/some_rain.png"
    }
}

function setDescription(day,description) {
    let dayDescription = document.getElementById(`day${day}_description`)
    dayDescription.innerText=description
}

function chooseUnits(element) {
    temperatureList = document.querySelectorAll(".temperature")
    if (element.value == "Celcius") {
        console.log("C")
        for (var i = 0; i < temperatureList.length; i++) {
            tempF = parseInt(temperatureList[i].innerText)
            temperatureList[i].innerText = Math.round((tempF - 32) * 5 / 9)
        }
    }
    else if (element.value == "Fahrenheit") {
        console.log("F")
        for (var i = 0; i < temperatureList.length; i++) {
            tempC = parseInt(temperatureList[i].innerText)
            temperatureList[i].innerText = Math.round(tempC * 9 / 5 + 32)
        }
    }
}

function acceptCookies() {
    cookiesWindow = document.querySelector("#cookie-notice")
    cookiesWindow.remove()
}

async function getCityLocation(cityName) {
    var response = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${api_key}`)
    var cityData = await response.json()
    return cityData
}

async function getWeatherData(lat,lon) {
    var response = await fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=current,minutely,hourly,alerts&units=metric&appid=${api_key}`)
    // https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=
    var weatherData = await response.json()
    return weatherData
}