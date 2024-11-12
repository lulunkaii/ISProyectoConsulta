document.addEventListener("DOMContentLoaded", function () {
    const changeDateLink = document.getElementById("changeDateLink");
    const fechaCitaInput = document.getElementById("fechaCita");

    const urlParams = new URLSearchParams(window.location.search);
    const fechaCita = urlParams.get('fechaCita');

    if (fechaCita) {
        fechaCitaInput.value = fechaCita;
    }

    const convert_spanish = {
        "january": "enero", "february": "febrero", "march": "marzo", "april": "abril",
        "may": "mayo", "june": "junio", "july": "julio", "august": "agosto",
        "september": "septiembre", "october": "octubre", "november": "noviembre", "december": "diciembre"
    };

    changeDateLink.addEventListener("click", function (event) {
        event.preventDefault();

        const selectedDate = new Date(fechaCitaInput.value);

        const monthInEnglish = selectedDate.toLocaleString('default', { month: 'long' }).toLowerCase();
        
        const monthInSpanish = convert_spanish[monthInEnglish];

        window.location.href = `monthly_calendar.html?mes=${monthInSpanish}`;
    });
});
