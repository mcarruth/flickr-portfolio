class PhotoMap {
    constructor(mapElement, apiKey) {
        this.map = new google.maps.Map(mapElement, {
            zoom: 2,
            center: { lat: 0, lng: 0 },
            styles: this.getDarkThemeStyles()
        });
        
        this.markers = [];
        this.markerClusterer = null;
        this.infoWindow = new google.maps.InfoWindow();
        
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
        this.markers = photos.map(photo => {
            const position = {
                lat: parseFloat(photo.latitude),
                lng: parseFloat(photo.longitude)
            };

            const marker = new google.maps.Marker({
                position: position,
                map: this.map,
                title: photo.title
            });

            marker.addListener('click', () => {
                this.infoWindow.setContent(`
                    <div class="photo-info-window">
                        <img src="${photo.url_sq}" alt="${photo.title}">
                        <h5>${photo.title}</h5>
                        <a href="/photo/${photo.id}" class="btn btn-sm btn-primary">
                            View Details
                        </a>
                    </div>
                `);
                this.infoWindow.open(this.map, marker);
            });

            return marker;
        });

        // Initialize MarkerClusterer
        this.markerClusterer = new markerClusterer.MarkerClusterer({
            map: this.map,
            markers: this.markers
        });
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

// Initialize map when Google Maps API is loaded
function initMap() {
    const mapElement = document.getElementById('map');
    if (mapElement) {
        new PhotoMap(mapElement, mapElement.dataset.apiKey);
    }
}
