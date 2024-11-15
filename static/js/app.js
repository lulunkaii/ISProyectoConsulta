const specialtyFilter = document.getElementById('specialtyFilter');
const doctorSelect = document.getElementById('doctorSelect');
const selectButton = document.getElementById('selectButton');
let selectedDoctor = null;

// Función para cargar todas las especialidades únicas
function loadSpecialties(doctors) {
    const specialties = new Set(doctors.map(doctor => doctor.specialty)); 
    specialties.forEach(specialty => {
        const option = document.createElement('option');
        option.value = specialty;
        option.textContent = specialty;
        specialtyFilter.appendChild(option);
    });
    
}


// Función para cargar los doctores
function loadDoctors(doctors) {
    doctorSelect.innerHTML = '<option value="">Selecciona un doctor</option>'; // Limpiamos las opciones
    doctors.forEach(doctor => {
        const option = document.createElement('option');
        option.value = doctor.id;
        option.textContent = `${doctor.name} (${doctor.specialty})`;
        doctorSelect.appendChild(option);
    });
    doctorSelect.disabled = false;
}

// Cargar doctores y especialidades al cargar la página
fetch('/doctors')
    .then(response => response.json())
    .then(doctors => {
        loadSpecialties(doctors); // Cargamos las especialidades
        loadDoctors(doctors); // Cargamos los doctores
    })
    .catch(error => {
        console.error('Error al cargar los doctores:', error);
        doctorSelect.disabled = true;
    });

specialtyFilter.addEventListener('change', function() {
    const specialty = specialtyFilter.value;

    if (!specialty) {
        // Si no hay especialidad seleccionada, mostramos todos los doctores
        fetch('/doctors')
            .then(response => response.json())
            .then(doctors => {
                loadDoctors(doctors); // Cargamos todos los doctores
            })
            .catch(error => {
                console.error('Error al cargar los doctores:', error);
                doctorSelect.disabled = true;
            });
        return;
    }

    // Si hay especialidad seleccionada, filtramos los doctores
    fetch(`/doctors?specialty=${specialty}`)
        .then(response => response.json())
        .then(filteredDoctors => {
            loadDoctors(filteredDoctors); // Cargamos los doctores filtrados
        })
        .catch(error => {
            console.error('Error al cargar los doctores:', error);
            doctorSelect.disabled = true;
        });
});

// Habilitamos el botón de selección cuando se elija un doctor
doctorSelect.addEventListener('change', function() {
    const selectedOption = doctorSelect.selectedOptions[0];
    selectedDoctor = selectedOption ? selectedOption.textContent : null;
    selectButton.disabled = !selectedDoctor;
});

selectButton.addEventListener('click', function() {
    if (selectedDoctor) {
        window.location.href = `/reserva?doctor=${encodeURIComponent(selectedDoctor)}`;
    } else {
        alert("Médico no seleccionado");
    }
});

// Obtenemos el botón y los íconos
const toggleButton = document.getElementById('dark-mode-toggle');
const lightIcon = document.getElementById('light-icon');
const darkIcon = document.getElementById('dark-icon');

// Función para alternar el modo oscuro
toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode'); // Alterna la clase dark-mode
    
    // Alternar los íconos
    if (document.body.classList.contains('dark-mode')) {
        darkIcon.style.display = 'inline';
        lightIcon.style.display = 'none';
    } else {
        darkIcon.style.display = 'none';
        lightIcon.style.display = 'inline';
    }
});

// Verificar el modo oscuro almacenado en localStorage (opcional)
if (localStorage.getItem('dark-mode') === 'enabled') {
    document.body.classList.add('dark-mode');
    darkIcon.style.display = 'inline';
    lightIcon.style.display = 'none';
}

// Guardar el estado del modo oscuro en localStorage
toggleButton.addEventListener('click', () => {
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        localStorage.setItem('dark-mode', 'disabled');
    }
});

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
        }, 500);  // El tiempo de la transición del spinner
    }, 2000);  // Tiempo de carga (2 segundos)
};

