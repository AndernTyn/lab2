document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', function(event) {
        if (event.target.id === 'calculatePrice') {
            getPrice();
        } else if (event.target.id === 'placeOrder') {
            pay();
        }
    });
});

function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(response) {
        return response.json();  
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб.`;
    })
    .catch(function(error) {
        console.error('Ошибка при обращении к API:', error);
    });
}

function pay() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const cardNumber = document.getElementById('cardNumber').value;
    const cvv = document.getElementById('cvv').value;

    console.log('Payment details:', { drink, milk, sugar, cardNumber, cvv }); // Debugging

    const obj = {
        "method": "pay",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            cardNumber: cardNumber,
            cvv: cvv
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(response) {
        return response.json();  
    })
    .then(function(data) {
        console.log('Payment response:', data); // Debugging

        if (data.success) {
            alert(`Списание успешно: ${data.message}`);
        } else {
            alert(`Ошибка: ${data.error}`);
        }
    })
    .catch(function(error) {
        console.error('Ошибка при обращении к API:', error);
    });
}