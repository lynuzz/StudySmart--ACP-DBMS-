document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('custom-confirm-modal');
    const deleteButtons = document.querySelectorAll('.custom-delete-btn');
    const cancelButton = document.getElementById('modal-cancel');
    const okButton = document.getElementById('modal-ok');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
  
            event.preventDefault(); 
            
            const deleteUrl = this.getAttribute('data-delete-url');

            okButton.setAttribute('href', deleteUrl);

            modal.style.display = 'block';
        });
    });

    cancelButton.addEventListener('click', function() {
        modal.style.display = 'none';
        okButton.setAttribute('href', '#');
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            okButton.setAttribute('href', '#'); 
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('custom-confirm-modal');
    const deleteButtons = document.querySelectorAll('.custom-delete-btn'); 
    const cancelButton = document.getElementById('modal-cancel');
    const okButton = document.getElementById('modal-ok'); 

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
        
            event.preventDefault(); 
            
            const deleteUrl = this.getAttribute('data-delete-url');

            okButton.setAttribute('href', deleteUrl);

            modal.style.display = 'block'; 
        });
    });

    cancelButton.addEventListener('click', function() {
        modal.style.display = 'none';
        okButton.setAttribute('href', '#'); 
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            okButton.setAttribute('href', '#'); 
        }
    });
});