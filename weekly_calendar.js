document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const isWeekly = urlParams.get('semana');
    
    if (isWeekly) {
        const day = parseInt(urlParams.get('dia'), 10);
        const month = urlParams.get('mes');
        const year = parseInt(urlParams.get('ano'), 10);
        if (day && month && year) {
            document.getElementById("calendarTitle").innerText = `Calendario de la Semana del ${day} de ${month}`;
            generateWeeklyCalendar(day, month, year);
        } else {
            document.getElementById("calendarContainer").innerText = "No se ha especificado un día, mes o año.";
        }
    }
});

function getParameterByName(name) {
    var url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function generateWeeklyCalendar(day, month, year) {
    var container = document.getElementById("calendarContainer");
    container.innerHTML = "";
    var date = new Date(`${month} ${day}, ${year}`);
    var daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    var hoursOfDay = Array.from({ length: 13 }, (_, i) => 8 + i);

    var table = document.createElement("table");
    table.className = "calendar-weekly";
    var headerRow = document.createElement("tr");
    var emptyHeader = document.createElement("th");
    headerRow.appendChild(emptyHeader);
    daysOfWeek.forEach((day, index) => {
        var th = document.createElement("th");
        var currentDay = new Date(date);
        currentDay.setDate(date.getDate() - (date.getDay() === 0 ? 7 : date.getDay()) + index + 1);
        th.innerHTML = `${daysOfWeek[index]} ${currentDay.getDate()}`;
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    hoursOfDay.forEach(hour => {
        var row = document.createElement("tr");
        var hourCell = document.createElement("td");
        hourCell.innerHTML = `${hour}:00`;
        row.appendChild(hourCell);
        for (var i = 0; i < daysOfWeek.length; i++) {
            var cell = document.createElement("td");
            var button = document.createElement("button");
            button.className = "hour-button";
            button.onclick = function() {
                this.classList.toggle("selected");
            };
            cell.appendChild(button);
            row.appendChild(cell);
        }
        table.appendChild(row);
    });

    container.appendChild(table);
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const isWeekly = urlParams.get('semana');
    
    if (isWeekly) {
        const day = parseInt(urlParams.get('dia'), 10);
        const month = urlParams.get('mes');
        const year = parseInt(urlParams.get('ano'), 10);
        if (day && month && year) {
            document.getElementById("calendarTitle").innerText = `Calendario de la Semana del ${day} de ${month}`;
            generateWeeklyCalendar(day, month, year);
        } else {
            document.getElementById("calendarContainer").innerText = "No se ha especificado un día, mes o año.";
        }
    }
}