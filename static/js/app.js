document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            if (alert && alert.parentNode) {
                alert.classList.add('fade');
                alert.style.display = 'none';
            }
        }, 3000);
    });
});
