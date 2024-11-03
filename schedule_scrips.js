function getParameterByName(name) {
    var url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function generateMonthlyCalendar(monthYear) {
    var container = document.getElementById("calendarContainer");
    container.innerHTML = "";
    var [month, year] = monthYear.split(' ');
    var date = new Date(`${month} 1, ${year}`);
    var daysInMonth = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    var firstDay = new Date(date.getFullYear(), date.getMonth(), 1).getDay();
    var daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    var table = document.createElement("table");
    var headerRow = document.createElement("tr");
    daysOfWeek.forEach(day => {
        var th = document.createElement("th");
        th.innerHTML = day;
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    var row = document.createElement("tr");
    for (var i = 0; i < (firstDay || 7) - 1; i++) {
        var cell = document.createElement("td");
        row.appendChild(cell);
    }

    for (var day = 1; day <= daysInMonth; day++) {
        if (row.children.length === 7) {
            table.appendChild(row);
            row = document.createElement("tr");
        }
        var cell = document.createElement("td");
        var button = document.createElement("button");
        button.className = "button";
        button.innerHTML = day;
        button.onclick = function() {
            window.location.href = `scheduler.html?dia=${this.innerHTML}&mes=${month}&ano=${year}`;
        };
        cell.appendChild(button);
        row.appendChild(cell);
    }

    while (row.children.length < 7) {
        var cell = document.createElement("td");
        row.appendChild(cell);
    }
    table.appendChild(row);
    container.appendChild(table);
}

function generateWeeklyCalendar(day, month, year) {
    var container = document.getElementById("calendarContainer");
    container.innerHTML = "";
    var date = new Date(`${month} ${day}, ${year}`);
    var daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    var hoursOfDay = Array.from({ length: 13 }, (_, i) => 8 + i);

    var table = document.createElement("table");
    var headerRow = document.createElement("tr");
    var emptyHeader = document.createElement("th");
    headerRow.appendChild(emptyHeader);
    daysOfWeek.forEach((day, index) => {
        var th = document.createElement("th");
        var currentDay = new Date(date);
        currentDay.setDate(date.getDate() - date.getDay() + index + 1);
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
            button.className = "button";
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
    var day = getParameterByName('dia');
    var mes = getParameterByName('mes');
    var year = new Date().getFullYear();

    if (day) {
        document.getElementById("calendarTitle").innerText = `Calendario de la Semana del ${day} de ${mes}`;
        generateWeeklyCalendar(day, mes, year);
    } else {
        if (!mes) {
            var now = new Date();
            mes = now.toLocaleString('default', { month: 'long' });
        }
        var monthYear = `${mes} ${year}`;
        document.getElementById("calendarTitle").innerText = `Calendario del Mes ${mes}`;
        generateMonthlyCalendar(monthYear);
    }
}
