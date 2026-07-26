/* Interactive Map Preview — Satisfactory, Factorio, Dyson Sphere Program */
/* CSS Grid-based region map with resource details */

const MAP_DATA = {
  satisfactory: {
    name: '⚙️ Satisfactory',
    regions: [
      {
        id: 'grass-fields',
        name: '🌿 Grass Fields',
        color: '#4a7c4f',
        description: 'The recommended starting area. Gentle terrain with abundant basic resources. Perfect for your first factory.',
        resources: [
          { name: 'Iron Ore', amount: 'Abundant', nodes: 18 },
          { name: 'Copper Ore', amount: 'Abundant', nodes: 10 },
          { name: 'Limestone', amount: 'Abundant', nodes: 12 },
          { name: 'Coal', amount: 'Moderate', nodes: 6 },
          { name: 'Raw Quartz', amount: 'Scarce', nodes: 2 },
        ],
        difficulty: 'Easy',
        terrain: 'Gentle hills, wide open spaces',
      },
      {
        id: 'rocky-desert',
        name: '🏜️ Rocky Desert',
        color: '#8b7355',
        description: 'Arid desert starting area with good early access to coal power. Moderate terrain.',
        resources: [
          { name: 'Iron Ore', amount: 'Abundant', nodes: 14 },
          { name: 'Copper Ore', amount: 'Abundant', nodes: 8 },
          { name: 'Limestone', amount: 'Moderate', nodes: 6 },
          { name: 'Coal', amount: 'Abundant', nodes: 8 },
          { name: 'Caterium Ore', amount: 'Moderate', nodes: 3 },
          { name: 'Raw Quartz', amount: 'Scarce', nodes: 1 },
        ],
        difficulty: 'Medium',
        terrain: 'Rocky cliffs, flat desert basins',
      },
      {
        id: 'dune-desert',
        name: '⏳ Dune Desert',
        color: '#c4a35a',
        description: 'Harsh desert with extreme terrain. Rich in oil and late-game resources. Challenging start.',
        resources: [
          { name: 'Iron Ore', amount: 'Moderate', nodes: 6 },
          { name: 'Copper Ore', amount: 'Moderate', nodes: 5 },
          { name: 'Limestone', amount: 'Moderate', nodes: 4 },
          { name: 'Coal', amount: 'Abundant', nodes: 8 },
          { name: 'Crude Oil', amount: 'Abundant', nodes: 6 },
          { name: 'Raw Quartz', amount: 'Abundant', nodes: 4 },
          { name: 'Sulfur', amount: 'Moderate', nodes: 3 },
        ],
        difficulty: 'Hard',
        terrain: 'Massive dunes, canyons, flat oil fields',
      },
      {
        id: 'northern-forest',
        name: '🌲 Northern Forest',
        color: '#2d5a27',
        description: 'Dense forest with rich resource variety. Caterium-rich area for early circuit production.',
        resources: [
          { name: 'Iron Ore', amount: 'Abundant', nodes: 16 },
          { name: 'Copper Ore', amount: 'Abundant', nodes: 10 },
          { name: 'Limestone', amount: 'Moderate', nodes: 5 },
          { name: 'Coal', amount: 'Moderate', nodes: 5 },
          { name: 'Caterium Ore', amount: 'Abundant', nodes: 6 },
          { name: 'Raw Quartz', amount: 'Moderate', nodes: 3 },
        ],
        difficulty: 'Medium',
        terrain: 'Dense forest, steep slopes, waterfalls',
      },
      {
        id: 'blue-crater',
        name: '🔵 Blue Crater',
        color: '#3b5998',
        description: 'A unique crater lake biome. The primary source of nitrogen gas for late-game production.',
        resources: [
          { name: 'Nitrogen Gas', amount: 'Abundant', nodes: 6 },
          { name: 'Sulfur', amount: 'Abundant', nodes: 5 },
          { name: 'Coal', amount: 'Moderate', nodes: 4 },
          { name: 'Raw Quartz', amount: 'Moderate', nodes: 3 },
          { name: 'Iron Ore', amount: 'Moderate', nodes: 4 },
          { name: 'Copper Ore', amount: 'Scarce', nodes: 2 },
        ],
        difficulty: 'Hard',
        terrain: 'Crater lake, vertical cliffs, cave entrances',
      },
      {
        id: 'red-jungle',
        name: '🟥 Red Jungle',
        color: '#8b2252',
        description: 'Dangerous red-tinted jungle. End-game resources including bauxite and uranium.',
        resources: [
          { name: 'Bauxite', amount: 'Abundant', nodes: 6 },
          { name: 'Uranium', amount: 'Abundant', nodes: 4 },
          { name: 'Iron Ore', amount: 'Moderate', nodes: 5 },
          { name: 'Copper Ore', amount: 'Moderate', nodes: 4 },
          { name: 'Limestone', amount: 'Scarce', nodes: 2 },
          { name: 'Crude Oil', amount: 'Moderate', nodes: 3 },
        ],
        difficulty: 'Very Hard',
        terrain: 'Dense jungle, tall cliffs, radioactive zones',
      },
    ],
  },
  factorio: {
    name: '💡 Factorio',
    regions: [
      {
        id: 'spawn-area',
        name: '🏠 Starting Area',
        color: '#6b8e23',
        description: 'The default spawn zone. Generated with standard resource patches. Turtle-safe zone with no biters initially.',
        resources: [
          { name: 'Iron Ore', amount: 'Abundant', nodes: 4 },
          { name: 'Copper Ore', amount: 'Abundant', nodes: 3 },
          { name: 'Coal', amount: 'Moderate', nodes: 2 },
          { name: 'Stone', amount: 'Moderate', nodes: 2 },
          { name: 'Water', amount: 'Unlimited', nodes: 1 },
        ],
        difficulty: 'Easy',
        terrain: 'Flat grassland, lake nearby',
        spawnLayout: 'Iron patches at N/S, Copper at E/W, Coal nearby, Stone further out',
      },
      {
        id: 'iron-north',
        name: '⛏️ Iron Fields (North)',
        color: '#8b7d6b',
        description: 'Large iron ore patches to the north. Recommended for early smelting arrays.',
        resources: [
          { name: 'Iron Ore', amount: 'Very Abundant', nodes: 6 },
          { name: 'Stone', amount: 'Moderate', nodes: 2 },
        ],
        difficulty: 'Easy',
        terrain: 'Open plains',
        spawnLayout: 'Default: 4-6 patches, richness 100%, size 100%, frequency 100%',
      },
      {
        id: 'copper-south',
        name: '🟠 Copper Fields (South)',
        color: '#cd853f',
        description: 'Copper ore patches to the south. Near water for early power.',
        resources: [
          { name: 'Copper Ore', amount: 'Very Abundant', nodes: 5 },
          { name: 'Water', amount: 'Unlimited', nodes: 1 },
        ],
        difficulty: 'Easy',
        terrain: 'Plains with small lake',
        spawnLayout: 'Default: 3-5 patches, richness 100%, size 100%, frequency 100%',
      },
      {
        id: 'coal-east',
        name: '🪨 Coal Veins (East)',
        color: '#555555',
        description: 'Coal deposits to the east. Pairs well with iron for steel and science.',
        resources: [
          { name: 'Coal', amount: 'Abundant', nodes: 3 },
          { name: 'Iron Ore', amount: 'Moderate', nodes: 2 },
        ],
        difficulty: 'Easy',
        terrain: 'Gentle hills',
        spawnLayout: 'Default: 2-3 patches, richness 100%, size 100%, frequency 100%',
      },
      {
        id: 'stone-west',
        name: '🪨 Stone Quarry (West)',
        color: '#a0a0a0',
        description: 'Stone and wall territory. Essential for walls, furnaces, and military science.',
        resources: [
          { name: 'Stone', amount: 'Abundant', nodes: 3 },
          { name: 'Copper Ore', amount: 'Moderate', nodes: 1 },
        ],
        difficulty: 'Easy',
        terrain: 'Rocky outcroppings',
        spawnLayout: 'Default: 2 patches, richness 100%, size 100%, frequency 100%',
      },
      {
        id: 'oil-fields',
        name: '🛢️ Oil Fields (Further Out)',
        color: '#3b3b3b',
        description: 'Crude oil patches beyond the starting area. Required for blue science and beyond.',
        resources: [
          { name: 'Crude Oil', amount: 'Abundant', nodes: 4 },
          { name: 'Uranium', amount: 'Moderate', nodes: 2 },
          { name: 'Coal', amount: 'Moderate', nodes: 2 },
        ],
        difficulty: 'Medium',
        terrain: 'Desert patches between forests',
        spawnLayout: 'Default: 3-5 patches, richness 150%, size 100%, frequency 100%',
        recommendedSettings: {
          'Iron/Copper richness': '100%-200% recommended for longer runs',
          'Coal': '100% default is fine',
          'Stone': '100%-150% for megabase',
          'Crude Oil': '150%-200% for extended play',
          'Uranium size': '150%+ to avoid frequent outposting',
          'Enemy bases': 'Set to Rail World or reduce to 75% for relaxed play',
          'Starting area size': '100% (default) or 150% for more building room',
        },
      },
    ],
  },
  dsp: {
    name: '🌌 Dyson Sphere Program',
    regions: [
      {
        id: 'starting-planet',
        name: '🌍 Starting Planet (Gobi)',
        color: '#4a7c4f',
        description: 'Your starting planet. Temperate world with all basic resources. Good solar efficiency.',
        resources: [
          { name: 'Iron Ore', amount: 'Abundant', nodes: '8 veins' },
          { name: 'Copper Ore', amount: 'Abundant', nodes: '6 veins' },
          { name: 'Stone', amount: 'Moderate', nodes: '5 veins' },
          { name: 'Coal', amount: 'Moderate', nodes: '4 veins' },
          { name: 'Silicon', amount: 'Scarce (from Stone)', nodes: 'Smelt from Stone' },
          { name: 'Titanium Ore', amount: 'None', nodes: '0 (must import)' },
          { name: 'Water', amount: 'Available (pumps)', nodes: '1 ocean' },
          { name: 'Crude Oil', amount: 'Moderate', nodes: '4 seeps' },
        ],
        difficulty: 'Easy',
        terrain: 'Rolling hills, 1 ocean, temperate',
        abundance: {
          abundant: ['Iron', 'Copper', 'Stone'],
          scarce: ['Silicon (smelt from stone)', 'Coal'],
          missing: ['Titanium (need interstellar)', 'Fire Ice', 'Kimberlite', 'Fractal Silicon'],
        },
      },
      {
        id: 'starting-moon',
        name: '🌕 Starting Moon (Luna)',
        color: '#8b8b8b',
        description: 'The tidally locked moon orbiting your starting planet. Rich in titanium and silicon.',
        resources: [
          { name: 'Titanium Ore', amount: 'Abundant', nodes: '6 veins' },
          { name: 'Silicon', amount: 'Abundant', nodes: '5 veins' },
          { name: 'Iron Ore', amount: 'Moderate', nodes: '3 veins' },
          { name: 'Copper Ore', amount: 'Moderate', nodes: '2 veins' },
          { name: 'Stone', amount: 'Scarce', nodes: '2 veins' },
          { name: 'Coal', amount: 'None', nodes: '0' },
          { name: 'Water', amount: 'None', nodes: '0' },
          { name: 'Crude Oil', amount: 'None', nodes: '0' },
        ],
        difficulty: 'Medium',
        terrain: 'Tidally locked, barren, no atmosphere',
        abundance: {
          abundant: ['Titanium', 'Silicon'],
          scarce: ['Iron', 'Copper', 'Stone'],
          missing: ['Coal', 'Water', 'Oil', 'Fire Ice', 'Kimberlite'],
        },
      },
      {
        id: 'desert-planet',
        name: '🏜️ Desert Planet (Mediterranean)',
        color: '#c4a35a',
        description: 'Hot desert world in the starter system. Rich in coal and oil. Good second planet.',
        resources: [
          { name: 'Coal', amount: 'Very Abundant', nodes: '8 veins' },
          { name: 'Crude Oil', amount: 'Abundant', nodes: '5 seeps' },
          { name: 'Iron Ore', amount: 'Moderate', nodes: '4 veins' },
          { name: 'Copper Ore', amount: 'Moderate', nodes: '3 veins' },
          { name: 'Stone', amount: 'Scarce', nodes: '2 veins' },
          { name: 'Silicon', amount: 'Scarce', nodes: '2 veins' },
          { name: 'Water', amount: 'Scarce', nodes: 'Small lakes' },
          { name: 'Fire Ice', amount: 'None', nodes: '0' },
        ],
        difficulty: 'Medium',
        terrain: 'Hot desert, scattered oases',
        abundance: {
          abundant: ['Coal', 'Crude Oil'],
          scarce: ['Iron', 'Copper', 'Stone', 'Silicon', 'Water'],
          missing: ['Titanium', 'Fire Ice', 'Kimberlite', 'Fractal Silicon'],
        },
      },
      {
        id: 'ice-planet',
        name: '❄️ Ice Planet (Glacio)',
        color: '#a8c8d8',
        description: 'Frozen world on the outer edge of the starter system. Contains rare resources.',
        resources: [
          { name: 'Fire Ice', amount: 'Abundant', nodes: '5 veins' },
          { name: 'Kimberlite', amount: 'Moderate', nodes: '3 veins' },
          { name: 'Titanium Ore', amount: 'Moderate', nodes: '3 veins' },
          { name: 'Silicon', amount: 'Moderate', nodes: '3 veins' },
          { name: 'Iron Ore', amount: 'Scarce', nodes: '2 veins' },
          { name: 'Copper Ore', amount: 'Scarce', nodes: '1 vein' },
          { name: 'Water', amount: 'Abundant (ice)', nodes: 'Frozen surface' },
          { name: 'Crude Oil', amount: 'None', nodes: '0' },
        ],
        difficulty: 'Hard',
        terrain: 'Frozen tundra, ice plains',
        abundance: {
          abundant: ['Fire Ice', 'Water (ice)'],
          scarce: ['Titanium', 'Silicon', 'Kimberlite'],
          missing: ['Coal', 'Oil', 'Iron (limited)', 'Copper (limited)'],
        },
      },
    ],
  },
};

