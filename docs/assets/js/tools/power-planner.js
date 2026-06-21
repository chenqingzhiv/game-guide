/* Power Grid Planner — Satisfactory, Factorio, Dyson Sphere Program */

const POWER_DATA = {
  satisfactory: {
    sources: {
      'Coal Generator':         { output: 75,  unit: 'MW', fuel: 'Coal',       fuelRate: 15,   fuelUnit: '/ min', byproduct: null },
      'Fuel Generator':         { output: 150, unit: 'MW', fuel: 'Fuel',       fuelRate: 12,   fuelUnit: '/ min', byproduct: null },
      'Turbofuel Generator':    { output: 150, unit: 'MW', fuel: 'Turbo Fuel', fuelRate: 4.5,  fuelUnit: '/ min', byproduct: null },
      'Nuclear Power Plant':    { output: 2500,unit: 'MW', fuel: 'Uranium Fuel Rod', fuelRate: 0.2, fuelUnit: '/ min', byproduct: 'Nuclear Waste' },
      'Geothermal Generator':   { output: 200, unit: 'MW', fuel: null,         fuelRate: 0,    fuelUnit: '',       byproduct: null },
    }
  },
  factorio: {
    sources: {
      'Steam Engine (Coal)':    { output: 0.9, unit: 'MW', fuel: 'Coal', fuelRate: 0.1, fuelUnit: '/ s', byproduct: null },
      'Steam Engine (Solid Fuel)': { output: 0.9, unit: 'MW', fuel: 'Solid Fuel', fuelRate: 0.03, fuelUnit: '/ s', byproduct: null },
      'Steam Engine (Rocket Fuel)': { output: 1.1, unit: 'MW', fuel: 'Rocket Fuel', fuelRate: 0.01, fuelUnit: '/ s', byproduct: null },
      'Steam Turbine (Nuclear)': { output: 5.8,  unit: 'MW', fuel: 'Uranium Fuel Cell', fuelRate: 0.005, fuelUnit: '/ s', byproduct: 'Used Fuel Cell' },
      'Solar Panel':            { output: 0.06, unit: 'MW', fuel: null, fuelRate: 0, fuelUnit: '', byproduct: null },
    }
  },
  dsp: {
    sources: {
      'Thermal Power Station':  { output: 2.16, unit: 'MW', fuel: 'Coal', fuelRate: 0.5, fuelUnit: '/ s', byproduct: null },
      'Thermal Power Station':  { output: 2.16, unit: 'MW', fuel: 'Oil', fuelRate: 0.25, fuelUnit: '/ s', byproduct: null },
      'Thermal Power Station':  { output: 2.16, unit: 'MW', fuel: 'Hydrogen', fuelRate: 0.2, fuelUnit: '/ s', byproduct: null },
      'Mini Fusion Power Plant':{ output: 50,  unit: 'MW', fuel: 'Deuteron Fuel Rod', fuelRate: 0.025, fuelUnit: '/ s', byproduct: null },
      'Artificial Sun':         { output: 125, unit: 'MW', fuel: 'Antimatter Fuel Rod', fuelRate: 0.01, fuelUnit: '/ s', byproduct: null },
      'Dyson Swarm (Solar Sail)': { output: 0.15, unit: 'MW', fuel: 'Solar Sail', fuelRate: 0.01, fuelUnit: '/ s', byproduct: null },
    }
  }
};

/* Flatten DSP sources into named options */
const DSP_SOURCES = [
  { id: 'dsp-coal',        name: 'Thermal (Coal)',        output: 2.16, fuel: 'Coal', fuelRate: 0.5,  fuelUnit: '/ s', byproduct: null },
  { id: 'dsp-oil',         name: 'Thermal (Oil)',         output: 2.16, fuel: 'Crude Oil', fuelRate: 0.25, fuelUnit: '/ s', byproduct: null },
  { id: 'dsp-hydrogen',    name: 'Thermal (Hydrogen)',    output: 2.16, fuel: 'Hydrogen', fuelRate: 0.2,  fuelUnit: '/ s', byproduct: null },
  { id: 'dsp-fusion',      name: 'Mini Fusion',           output: 50,   fuel: 'Deuteron Fuel Rod', fuelRate: 0.025, fuelUnit: '/ s', byproduct: null },
  { id: 'dsp-sun',         name: 'Artificial Sun',        output: 125,  fuel: 'Antimatter Fuel Rod', fuelRate: 0.01, fuelUnit: '/ s', byproduct: null },
  { id: 'dsp-sail',        name: 'Dyson Swarm (Sail)',    output: 0.15, fuel: 'Solar Sail', fuelRate: 0.01, fuelUnit: '/ s', byproduct: null },
];

