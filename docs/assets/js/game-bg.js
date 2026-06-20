// game-guide.club - Game background detection
// Applies per-game CSS class for background images + color overlays
(function() {
  const path = window.location.pathname;
  let bgClass = '';
  
  if (path.startsWith('/wukong/') || path.startsWith('/wukong')) {
    bgClass = 'wukong-bg';
  } else if (path.startsWith('/genshin/') || path.startsWith('/genshin')) {
    bgClass = 'genshin-bg';
  } else if (path.startsWith('/diablo4/') || path.startsWith('/diablo4')) {
    bgClass = 'diablo4-bg';
  } else if (path.startsWith('/gta/') || path.startsWith('/gta')) {
    bgClass = 'gta-bg';
  }
  
  if (bgClass) {
    document.body.classList.add(bgClass);
  }
})();
