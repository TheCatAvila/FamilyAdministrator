// Mostrar la alerta en la esquina superior derecha después de redirigir
document.addEventListener("DOMContentLoaded", function() {
    if (sessionStorage.getItem("login_success") === "true") {
        sessionStorage.removeItem("login_success"); // Eliminar para que no se repita
        Swal.fire({
            icon: "success",
            title: "¡Inicio de sesión exitoso!",
            toast: true,
            position: "top-end",
            timer: 1500,
            showConfirmButton: false,
        });
    }
});