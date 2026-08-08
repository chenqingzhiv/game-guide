// game-guide.club - Per-game background detection
// Applies per-game CSS class for background images + color overlays
(function() {
  const path = window.location.pathname;
  let bgClass = '';

  if (path.startsWith('/satisfactory/')) {
    bgClass = 'factory-bg';
  } else if (path.startsWith('/factorio/')) {
    bgClass = 'factory-bg';
  } else if (path.startsWith('/dyson/')) {
    bgClass = 'space-bg';
  } else if (path.startsWith('/timberborn/')) {
    bgClass = 'nature-bg';
  } else if (path.startsWith('/shapez2/')) {
    bgClass = 'abstract-bg';
  }

  if (bgClass) {
    document.body.classList.add(bgClass);
  }
})();
