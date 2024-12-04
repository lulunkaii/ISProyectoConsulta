let horasDeseleccionadas = new Set();

document.addEventListener("DOMContentLoaded", function () {
    const medico_id = localStorage.getItem('medico_id');
    const fecha = localStorage.getItem('fecha');

    if (medico_id && fecha) {
        document.getElementById("calendarTitle").innerText = `Disponibilidad para la Semana del ${fecha}`;

        // Convertir la fecha a un objeto Date
        const [year, month, day] = fecha.split('-').map(Number);
        generateWeeklyCalendar(day, month - 1, year); // Restar 1 al mes porque los meses en JavaScript son 0-indexados

        const formattedDate = `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;

        // Obtener y marcar las horas disponibles del médico
        fetch(`http://127.0.0.1:5000/obtener_agenda_medico?id_medico=${medico_id}&fecha=${formattedDate}`)
            .then(response => response.json())
            .then(horasDisponibles => {
                marcarHorasDisponibles(horasDisponibles);
            })
            .catch(error => console.error('Error al obtener las horas disponibles:', error));
    } else {
        document.getElementById("calendarContainer").innerText = "No se ha especificado un médico o una fecha.";
    }

    document.getElementById("submitAvailability").addEventListener("click", function () {
        const selectedHours = Array.from(document.querySelectorAll(".hour-button.selected")).map(button => button.dataset.fecha);
        const data = {
            id_medico: medico_id,
            horas: selectedHours
        };

        // Enviar las horas seleccionadas
        fetch('http://127.0.0.1:5000/ingresar_agenda', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.status === 'success') {
                alert('Disponibilidad enviada exitosamente');
            } else {
                alert('Error al enviar la disponibilidad');
            }
        })
        .catch(error => console.error('Error:', error));

        // Enviar las horas deseleccionadas
        horasDeseleccionadas.forEach(fecha => {
            const data = {
                id_medico: medico_id,
                fecha: fecha
            };

            fetch('http://127.0.0.1:5000/eliminar_hora_agenda', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                if (result.status === 'success') {
                    console.log('Hora eliminada exitosamente');
                } else {
                    console.error('Error al eliminar la hora');
                }
            })
            .catch(error => console.error('Error:', error));
        });

        horasDeseleccionadas.clear(); // Vaciar el conjunto después de enviar los cambios
    });
});

function generateWeeklyCalendar(day, month, year) {
    const container = document.getElementById("calendarContainer");
    container.innerHTML = ""; // Limpia el contenido anterior del contenedor del calendario

    const date = new Date(year, month, day);
    const daysOfWeek = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"];
    const hoursOfDay = Array.from({ length: 13 }, (_, i) => 8 + i);

    const table = document.createElement("table");
    table.className = "calendar-weekly";

    const headerRow = document.createElement("tr");
    const emptyHeader = document.createElement("th");
    headerRow.appendChild(emptyHeader);

    daysOfWeek.forEach((dayOfWeek, index) => {
        const th = document.createElement("th");
        const currentDay = new Date(date);
        currentDay.setDate(date.getDate() - (date.getDay() === 0 ? 6 : date.getDay() - 1) + index);
        th.innerHTML = `${dayOfWeek} ${currentDay.getDate()}`;
        headerRow.appendChild(th);
    });

    table.appendChild(headerRow);

    hoursOfDay.forEach((hour) => {
        const row = document.createElement("tr");
        const hourCell = document.createElement("td");
        hourCell.innerHTML = `${hour}:00`;
        row.appendChild(hourCell);

        for (let dayIndex = 0; dayIndex < daysOfWeek.length; dayIndex++) {
            const cell = document.createElement("td");
            const button = document.createElement("button");

            const currentDay = new Date(date);
            currentDay.setDate(date.getDate() - (date.getDay() === 0 ? 6 : date.getDay() - 1) + dayIndex);
            const formattedDate = currentDay.toISOString().split('T')[0];

            button.className = "hour-button";
            button.dataset.fecha = `${formattedDate}T${hour.toString().padStart(2, '0')}:00:00`;

            button.addEventListener("click", function () {
                if (this.classList.contains("selected")) {
                    this.classList.remove("selected");
                    horasDeseleccionadas.add(this.dataset.fecha); // Agregar al conjunto de deseleccionadas
                } else {
                    this.classList.add("selected");
                    horasDeseleccionadas.delete(this.dataset.fecha); // Eliminar de deseleccionadas si vuelve a ser seleccionada
                }
            });

            cell.appendChild(button);
            row.appendChild(cell);
        }

        table.appendChild(row);
    });

    container.appendChild(table);
}

function marcarHorasDisponibles(horasDisponibles) {
    horasDisponibles.forEach(hora => {
        const button = document.querySelector(`.hour-button[data-fecha="${hora.fecha}T${hora.hora.toString().padStart(2, '0')}:00:00"]`);
        if (button) {
            button.classList.add("selected");
            button.dataset.initiallySelected = "true"; // Marcar como inicialmente seleccionado
        }
    });
}