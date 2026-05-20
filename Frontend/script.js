const beachContainer = document.getElementById("beach-container")
const searchInput = document.getElementById("search-input")
const filterSelect = document.getElementById("filter-select")


let allBeaches = []


async function getBeaches(){

    try {
        const response = await fetch("http://127.0.0.1:8000/beaches")
        
        if(!response.ok) {
            console.error("Failed to fetch beaches:", response.status)
            return
        }
        const data = await response.json()
        allBeaches = data
        displayBeaches(allBeaches)
    } catch(error) {
        console.error("Error fetching beaches:", error)
    }
}


function getWeatherIcon(weather){

    const condition = weather.toLowerCase()

    if(condition.includes("clear")){
        return "☀️"
    }

    else if(condition.includes("cloud")){
        return "☁️"
    }

    else if(condition.includes("rain")){
        return "🌧️"
    }

    else if(condition.includes("thunder")){
        return "⛈️"
    }

    else if(condition.includes("mist") || condition.includes("fog")){
        return "🌫️"
    }

    else{
        return "🌍"
    }
}

function displayBeaches(beaches){

    beachContainer.innerHTML = ""

    beaches.forEach(beach => {

        const card = document.createElement("div")

        card.classList.add("beach-card")

        if(beach.safety_status === "Safe"){
            card.classList.add("safe")
        }

        else if(beach.safety_status === "Moderate"){
            card.classList.add("moderate")
        }

        else{
            card.classList.add("danger")
        }

        card.innerHTML = `

        <img src="${beach.img}" class="beach-image">

        <div class="card-top">

        <h2>${beach.name}</h2>

        <span class="badge ${beach.safety_status.toLowerCase()}-badge">
            ${beach.safety_status}
        </span>

        </div>

    <p class="city">${beach.city}</p>

    <div class="weather-info">

        <p>🌡 ${beach.temperature}°C</p>

        <p>
            ${getWeatherIcon(beach.weather)}
            ${beach.weather}
        </p>

        <p>🌬 ${beach.wind_speed} m/s</p>

    </div>

`

        beachContainer.appendChild(card)
    })
}

function applyFilters(){

    const searchText = searchInput.value.toLowerCase()

    const selectedSafety = filterSelect.value

    let filteredBeaches = allBeaches.filter(beach =>
        beach.name.toLowerCase().includes(searchText)
    )

    if(selectedSafety !== "All"){

        filteredBeaches = filteredBeaches.filter(beach =>
            beach.safety_status === selectedSafety
        )
    }

    displayBeaches(filteredBeaches)
}

filterSelect.addEventListener("change", applyFilters)
searchInput.addEventListener("input", applyFilters)


getBeaches()