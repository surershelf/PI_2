const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirm-password");
const passwordMismatchMessage = document.getElementById("password-mismatch-message");

confirmPasswordInput.addEventListener("input", function() {
    if (passwordInput.value !== confirmPasswordInput.value) {
        passwordMismatchMessage.textContent = "As senhas não coincidem.";
    } else {
        passwordMismatchMessage.textContent = "";
    }
});
