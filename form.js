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

        // Obtiene los datos del formulario
        const formData = new FormData(form);
        const data = {
            id_medico: 1,
            usuario_rut: formData.get('rut'),
            fecha: formData.get('fechaCita'),
            motivo: formData.get('motivo')
        };

        // Envía los datos al backend usando una solicitud POST
        fetch('http://127.0.0.1:5000/ingresar_cita', {  // Asegúrate de que la URL apunte al puerto correcto
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.status === 'success') {
                window.location.href = "medico.html";
            } else {
                // Maneja el error
                alert('Error al enviar la cita');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al enviar la cita');
        });
    });
});