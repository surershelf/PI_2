document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        const nome = document.getElementById("nome").value;
        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;
        const confirmarSenha = document.getElementById("confirmarSenha").value;

        if (!nome || !email || !senha || !confirmarSenha) {
            event.preventDefault(); // Impede o envio do formulário se algum campo estiver em branco
            alert("Todos os campos são obrigatórios");
        } else if (senha !== confirmarSenha) {
            event.preventDefault(); // Impede o envio do formulário se as senhas não coincidirem
            alert("As senhas não coincidem");
        }
    });
});