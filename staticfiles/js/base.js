// Auto dismiss flash messages
setTimeout(function() {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        message.style.transition = 'opacity 0.5s';
        message.style.opacity = '0';
        setTimeout(() => message.remove(), 500);
    });
 }, 3000);
 
 // Confirm before delete
 document.querySelectorAll('.delete-link').forEach(function(link) {
    link.addEventListener('click', function(e) {
        if (!confirm('Are you sure you want to delete this?')) {
            e.preventDefault();
        }
    });
 });