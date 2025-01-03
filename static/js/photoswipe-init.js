class PhotoSwipeInitializer {
    constructor() {
        this.lightbox = new PhotoSwipeLightbox({
            gallery: '#photo-grid',
            children: '.photo-link',
            pswpModule: PhotoSwipe,
            paddingFn: () => ({ top: 30, bottom: 30, left: 70, right: 70 }),
            bgOpacity: 0.85,
            showHideAnimationType: 'zoom'
        });

        // Add custom buttons to the UI
        this.lightbox.on('uiRegister', () => {
            this.lightbox.pswp.ui.registerElement({
                name: 'info-button',
                order: 9,
                isButton: true,
                html: '<i class="bi bi-info-circle"></i>',
                onClick: (event, el) => {
                    const currentSlide = this.lightbox.pswp.currSlide;
                    const photoId = currentSlide.data.element.dataset.photoId;
                    this.showPhotoInfo(photoId);
                }
            });
        });

        this.lightbox.init();
        this.infoOverlay = null;
    }

    async showPhotoInfo(photoId) {
        try {
            const response = await fetch(`/photo/${photoId}/info`);
            const photoInfo = await response.json();

            // Create or update info overlay
            if (!this.infoOverlay) {
                this.infoOverlay = document.createElement('div');
                this.infoOverlay.className = 'pswp-info-overlay';
                this.lightbox.pswp.element.appendChild(this.infoOverlay);
            }

            // Format the date strings
            const dateTaken = new Date(photoInfo.dates.taken).toLocaleDateString();
            const dateUploaded = new Date(photoInfo.dates.posted * 1000).toLocaleDateString();

            // Generate EXIF information HTML
            const exifInfo = photoInfo.exif.reduce((html, item) => {
                if (['FNumber', 'FocalLength', 'ExposureTime', 'Model', 'Flash'].includes(item.tag)) {
                    return html + `<div><strong>${item.label}:</strong> ${item.raw._content}</div>`;
                }
                return html;
            }, '');

            this.infoOverlay.innerHTML = `
                <div class="info-content">
                    <button class="close-info">&times;</button>
                    <h3>${photoInfo.title._content}</h3>
                    ${photoInfo.description._content ? `<p class="description">${photoInfo.description._content}</p>` : ''}
                    <div class="info-grid">
                        <div><strong>Date Taken:</strong> ${dateTaken}</div>
                        <div><strong>Date Uploaded:</strong> ${dateUploaded}</div>
                        <div><strong>Views:</strong> ${photoInfo.views}</div>
                        <div><strong>Favorites:</strong> ${photoInfo.favorites || 0}</div>
                        <div><strong>Comments:</strong> ${photoInfo.comments._content}</div>
                    </div>
                    <div class="exif-info">
                        ${exifInfo}
                    </div>
                    <a href="/photo/${photoInfo.id}" 
                       class="flickr-link" 
                       target="_blank"
                       rel="noopener noreferrer">
                        View full exif data
                    </a>
                </div>
            `;

            // Add close button event listener
            this.infoOverlay.querySelector('.close-info').addEventListener('click', () => {
                this.infoOverlay.classList.remove('visible');
            });

            // Show the overlay with animation
            requestAnimationFrame(() => {
                this.infoOverlay.classList.add('visible');
            });
        } catch (error) {
            console.error('Error fetching photo info:', error);
        }
    }

    static init() {
        return new PhotoSwipeInitializer();
    }
}

document.addEventListener('DOMContentLoaded', PhotoSwipeInitializer.init);