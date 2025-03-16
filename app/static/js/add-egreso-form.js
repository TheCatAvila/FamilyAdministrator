document.getElementById("egresoForm").addEventListener("submit", function (event) {
    let isValid = true;

    // Validar fecha
    let fecha = document.getElementById("fecha");
    let fechaError = document.getElementById("fechaError");
    let hoy = new Date().toISOString().split("T")[0];

    if (!fecha.value) {
        fechaError.textContent = "La fecha es obligatoria.";
        isValid = false;
    } else if (fecha.value > hoy) {
        fechaError.textContent = "No puedes seleccionar una fecha futura.";
        isValid = false;
    } else {
        fechaError.textContent = "";
    }

    // Validar categoría
    let categoria = document.getElementById("categoria");
    let categoriaError = document.getElementById("categoriaError");

    if (!categoria.value) {
        categoriaError.textContent = "Debe seleccionar una categoría.";
        isValid = false;
    } else {
        categoriaError.textContent = "";
    }

    // Validar monto
    let monto = document.getElementById("monto");
    let montoError = document.getElementById("montoError");

    if (!monto.value) {
        montoError.textContent = "El monto es obligatorio.";
        isValid = false;
    } else {
        montoError.textContent = "";
    }

    // Si hay errores, detener envío
    if (!isValid) {
        event.preventDefault();
    }
});