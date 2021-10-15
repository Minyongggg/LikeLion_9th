const getRandomHexaColor = () => {
    const hexa = '0123456789abcdef';

    let randhexa = '#';
    for (let i = 0; i < 6; i++){
        randhexa += hexa[Math.floor(Math.random() * 16)]
    }

    return randhexa;
};

setInterval(() => {
    document.querySelector('body').style.backgroundColor = 
        getRandomHexaColor();
}, 100);