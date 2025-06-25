document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        let errorContainer = document.getElementById("message-container");
        if (errorContainer) {
            errorContainer.classList.add("hidden"); // Aplică fade-out
            setTimeout(() => {
                errorContainer.style.display = "none"; // Ascunde complet după fade-out
            }, 1000); // Timpul trebuie să fie egal cu CSS transition (1s)
        }
    }, 3000); // Așteaptă 3 secunde înainte să înceapă fade-out
});

