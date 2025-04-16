document.addEventListener('DOMContentLoaded', function () {
    const editModal = document.getElementById('editSubcategory');
    if (editModal) {
        editModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;
            const id = button.getAttribute('data-subcategory-id');
            const name = button.getAttribute('data-subcategory-name');
            const budget = button.getAttribute('data-subcategory-budget');

            document.getElementById('edit_subcategory_id').value = id;
            document.getElementById('edit_subcategory_name').value = name;
            document.getElementById('edit_subcategory_budget').value = budget;
        });
    }

    const editModalExpenses = document.getElementById('editarEgreso');
    if (editModalExpenses) {
        editModalExpenses.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget;

            const expense_id = button.getAttribute('data-expense-id');
            const expense_date = button.getAttribute('data-expense-date');
            const expense_category = button.getAttribute('data-expense-category');
            const expense_subcategory = button.getAttribute('data-expense-subcategory');
            const expense_amount = button.getAttribute('data-expense-amount');
            const expense_description = button.getAttribute('data-expense-description');

            document.getElementById('edit_expense_id').value = expense_id;
            document.getElementById('edit_expense_date').value = expense_date;
            document.getElementById('edit_categoria').value = expense_category;
            document.getElementById('edit_description').value = (expense_description && expense_description !== "None") ? expense_description : '';
            document.getElementById('edit_monto').value = expense_amount;

            const subcategoriaSelect = document.getElementById('edit_subcategoria');
            subcategoriaSelect.innerHTML = ''; // Limpiar antes de cargar

            if (!expense_category || expense_category === "0") {
                subcategoriaSelect.disabled = true;
                return;
            }

            subcategoriaSelect.disabled = false;

            fetch(`/get_subcategorias/${expense_category}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach((subcat) => {
                        const option = document.createElement('option');
                        option.value = subcat.id;
                        option.textContent = subcat.name;

                        if (subcat.id == expense_subcategory) {
                            option.selected = true;
                        }

                        subcategoriaSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error cargando subcategorías:', error));
        });

        // En caso de que el modal se abra con un valor ya precargado (ej. recarga)
        const initialCategory = document.getElementById('edit_categoria').value;
        const subcategoriaSelect = document.getElementById('edit_subcategoria');
        subcategoriaSelect.disabled = (initialCategory === "0" || initialCategory === "");
    }

    // Evento al cambiar la categoría manualmente en el modal
    const categoriaSelect = document.getElementById('edit_categoria');
    if (categoriaSelect) {
        categoriaSelect.addEventListener('change', function () {
            const categoriaId = this.value;
            const subcategoriaSelect = document.getElementById('edit_subcategoria');

            subcategoriaSelect.innerHTML = '';

            if (categoriaId === "0" || categoriaId === "") {
                subcategoriaSelect.disabled = true;
                return;
            }

            subcategoriaSelect.disabled = false;

            fetch(`/get_subcategorias/${categoriaId}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach((subcat, index) => {
                        const option = document.createElement('option');
                        option.value = subcat.id;
                        option.textContent = subcat.name;

                        if (index === 0) {
                            option.selected = true;
                        }

                        subcategoriaSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error cargando subcategorías:', error));
        });
    }
});
