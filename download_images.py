import os
import requests
from urllib.parse import urlparse

# Create images directory if it doesn't exist
if not os.path.exists('static/images'):
    os.makedirs('static/images')

# List of AI-themed background images
images = {
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485',  # AI/Tech abstract
    'features-bg.jpg': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31',  # Circuit board
    'products-hero.jpg': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2',  # Technology workspace
    'products-bg.jpg': 'https://images.unsplash.com/photo-1518432031352-d6fc5c10da5a',  # Abstract tech
    'process-bg.jpg': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa',  # Digital abstract
    'values-bg.jpg': 'https://images.unsplash.com/photo-1510915361894-db8b60106cb1',  # Tech network
    'team-bg.jpg': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5',  # Digital matrix
    'vision-bg.jpg': 'https://images.unsplash.com/photo-1607705703571-c5a8695f18f6',  # Futuristic lights
    'ai-background.jpg': 'https://images.unsplash.com/photo-1517373116369-9bdb8cdc9f62',  # AI visualization
    'cta-bg.jpg': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b'  # Tech abstract
}

def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join('static/images', filename), 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {filename}")
        else:
            print(f"Failed to download {filename}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")

# Download all images
for filename, url in images.items():
    if filename == 'ai-background.jpg':  # Only download the failed image
        download_image(url, filename) 