/* --- UI Elements --- */
const mapGameSelect = document.getElementById('map-game-select');
const mapGrid = document.getElementById('map-grid');
const mapInfo = document.getElementById('map-region-info');

mapGameSelect.addEventListener('change', () => {
  const game = mapGameSelect.value;
  mapGrid.innerHTML = '';
  if (!game || !MAP_DATA[game]) {
    mapInfo.innerHTML = '<p style="color:#64748b;">Select a game above to see the region map.</p>';
    return;
  }

  const data = MAP_DATA[game];
  let gridHtml = '';

  data.regions.forEach((region, idx) => {
    gridHtml += `
      <div class="map-region-box" data-index="${idx}" data-game="${game}"
           style="background:${region.color}22; border:2px solid ${region.color}; border-radius:10px; padding:16px; cursor:pointer; transition:all 0.2s;"
           onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 20px ${region.color}44';"
           onmouseout="this.style.transform=''; this.style.boxShadow='';"
           onclick="showRegionInfo('${game}', ${idx})">
        <div style="font-weight:700; font-size:1rem; color:${region.color}; margin-bottom:4px;">${region.name}</div>
        <div style="font-size:0.75rem; color:#94a3b8; margin-bottom:6px;">
          ${region.resources.slice(0,3).map(r => r.name).join(' · ')}
          ${region.resources.length > 3 ? ' · +' + (region.resources.length - 3) + ' more' : ''}
        </div>
        <div style="display:flex; gap:6px; flex-wrap:wrap;">
          ${region.resources.slice(0,4).map(r => {
            const colorMap = {
              'Abundant': '#22c55e', 'Very Abundant': '#16a34a',
              'Moderate': '#eab308', 'Scarce': '#f87171', 'None': '#64748b',
              'Unlimited': '#60a5fa', 'Available (pumps)': '#60a5fa',
            };
            return `<span style="font-size:0.65rem; padding:2px 6px; border-radius:4px; background:${(colorMap[r.amount]||'#64748b')}22; color:${colorMap[r.amount]||'#64748b'};">${r.amount}</span>`;
          }).join('')}
        </div>
        <div style="font-size:0.65rem; color:#475569; margin-top:6px;">
          ⭐ ${region.difficulty}
        </div>
      </div>
    `;
  });

  mapGrid.innerHTML = gridHtml;

  /* Show first region by default */
  showRegionInfo(game, 0);
});

