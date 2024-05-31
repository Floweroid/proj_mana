document.addEventListener('DOMContentLoaded', function () {
    const descriptionFields = document.querySelectorAll('.description');

    descriptionFields.forEach(function (field) {
        const wrapper = field.closest('.form-row');
        const toggleLink = document.createElement('a');
        toggleLink.href = '#';
        toggleLink.innerText = 'Toggle Description';
        toggleLink.style.display = 'block';
        toggleLink.style.marginBottom = '5px';

        toggleLink.addEventListener('click', function (e) {
            e.preventDefault();
            if (field.style.display === 'none' || field.style.display === '') {
                field.style.display = 'block';
            } else {
                field.style.display = 'none';
            }
        });

        wrapper.insertBefore(toggleLink, field);
        field.style.display = 'none';  // Hide by default
    });
});

