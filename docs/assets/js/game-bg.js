// game-guide.club - Game background detection
(function() {
  const path = window.location.pathname;
  let bgClass = '';
  
  if (path.startsWith('/wukong/') || path === '/wukong/') {
    bgClass = 'wukong-bg';
  } else if (path.startsWith('/genshin/') || path === '/genshin/') {
    bgClass = 'genshin-bg';
  } else if (path.startsWith('/diablo4/') || path === '/diablo4/') {
    bgClass = 'diablo4-bg';
  } else if (path.startsWith('/gta/') || path === '/gta/') {
    bgClass = 'gta-bg';
  }
  
  if (bgClass) {
    document.body.classList.add(bgClass);
  }
})();
