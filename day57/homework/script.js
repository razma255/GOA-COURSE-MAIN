document.addEventListener("DOMContentLoaded", function() {
    const box = document.getElementById('box');
    const infoBtn = document.getElementById('infoBtn');

    infoBtn.addEventListener('click', function() {
        const privilege = prompt("Enter privilege:");
        const color = prompt("Enter color (e.g., #ff0000):");
        const width = parseInt(prompt("Enter width (in pixels):"));
        const height = parseInt(prompt("Enter height (in pixels):"));
        const text = prompt("Enter text:");
        if (!isNaN(width) && !isNaN(height)) {
            box.style.width = width + 'px';
            box.style.height = height + 'px';
        }
        if (color) {
            box.style.backgroundColor = color;
        }
        if (text) {
            box.innerText = text;
        }
    });
});
