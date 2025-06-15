document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("search-input");
  const resultsBox = document.getElementById("search-results");

  let preventHide = false;

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

  // Când dai click pe un rezultat, NU ascunde imediat dropdown-ul
  resultsBox.addEventListener("mousedown", function (e) {
    preventHide = true;
  });

  input.addEventListener("blur", function () {
    setTimeout(() => {
      if (!preventHide) {
        resultsBox.innerHTML = "";
        resultsBox.style.display = "none";
      }
      preventHide = false;
    }, 100);
  });
});