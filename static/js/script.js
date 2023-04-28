async function rollDice(die) {
    die.style.animation = 'shake 1s';
    const delay = (t) => new Promise((resolve) => setTimeout(resolve, t));
    await delay(1000);
    die.style.animation = '';
}

document.querySelectorAll('.die-button').forEach((button) => {
    button.addEventListener('click', async (e) => {
        const numberPicked = button.getAttribute('data-value');
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ numberPicked }),
        });

        const results = await response.json();
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';

        let total = 0;

        for (let i = 0; i < results.length; i++) {
            const dieResult = document.createElement('div');
            dieResult.className = 'dice';
            resultsContainer.appendChild(dieResult);

            await rollDice(dieResult);

            dieResult.style.backgroundImage = `url('/static/images/${results[i]}.png')`;

            total += results[i];
        }

        const totalElement = document.getElementById('total');
        totalElement.textContent = `You rolled a ${total}!`;
    });
});