// paint/static/paint/js/paint.js
document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('paintCanvas');
    const ctx = canvas.getContext('2d');
    let painting = false;

    function startPosition(e) {
        painting = true;
        draw(e);
    }

    function endPosition() {
        painting = false;
        ctx.beginPath();
        // Set image data in the hidden form field
        document.getElementById('imageDataField').value = canvas.toDataURL();
    }

    function draw(e) {
        if (!painting) return;

        ctx.lineWidth = 5;
        ctx.lineCap = 'round';
        ctx.strokeStyle = 'black';

        ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    }

    canvas.addEventListener('mousedown', startPosition);
    canvas.addEventListener('mouseup', endPosition);
    canvas.addEventListener('mousemove', draw);
});
