function createColoredParagraph() {
    const text = prompt("Enter text:");
    const color = prompt("Enter text color:");
    const bgColor = prompt("Enter background color:");
    
    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    paragraph.style.color = color;
    paragraph.style.backgroundColor = bgColor;
    
    document.body.appendChild(paragraph);
}

createColoredParagraph();
