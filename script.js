let currentIndex = 0;
const photos = document.querySelectorAll('.foto');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

function updateGallery() {
    // Esconde todas as fotos
    photos.forEach(photo => photo.style.display = 'none');
    // Exibe a foto atual
    photos[currentIndex].style.display = 'block';
}

// Inicializa o mural com a primeira foto
updateGallery();

// Função para ir para a foto anterior
prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = photos.length - 1; // Vai para a última imagem
    }
    updateGallery();
});

// Função para ir para a próxima foto
nextButton.addEventListener('click', () => {
    if (currentIndex < photos.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Vai para a primeira imagem
    }
    updateGallery();
});
