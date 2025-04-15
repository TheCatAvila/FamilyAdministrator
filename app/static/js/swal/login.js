document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita la recarga de la página

    let formData = new FormData(this);

    fetch("/login_user", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirige primero y luego muestra la alerta en la nueva página
            sessionStorage.setItem("login_success", "true"); // Guardar en sessionStorage
            window.location.href = "/"; 
        } else {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: data.message,
                confirmButtonText: "Aceptar",
                confirmButtonColor: "#007BFF", // Color azul para el botón "Aceptar"
            });
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});