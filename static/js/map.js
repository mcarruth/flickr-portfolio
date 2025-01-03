class PhotoMap {
    constructor(mapElement) {
        this.map = L.map('map').setView([0, 0], 2);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(this.map);
        
        this.loadGeotaggedPhotos();
    }

    async loadGeotaggedPhotos() {
        try {
            const response = await fetch('/geotagged-photos');
            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            this.addPhotosToMap(data.photos.photo);
        } catch (error) {
            console.error('Error loading geotagged photos:', error);
        }
    }

    addPhotosToMap(photos) {
        photos.forEach(photo => {
            if (photo.latitude && photo.longitude) {
                const marker = L.marker([photo.latitude, photo.longitude], {title: photo.title}).addTo(this.map);
                marker.bindPopup(this.createPopupContent(photo)).openPopup();
            }
        });
    }

    createPopupContent(photo) {
        return `
            <a href="/photo/${photo.id}">
                <img src="${photo.url_sq}" />
            </a>
        `;
    }


    getDarkThemeStyles() {
        return [
            { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
            // ... more dark theme styles
        ];
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const mapElement = document.getElementById('map');
    if (mapElement) {
        new PhotoMap(mapElement);
    }
});