const gameSelect = document.getElementById('game-select');
const powerSelect = document.getElementById('power-select');
const targetMw = document.getElementById('target-mw');
const calcBtn = document.getElementById('calc-btn');
const results = document.getElementById('results');
const summary = document.getElementById('result-summary');
const fuelOutput = document.getElementById('fuel-output');

gameSelect.addEventListener('change', () => {
  const game = gameSelect.value;
  powerSelect.innerHTML = '<option value="">— Select a source —</option>';
  if (!game) return;

  if (game === 'dsp') {
    DSP_SOURCES.forEach(s => {
      const opt = document.createElement('option');
      opt.value = s.id;
      opt.textContent = s.name;
      powerSelect.appendChild(opt);
    });
  } else {
    const sources = POWER_DATA[game].sources;
    Object.entries(sources).forEach(([name, data]) => {
      const opt = document.createElement('option');
      opt.value = name;
      opt.textContent = `${name} (${data.output} MW)`;
      powerSelect.appendChild(opt);
    });
  }
  results.style.display = 'none';
});

calcBtn.addEventListener('click', calculate);

function getSourceData(game, value) {
  if (game === 'dsp') return DSP_SOURCES.find(s => s.id === value);
  const src = POWER_DATA[game];
  if (!src) return null;
  for (const [k, v] of Object.entries(src.sources)) {
    if (k === value) return { ...v, id: k, name: k };
  }
  return null;
}

function calculate() {
  const game = gameSelect.value;
  const srcVal = powerSelect.value;
  const target = parseFloat(targetMw.value);

  if (!game || !srcVal || !target || target <= 0) {
    results.style.display = 'block';
    summary.innerHTML = '<span style="color:#f87171;">⚠️ Select a game, power source, and enter a valid target.</span>';
    fuelOutput.innerHTML = '';
    return;
  }

  const source = getSourceData(game, srcVal);
  if (!source) {
    summary.innerHTML = '<span style="color:#f87171;">⚠️ Source data not found.</span>';
    return;
  }

  const units = Math.ceil(target / source.output);
  const actualOutput = units * source.output;
  const fuelRateTotal = source.fuelRate * units;

  results.style.display = 'block';

  let html = `
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px;">
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Generators needed</div>
        <div style="font-size:1.3rem; font-weight:700; color:#f97316;">${units}</div>
        <div style="font-size:0.7rem; color:#475569;">${source.name}</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Total output</div>
        <div style="font-size:1.3rem; font-weight:700; color:#22c55e;">${actualOutput.toFixed(1)}</div>
        <div style="font-size:0.7rem; color:#475569;">MW (target: ${target} MW)</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Per generator</div>
        <div style="font-size:1.3rem; font-weight:700; color:#60a5fa;">${source.output}</div>
        <div style="font-size:0.7rem; color:#475569;">MW each</div>
      </div>
    </div>
  `;
  summary.innerHTML = html;

  if (source.fuel) {
    let fuelHtml = '<table style="width:100%; border-collapse:collapse; margin-top:8px;">';
    fuelHtml += '<thead><tr style="border-bottom:1px solid rgba(255,255,255,0.1);"><th style="text-align:left; padding:8px;">Material</th><th style="text-align:right; padding:8px;">Per Generator</th><th style="text-align:right; padding:8px;">Total</th></tr></thead><tbody>';
    fuelHtml += `<tr><td style="padding:8px;">${source.fuel}</td>`;
    fuelHtml += `<td style="text-align:right; padding:8px; color:#eab308; font-weight:600;">${source.fuelRate} ${source.fuelUnit}</td>`;
    fuelHtml += `<td style="text-align:right; padding:8px; color:#eab308; font-weight:600;">${fuelRateTotal.toFixed(2)} ${source.fuelUnit}</td>`;
    fuelHtml += '</tr>';
    if (source.byproduct) {
      const byprodRate = source.fuelRate * units;
      fuelHtml += `<tr><td style="padding:8px; color:#64748b;">↳ Byproduct: ${source.byproduct}</td>`;
      fuelHtml += `<td style="text-align:right; padding:8px; color:#64748b;">${source.fuelRate} ${source.fuelUnit}</td>`;
      fuelHtml += `<td style="text-align:right; padding:8px; color:#64748b;">${byprodRate.toFixed(2)} ${source.fuelUnit}</td></tr>`;
    }
    fuelHtml += '</tbody></table>';
    fuelOutput.innerHTML = fuelHtml;
  } else {
    fuelOutput.innerHTML = '<p style="color:#64748b;">✨ No fuel required — this is a renewable source.</p>';
  }
}
