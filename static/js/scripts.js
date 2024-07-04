document.getElementById('detectarBtn').addEventListener('click', function() {
    let texto = document.getElementById('texto').value;
    
    fetch('/detectar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ texto: texto })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sentimiento').innerText = data.sentimiento;
        let consejosList = document.getElementById('consejos');
        consejosList.innerHTML = '';
        data.consejos.forEach(consejo => {
            let listItem = document.createElement('li');
            listItem.textContent = consejo;
            consejosList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
});
