document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.delete-form').forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            // Opcional: usar atributos personalizados para texto
            const title = form.getAttribute('data-title') || '¿Estás seguro?';
            const text = form.getAttribute('data-text') || 'Esta acción no se puede deshacer.';

            Swal.fire({
                title: title,
                text: text,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    form.submit();
                }
            });
        });
    });
});