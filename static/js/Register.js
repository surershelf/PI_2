document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".button button").addEventListener("click", async function () {
        const nome = document.getElementById("nome").value;
        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;
        const confirmarSenha = document.getElementById("confirmarSenha").value;
    
        if (senha !== confirmarSenha) {
            alert("As senhas não correspondem.");
            return;
        }
    
        try {
            const response = await fetch("http://localhost:8000/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: nome,
                    password: senha,
                    email: email,
                }),
            });
    
            if (response.ok) {
                alert("Registro bem-sucedido.");
            } else {
                const data = await response.json();
                alert("Erro no registro: " + data.error);
            }
        } catch (error) {
            console.error("Erro:", error);
        }
    })
});