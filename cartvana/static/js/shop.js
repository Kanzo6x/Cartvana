async function showProducts(categoryId) {
    try {
        const response = await fetch(`/api/products/${categoryId}`);
        const data = await response.json();
        
        const productsContainer = document.getElementById('products-container');
        productsContainer.innerHTML = ''; // Clear existing products

        data.products.forEach(product => {
            const productCard = `
                <div class="product-card">
                    <div class="product-image" style="background-image: url('data:image/jpeg;base64,${product.image}')"></div>
                    <h3>${product.name}</h3>
                    <p class="price">$${product.price.toFixed(2)}</p>
                    <button class="show-product-btn" onclick="window.location.href='/product/${product.id}'">Show</button>
                </div>
            `;
            productsContainer.innerHTML += productCard;
        });
        
        // Show products section
        document.getElementById('products-section').style.display = 'block';
        
        // Update active category
        document.querySelectorAll('.category-card').forEach(card => {
            card.classList.remove('active');
        });
        document.querySelector(`[data-category="${categoryId}"]`).classList.add('active');

    } catch (error) {
        console.error('Error fetching products:', error);
    }
}
