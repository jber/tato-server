const secret = document.getElementById('secret');
secret.addEventListener('mouseover', () => { 
    secret.textContent = 'check the source';
});
secret.addEventListener('mouseout', () => { 
    secret.textContent = 'purpx gur fbhepr';
});

function randomGifGenerator() {
    const gifs = [
        "gifs/elmo.gif",
        "gifs/elmotato.gif",
        "gifs/tatointensify.gif",
        "gifs/potatointensify.gif",
        "gifs/tatowiggle.gif",
        "gifs/elmobob.gif",
        "gifs/fries.gif",
        "gifs/friesagain.gif",
        "gifs/elmodance.gif"
    ];
    const randomGif = gifs[Math.floor(Math.random() * gifs.length)];
    document.getElementById("randomGif").src = randomGif;
}

randomGifGenerator();
setInterval(randomGifGenerator, 3000);

