function formatMonto(input) {
    // Remover caracteres que no sean números
    let value = input.value.replace(/\D/g, "");

    // Convertir a número y luego a string formateado con puntos de miles
    let formattedValue = Number(value).toLocaleString("es-CL");

    // Asignar el valor formateado al input
    input.value = formattedValue;
}