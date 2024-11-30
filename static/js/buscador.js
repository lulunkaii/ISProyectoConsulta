window.onload = function() {
    // Muestra el spinner cuando la página cargue
    const spinner = document.querySelector('.spinner');
    const searchScreen = document.querySelector('.search-screen');
    
    // Simula el tiempo de carga (por ejemplo, 2 segundos)
    setTimeout(function() {
        // Desvanece el spinner
        spinner.style.opacity = 0;
        
        // Espera a que el spinner termine de desvanecerse
        setTimeout(function() {
            // Oculta el spinner completamente
            spinner.style.display = 'none';
            
            // Muestra la pantalla de búsqueda con desvanecimiento
            searchScreen.style.display = 'block';
            searchScreen.style.opacity = 1;
        }, 400);  // El tiempo de la transición del spinner
    }, 2000);  // Tiempo de carga (2 segundos)
};


document.addEventListener('DOMContentLoaded', function() {
    // Cargar filtros
    fetch('/get_filters')
        .then(response => response.json())
        .then(data => {
            // Llenar los filtros con los datos obtenidos
            const especialidadFilter = document.getElementById('especialidadFilter');
            const areaFilter = document.getElementById('areaFilter');
            const convenioFilter = document.getElementById('convenioFilter');
            
            // Llenar especialidades
            data.especialidades.forEach(especialidad => {
                const option = document.createElement('option');
                option.value = especialidad;
                option.textContent = especialidad;
                especialidadFilter.appendChild(option);
            });
            
            // Llenar áreas
            data.areas.forEach(area => {
                const option = document.createElement('option');
                option.value = area;
                option.textContent = area;
                areaFilter.appendChild(option);
            });

            // Llenar convenios
            data.convenios.forEach(convenio => {
                const option = document.createElement('option');
                option.value = convenio;
                option.textContent = convenio;
                convenioFilter.appendChild(option);
            });
        })
        .catch(error => console.error('Error al cargar filtros:', error));

    // Escuchar cambios en los filtros para buscar doctores
    document.querySelectorAll('.filter-bar').forEach(element => {
        element.addEventListener('change', searchDoctors);
        console.log('Escuchando cambios en los filtros');
    });

    document.getElementById('searchInput').addEventListener('input', searchDoctors);
});

function searchDoctors() {
    const especialidad = document.getElementById('especialidadFilter').value;
    const area = document.getElementById('areaFilter').value;
    const convenio = document.getElementById('convenioFilter').value;
    const name = document.getElementById('searchInput').value;

    const url = `/obtener_medicos?especialidad=${especialidad}&area=${area}&convenio=${convenio}&name=${name}`;
    
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al obtener medicos');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data); // Añadido para inspeccionar los datos
          // Asegúrate de que data es un array
        if (Array.isArray(data)) {
                displayDoctors(data);
            
        } else {
            console.error("Los doctores no están en un array:", doctors);
        }
    })
    .catch(error => console.error('Error al buscar doctores:', error));
}

function displayDoctors(doctors) {
    const resultsContainer = document.querySelector('.results-container');
    resultsContainer.innerHTML = '';  // Limpiar resultados anteriores
    
    if (doctors.length === 0) {
        resultsContainer.innerHTML = '<p>No se encontraron doctores</p>';
    }

    doctors.forEach(doctor => {
        const doctorCard = document.createElement('div');
        doctorCard.classList.add('opcion-medico');
        
        sexo = doctor.sexo == 'M'? "mars": "venus"; 
        let imagen = null;
        if (imagen == null){
            imagen = doctor.sexo == "M" ? "https://w7.pngwing.com/pngs/945/530/png-transparent-male-avatar-boy-face-man-user-flat-classy-users-icon.png": "https://w7.pngwing.com/pngs/1006/489/png-transparent-female-avatar-girl-face-woman-user-flat-classy-users-icon.png"
        }
            
        
        doctorCard.innerHTML = `
            <div class="card profile-header" id="${doctor.id}">
                <div class="body">
                    <div class="element profile-image">
                        <img src="${imagen}" alt="${doctor.nombre}">
                    </div>
                    <div class="element info-contacto">
                        <h4 class="nombre-medico"><strong>${doctor.nombre}</strong></h4>
                        <h5 class="especialidad-medico"><i>${doctor.especialidad}</i></h5>
                        <p><i class="fas fa-${sexo} sexo-medico"></i><p>
                        <table>
                            <tr><td><i class="fas fa-map-marker-alt"></i></td><td>${doctor.ciudad}</td></tr>
                            <tr><td><i class="fas fa-phone"></i></td><td>${doctor.telefono}</td></tr>
                            <tr><td><i class="fas fa-envelope"></i></td><td><a href="mailto:michael">${doctor.correo}</a></td></tr>

                        </table>
                    </div>
                    <div class="element informacion">
                        <label class="titulo_info">Convenio</label><p class="convenio-medico">${doctor.convenio}</p>
                        <label class="titulo_info">Descripción</label><p class="descripcion-medico">${doctor.descripcion}</p>
                        <label class="titulo_info">Estudios</label><p class="estudios-medico">${doctor.estudios}</p>

                    </div>
                </div>
            </div>
        `;
        resultsContainer.appendChild(doctorCard);
    });
}
