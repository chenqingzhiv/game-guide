/* Valheim Boss Tracker — tracks defeated status via localStorage */

const BOSSES = ['eikthyr', 'elder', 'bonemass', 'moder', 'yagluth', 'queen'];
const STORAGE_KEY = 'gameguide_boss_tracker';

let defeated = loadDefeated();

function loadDefeated() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : {};
  } catch { return {}; }
}

function saveDefeated() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(defeated)); } catch {}
}

function updateUI() {
  document.querySelectorAll('.toggle-boss').forEach(btn => {
    const boss = btn.dataset.boss;
    const card = btn.closest('.boss-card');
    const statusEl = card.querySelector('.boss-status');
    const isDefeated = defeated[boss];

    statusEl.textContent = isDefeated ? '✅ Defeated' : '⚔️ Undefeated';
    statusEl.style.background = isDefeated ? 'rgba(34,197,94,0.15)' : 'rgba(255,255,255,0.04)';
    statusEl.style.color = isDefeated ? '#22c55e' : '#64748b';

    if (isDefeated) {
      card.style.borderColor = 'rgba(34,197,94,0.2)';
      card.style.background = 'rgba(34,197,94,0.03)';
    } else {
      card.style.borderColor = 'rgba(255,255,255,0.06)';
      card.style.background = 'rgba(255,255,255,0.03)';
    }
  });

  const count = BOSSES.filter(b => defeated[b]).length;
  const pct = (count / BOSSES.length) * 100;
  document.getElementById('progress-fill').style.width = pct + '%';
  document.getElementById('progress-text').textContent = `${count} / ${BOSSES.length} defeated`;
}

document.addEventListener('click', e => {
  const btn = e.target.closest('.toggle-boss');
  if (!btn) return;
  const boss = btn.dataset.boss;
  defeated[boss] = !defeated[boss];
  saveDefeated();
  updateUI();
});

updateUI();
