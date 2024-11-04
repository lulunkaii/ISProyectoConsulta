document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const monthParam = urlParams.get('mes') || new Date().toLocaleString('default', { month: 'long' });
    const yearParam = new Date().getFullYear(); // Usa el año actual por defecto
    generateMonthlyCalendar(`${monthParam} ${yearParam}`);
});

function generateMonthlyCalendar(monthYear) {
    const container = document.getElementById("calendarContainer");
    container.innerHTML = ""; // Limpiar contenido anterior

    // Separar mes y año del parámetro
    const [month, year] = monthYear.split(' ');
    const date = new Date(`${month} 1, ${year}`);
    const daysInMonth = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const firstDay = new Date(date.getFullYear(), date.getMonth(), 1).getDay();

    // Crear el contenedor del calendario con el estilo aplicado
    const calendarDiv = document.createElement("div");
    calendarDiv.className = "calendar";

    // Barra del mes
    const monthDiv = document.createElement("div");
    monthDiv.className = "month";
    monthDiv.innerHTML = `
        <div>${month} <span class="year">${year}</span></div>
    `;
    calendarDiv.appendChild(monthDiv);

    // Nombres de los días de la semana
    const daysDiv = document.createElement("div");
    daysDiv.className = "days";
    const daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    daysOfWeek.forEach(day => {
        const daySpan = document.createElement("span");
        daySpan.innerText = day;
        daysDiv.appendChild(daySpan);
    });
    calendarDiv.appendChild(daysDiv);

    // Contenedor de las fechas
    const datesDiv = document.createElement("div");
    datesDiv.className = "dates";

    // Espacios en blanco antes del primer día del mes
    for (let i = 0; i < (firstDay || 7) - 1; i++) { // Ajuste para empezar en lunes
        const emptyDiv = document.createElement("div");
        datesDiv.appendChild(emptyDiv);
    }

    // Añadir los días del mes
    for (let day = 1; day <= daysInMonth; day++) {
        const button = document.createElement("button");
        button.className = "date-button";
        button.innerHTML = day;
        button.onclick = function () {
            window.location.href = `scheduler_week.html?semana=true&dia=${day}&mes=${month}&ano=${year}`;
        };

        datesDiv.appendChild(button);
    }

    calendarDiv.appendChild(datesDiv);
    container.appendChild(calendarDiv);
}
