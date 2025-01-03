class PortfolioGrid {
    constructor() {
        this.page = 1;
        this.loading = false;
        this.container = document.getElementById('photo-grid');
        this.loadingIndicator = document.getElementById('loading-indicator');

        // Initialize infinite scroll
        this.setupInfiniteScroll();

        // Load initial photos
        this.loadMorePhotos();
    }

    setupInfiniteScroll() {
        window.addEventListener('scroll', () => {
            if (this.loading) return;

            const scrollPos = window.innerHeight + window.scrollY;
            const pageBottom = document.documentElement.offsetHeight - 800;

            if (scrollPos >= pageBottom) {
                this.loadMorePhotos();
            }
        });
    }

    async loadMorePhotos() {
        this.loading = true;
        this.loadingIndicator.classList.remove('d-none');

        try {
            const queryParams = new URLSearchParams({
                page: this.page
            });

            const response = await fetch(`/photos?${queryParams.toString()}`);
            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            this.renderPhotos(data.photos.photo);
            this.page++;
        } catch (error) {
            console.error('Error loading photos:', error);
            this.showError('Failed to load photos. Please try again later.');
        } finally {
            this.loading = false;
            this.loadingIndicator.classList.add('d-none');
        }
    }

    renderPhotos(photos) {
        photos.forEach(photo => {
            const photoCard = document.createElement('div');
            photoCard.className = 'col-md-6 col-lg-6 mb-6';

            // Get the largest available image URL for lightbox
            const largeImageUrl = photo.url_l || photo.url_m;
            const thumbnailUrl = largeImageUrl;

            photoCard.innerHTML = `
                <div class="card h-100 border-0">
                    <a href="${largeImageUrl}" 
                       class="photo-link" 
                       data-pswp-width="${photo.width_l || photo.width_m}"
                       data-pswp-height="${photo.height_l || photo.height_m}"
                       data-photo-id="${photo.id}"
                       target="_blank">
                        <img src="${thumbnailUrl}" 
                             class="card-img" 
                             alt="${photo.title}"
                             loading="lazy">
                    </a>
                </div>
            `;
            this.container.appendChild(photoCard);
        });
    }

    showError(message) {
        const alert = document.createElement('div');
        alert.className = 'alert alert-danger';
        alert.textContent = message;
        this.container.prepend(alert);
    }
}

// Initialize portfolio when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PortfolioGrid();
});