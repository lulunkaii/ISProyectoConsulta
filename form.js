// Espera a que el contenido del documento se haya cargado completamente
document.addEventListener("DOMContentLoaded", function() {
    // Obtiene los parámetros de la URL
    const urlParams = new URLSearchParams(window.location.search);
    // Obtiene el valor del parámetro 'fechaCita'
    const fechaCita = urlParams.get('fechaCita');
    
    // Si se proporciona la fechaCita, la establece en el campo correspondiente
    if (fechaCita) {
        document.getElementById("fechaCita").value = fechaCita;
    }

    const form = document.getElementById("formCita");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío del formulario por defecto

        // Si el formulario se envía correctamente, redirige a la nueva página
        window.location.href = "medico.html";
    });
});