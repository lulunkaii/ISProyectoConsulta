// Ejecuta el script una vez que el contenido del documento ha sido completamente cargado.
document.addEventListener("DOMContentLoaded", function () {
    const urlParams = new URLSearchParams(window.location.search);
    const isWeekly = urlParams.get('semana');
    
    // Si la URL contiene el parámetro "semana", obtiene los valores del día, mes y año para generar el calendario semanal.
    if (isWeekly) {
        const day = parseInt(urlParams.get('dia'), 10);
        const month = urlParams.get('mes');
        const year = parseInt(urlParams.get('ano'), 10);

        if (day && month && year) {
            document.getElementById("calendarTitle").innerText = `Calendario de la Semana del ${day} de ${month}`;

            // Convertir el nombre del mes a su índice numérico
            const monthIndex = getMonthIndex(month);
            if (monthIndex === -1) {
                document.getElementById("calendarContainer").innerText = "Mes inválido.";
                return;
            }

            // Formatear la fecha en el formato YYYY-MM-DD
            const formattedDate = `${year}-${String(monthIndex + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;

            fetch(`http://127.0.0.1:5000/obtener_horas_ocupadas?fecha=${formattedDate}`) // Obtener las citas agendadas para la fecha especificada (Reemplazar la URL con la correcta)
                .then(response => response.json()) // Convertir la respuesta a JSON
                .then(agendadas => {
                    const citasFomateadas = formatAppointments(agendadas);
                    generateAppointmentsList(citasFomateadas);
                    generateWeeklyCalendar(day, month, year);
                })
                .catch(error => console.error("Error al obtener las citas:", error));
        } else {
            document.getElementById("calendarContainer").innerText = "No se ha especificado un día, mes o año.";
        }
    }
});

// Procesar citas agendadas para formatearlas correctamente
function formatAppointments(appointments) {
    return appointments.map(item => ({
        fecha: item['fecha'],
        hora: parseInt(item['hora'], 10)
    }));
}

// Función para convertir el nombre del mes en español a su índice (0 para enero, 11 para diciembre).
function getMonthIndex(monthName) {
    const months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
    return months.indexOf(monthName.toLowerCase());
}

// Lista de citas agendadas
const agendadas = []

// Generar la lista de citas agendadas
function generateAppointmentsList(citasFomateadas) {
    citasFomateadas.forEach((cita) => {
        agendadas.push(cita);
    });
}


// Lista de horas y fechas en proceso (Para probar)
const en_proceso = [
    { fecha: '2024-11-16', hora: 10 },
    { fecha: '2024-11-16', hora: 11 },
];

// Función para generar el calendario semanal basado en el día, mes y año proporcionados.
function generateWeeklyCalendar(day, month, year) {
    const container = document.getElementById("calendarContainer");
    container.innerHTML = ""; // Limpia el contenido anterior del contenedor del calendario

    const monthIndex = getMonthIndex(month); // Convierte el mes a índice numérico
    if (monthIndex === -1) {
        container.innerText = "Mes inválido.";
        return;
    }

    // Crea la fecha inicial a partir de los parámetros ingresados
    const date = new Date(year, monthIndex, day);
    
    // Lista de nombres de los días de la semana
    const daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    
    // Crea un array de horas, empezando desde las 8:00 hasta las 20:00 (13 horas)
    const hoursOfDay = Array.from({ length: 13 }, (_, i) => 8 + i);

    // Inicializa la matriz de selección
    var selectionMatrix = Array.from({ length: hoursOfDay.length }, () => Array(daysOfWeek.length).fill(0));

    // Crea la estructura de la tabla del calendario
    const table = document.createElement("table");
    table.className = "calendar-weekly";

    // Fila de encabezado para mostrar los días de la semana y el día correspondiente del mes
    const headerRow = document.createElement("tr");
    const emptyHeader = document.createElement("th");
    headerRow.appendChild(emptyHeader);

    daysOfWeek.forEach((dayOfWeek, index) => {
        const th = document.createElement("th");
        
        // Crea una nueva fecha para cada día de la semana calculado
        const currentDay = new Date(date);
        currentDay.setDate(date.getDate() - (date.getDay() === 0 ? 6 : date.getDay() - 1) + index);
        
        // Muestra el nombre del día y el número de día correctamente
        th.innerHTML = `${dayOfWeek} ${currentDay.getDate()}`;
        headerRow.appendChild(th);
    });

    table.appendChild(headerRow);

    // Crea las filas de horas en la tabla, con una celda para cada hora y botones dentro de cada celda
    hoursOfDay.forEach((hour, hourIndex) => {
        const row = document.createElement("tr");

        // Primera columna con la hora de la fila
        const hourCell = document.createElement("td");
        hourCell.innerHTML = `${hour}:00`;
        row.appendChild(hourCell);

        // Agrega las celdas para cada día de la semana en la fila de la hora
        for (let dayIndex = 0; dayIndex < daysOfWeek.length; dayIndex++) {
            const cell = document.createElement("td");
            const button = document.createElement("button");

            // Verificar si la fecha y hora están agendadas
            const currentDay = new Date(date);
            currentDay.setDate(date.getDate() - (date.getDay() === 0 ? 6 : date.getDay() - 1) + dayIndex);
            const formattedDate = currentDay.toISOString().split('T')[0];
            const isAgendada = agendadas.some(a => a.fecha === formattedDate && a.hora === hour);
            const isEnProceso = en_proceso.some(a => a.fecha === formattedDate && a.hora === hour);

            // Verificar si la fecha y hora ya pasaron
            const now = new Date();
            const currentDateTime = new Date(`${formattedDate}T${hour.toString().padStart(2, '0')}:00:00`);

            // Configuración del botón para mostrar si está agendado o no
            if (isAgendada || isEnProceso || currentDateTime < now) {
                if (isAgendada) {
                    button.classList.add("agendada"); // Añade la clase de agendado
                    button.style.backgroundColor = "red"; // Añade el fondo rojo
                } else if (isEnProceso) {
                    button.classList.add("in-process"); // Añade la clase de en proceso
                    button.style.backgroundColor = "orange"; // Añade el fondo amarillo
                } else if (currentDateTime < now) {
                    button.classList.add("past"); // Añade la clase de pasado
                    button.style.backgroundColor = "gray"; // Añade el fondo gris
                }
                button.disabled = true; // Deshabilita el botón
                button.style.cursor = "not-allowed"; // Fuerza el cursor
                button.onmouseenter = null; // Elimina cualquier cambio de hover
                button.onmouseleave = null; // Evita que se cambie al quitar el hover
            }

            // Configuración del botón para seleccionarlo al hacer clic
            button.className = "hour-button";
            button.dataset.fecha = `${formattedDate}T${hour.toString().padStart(2, '0')}:00:00`;
            button.onclick = function() {
                if (!this.disabled) {
                    this.classList.add("in_process");
                    selectionMatrix[hourIndex][dayIndex] = 1;
                    // Redirigir a la página de formulario con la fecha y hora seleccionadas
                    window.location.href = `/reserva/rellenar-datos?fechaCita=${encodeURIComponent(formattedDate + 'T' + hour + ':00')}`;
                }
            };

            cell.appendChild(button);
            row.appendChild(cell);
        }

        table.appendChild(row);
    });

    container.appendChild(table); // Agrega la tabla generada al contenedor del calendario
}

// Ejecuta la función de carga inicial del calendario semanal en caso de que se haya especificado la vista semanal.
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