function showRegionInfo(game, index) {
  const data = MAP_DATA[game];
  if (!data || !data.regions[index]) return;

  const region = data.regions[index];

  let html = `
    <div style="background:rgba(255,255,255,0.03); border:1px solid ${region.color}44; border-radius:12px; padding:20px;">
      <div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
        <div style="width:12px; height:12px; border-radius:3px; background:${region.color};"></div>
        <h4 style="margin:0; color:${region.color};">${region.name}</h4>
      </div>
      <p style="color:#94a3b8; margin-bottom:16px;">${region.description}</p>

      <h5 style="margin:0 0 8px; color:#e8e6e3;">🗺️ Terrain</h5>
      <p style="color:#64748b; font-size:0.85rem; margin-bottom:16px;">${region.terrain}</p>

      <h5 style="margin:0 0 8px; color:#e8e6e3;">⛏️ Resources</h5>
      <table style="width:100%; border-collapse:collapse; margin-bottom:16px;">
        <thead>
          <tr style="border-bottom:1px solid rgba(255,255,255,0.1);">
            <th style="text-align:left; padding:6px 8px; font-size:0.75rem; color:#64748b;">Resource</th>
            <th style="text-align:center; padding:6px 8px; font-size:0.75rem; color:#64748b;">Amount</th>
            <th style="text-align:right; padding:6px 8px; font-size:0.75rem; color:#64748b;">Nodes</th>
          </tr>
        </thead>
        <tbody>
          ${region.resources.map(r => {
            const colorMap = {
              'Abundant': '#22c55e', 'Very Abundant': '#16a34a',
              'Moderate': '#eab308', 'Scarce': '#f87171', 'None': '#64748b',
              'Unlimited': '#60a5fa', 'Available (pumps)': '#60a5fa',
            };
            return `<tr style="border-bottom:1px solid rgba(255,255,255,0.03);">
              <td style="padding:6px 8px; font-size:0.85rem;">${r.name}</td>
              <td style="text-align:center; padding:6px 8px; font-size:0.8rem; color:${colorMap[r.amount] || '#64748b'}; font-weight:600;">${r.amount}</td>
              <td style="text-align:right; padding:6px 8px; font-size:0.8rem; color:#94a3b8;">${typeof r.nodes === 'number' ? r.nodes : r.nodes}</td>
            </tr>`;
          }).join('')}
        </tbody>
      </table>
  `;

  /* Extra info: Factorio recommended settings */
  if (region.spawnLayout) {
    html += `<h5 style="margin:0 0 8px; color:#e8e6e3;">📐 Spawn Layout</h5>
      <p style="color:#64748b; font-size:0.85rem;">${region.spawnLayout}</p>`;
  }

  if (region.recommendedSettings) {
    html += `<h5 style="margin:0 0 8px; color:#e8e6e3;">⚙️ Recommended Starting Settings</h5>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">`;
    for (const [setting, value] of Object.entries(region.recommendedSettings)) {
      html += `<div style="padding:6px 10px; background:rgba(255,255,255,0.03); border-radius:6px;">
        <div style="font-size:0.75rem; color:#eab308;">${setting}</div>
        <div style="font-size:0.72rem; color:#64748b;">${value}</div>
      </div>`;
    }
    html += `</div>`;
  }

  /* DSP abundance info */
  if (region.abundance) {
    html += `<h5 style="margin:12px 0 8px; color:#e8e6e3;">📊 Resource Abundance</h5>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
        <div style="padding:8px 12px; background:rgba(34,197,94,0.08); border:1px solid rgba(34,197,94,0.2); border-radius:8px;">
          <div style="font-size:0.7rem; color:#22c55e; font-weight:600; margin-bottom:4px;">✅ Abundant</div>
          <div style="font-size:0.78rem; color:#94a3b8;">${region.abundance.abundant.join(' · ')}</div>
        </div>
        <div style="padding:8px 12px; background:rgba(234,179,8,0.08); border:1px solid rgba(234,179,8,0.2); border-radius:8px;">
          <div style="font-size:0.7rem; color:#eab308; font-weight:600; margin-bottom:4px;">⚠️ Scarce</div>
          <div style="font-size:0.78rem; color:#94a3b8;">${region.abundance.scarce.join(' · ')}</div>
        </div>
        <div style="padding:8px 12px; background:rgba(248,113,113,0.08); border:1px solid rgba(248,113,113,0.2); border-radius:8px; grid-column:1/-1;">
          <div style="font-size:0.7rem; color:#f87171; font-weight:600; margin-bottom:4px;">❌ Missing</div>
          <div style="font-size:0.78rem; color:#94a3b8;">${region.abundance.missing.join(' · ')}</div>
        </div>
      </div>`;
  }

  html += `</div>`;
  mapInfo.innerHTML = html;
}
