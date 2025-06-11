document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("search-input");
const resultsBox = document.getElementById("search-results");

input.addEventListener("input", function () {
    const query = this.value.trim();

    if (query === "") {
        resultsBox.innerHTML = "";
        resultsBox.style.display = "none";
        return;
    }

    fetch(`/search_api/?q=${encodeURIComponent(query)}`)
        .then(response => response.text())
        .then(data => {
            resultsBox.innerHTML = data;
            resultsBox.style.display = "block";
        });
});

// ascunde dropdown-ul când pierzi focusul
input.addEventListener("blur", function () {
    setTimeout(() => {
        resultsBox.innerHTML = "";
        resultsBox.style.display = "none";
    }, 100); // delay ca să poți da click pe link
});  
});
