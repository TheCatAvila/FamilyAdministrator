const editModal = document.getElementById('editSubcategory');

editModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;

    const id = button.getAttribute('data-subcategory-id');
    const name = button.getAttribute('data-subcategory-name');
    const budget = button.getAttribute('data-subcategory-budget');

    // Set values in the modal
    document.getElementById('edit_subcategory_id').value = id;
    document.getElementById('edit_subcategory_name').value = name;
    document.getElementById('edit_subcategory_budget').value = budget;
});