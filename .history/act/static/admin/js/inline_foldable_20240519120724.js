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

        const descriptionWrapper = document.createElement('div');
        descriptionWrapper.className = 'description-wrapper';
        descriptionWrapper.style.display = 'none';
        field.parentNode.insertBefore(descriptionWrapper, field);
        descriptionWrapper.appendChild(field);

        wrapper.insertBefore(toggleLink, descriptionWrapper);
    });
});
