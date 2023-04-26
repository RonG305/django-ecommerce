const toggler = document.querySelector('.toggler')
const sidebar = document.getElementById('sidebar')
const productCard = document.querySelectorAll('.best-deals .deal')
const addToCart = document.getElementById('add-to-cart')

toggler.addEventListener('click', () => {
    sidebar.classList.toggle('show')
})

productCard.addEventListener('mouseover', () => {
    productCard.classList.toggle('add-to-cart')
})


