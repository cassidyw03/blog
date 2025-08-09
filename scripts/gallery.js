fetch('data/photo.json')
  .then(response => response.json())
  .then(photoData => {
    const container = document.getElementById('photo-grid');
    const filter = document.getElementById('year-filter');

    // Extract unique years from photo dates
    const years = [...new Set(photoData
      .map(photo => photo.date ? photo.date.split('-')[0] : null)
      .filter(year => year))].sort();

    // Populate the dropdown with years
    years.forEach(year => {
      const option = document.createElement('option');
      option.value = year;
      option.textContent = year;
      filter.appendChild(option);
    });

    // Function to display photos filtered by year
    function displayPhotos(selectedYear = '') {
      container.innerHTML = '';
      let filtered = selectedYear
        ? photoData.filter(photo => photo.date && photo.date.startsWith(selectedYear))
        : photoData;

      filtered.forEach(photo => {
        const img = document.createElement('img');
        img.src = photo.src;
        img.alt = photo.alt || '';
        img.title = photo.date || '';
        img.style.width = '100%';
        img.style.borderRadius = '8px';
        img.style.objectFit = 'cover';
        container.appendChild(img);
      });
    }

    // Initial display (all photos)
    displayPhotos();

    // Listen for filter changes
    filter.addEventListener('change', () => {
      displayPhotos(filter.value);
    });
  })
  .catch(err => {
    console.error('Error loading photos:', err);
  });

