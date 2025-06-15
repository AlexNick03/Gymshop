let page = 0;
let loading = false;
let hasMore = true;

function loadOrders() {
    if (loading || !hasMore) return;
    loading = true;
    document.getElementById("loading").style.display = "block";

    fetch(`/order_history_api/?page=${page + 1}`)
        .then(response => {
            if (!response.ok) throw new Error("Răspuns invalid");
            return response.text();
        })
        .then(data => {
            if (data.trim() === "") {
                hasMore = false;
                document.getElementById("loading").innerText = "Toate comenzile au fost încărcate.";
                return;
            }

            document.getElementById("order-list").insertAdjacentHTML("beforeend", data);
            page++;
        })
        .catch(error => {
            console.error("Eroare la încărcarea comenzilor:", error);
        })
        .finally(() => {
            loading = false;
        });
}

window.addEventListener("scroll", function () {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 300) {
        loadOrders();
    }
});

window.addEventListener("DOMContentLoaded", function () {
    loadOrders(); // încărcare inițială
});