let cart = [];
let total = 0;

function addToCart(productName, price) {
    cart.push({ productName, price });
    total += price;

    updateCart();
}

function updateCart() {
    const cartContent = document.getElementById("cart-content");
    cartContent.innerHTML = ""; // Limpa o conteúdo anterior

    cart.forEach(item => {
        const itemDiv = document.createElement("div");
        itemDiv.classList.add("cart-item");
        itemDiv.innerHTML = `${item.productName} - R$ ${item.price.toFixed(2)}`;
        cartContent.appendChild(itemDiv);
    });

    document.getElementById("total-price").textContent = total.toFixed(2);
}

function clearCart() {
    cart = [];
    total = 0;
    updateCart();
}
