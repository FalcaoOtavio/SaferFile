<script>
var dropArea = document.body;

dropArea.addEventListener('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
    dropArea.style.backgroundColor = '#f0f0f0';
});

dropArea.addEventListener('drop', function(e) {
    e.preventDefault();
    e.stopPropagation();
    var files = e.dataTransfer.files;
    var formData = new FormData();
    formData.append('file', files[0]);

    fetch('/', {
        method: 'POST',
        body: formData
    }).then(response => response.text()).then(result => {
        alert(result);
    });
});
</script>