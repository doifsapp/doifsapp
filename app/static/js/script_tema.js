let tamanhoFonte = 16;

document.getElementById("aumentarFonte").addEventListener("click", () => {
    tamanhoFonte += 2;
    document.body.style.fontSize = `${tamanhoFonte}px`;
});

document.getElementById("diminuirFonte").addEventListener("click", () => {
    if (tamanhoFonte > 10) {
        tamanhoFonte -= 2;
        document.body.style.fontSize = `${tamanhoFonte}px`;
    }
});

document.getElementById("alternarTema").addEventListener("click", () => {
    document.body.classList.toggle("tema-escuro");

    // Seleciona todos os elementos com a classe "box-title" e altera a cor
    document.querySelectorAll(".box-title").forEach((element) => {
        if (document.body.classList.contains("tema-escuro")) {
            element.style.color = "white";  // Cor branca no tema escuro
        } else {
            element.style.color = "";  // Volta ao padrão do CSS
        }
    });
});
