/* Production Ratio Calculator — Satisfactory, Factorio, Dyson Sphere Program */

const DATA = {
  satisfactory: {
    machine: { name: 'Constructor / Assembler / Manufacturer', speed: 1.0, unit: '/ min' },
    items: {
      'Iron Plate':    { time: 6,  out: 2,  in: { 'Iron Ingot': 3 } },
      'Iron Rod':      { time: 4,  out: 1,  in: { 'Iron Ingot': 1 } },
      'Screw':         { time: 6,  out: 4,  in: { 'Iron Rod': 1 } },
      'Reinforced Plate': { time: 12, out: 1, in: { 'Iron Plate': 6, 'Screw': 12 } },
      'Modular Frame': { time: 60, out: 1, in: { 'Reinforced Plate': 3, 'Iron Rod': 12 } },
      'Rotor':         { time: 12, out: 1, in: { 'Iron Rod': 5, 'Screw': 25 } },
      'Cable':         { time: 4,  out: 2, in: { 'Wire': 2 } },
      'Wire':          { time: 2,  out: 3, in: { 'Copper Ingot': 1 } },
      'Concrete':      { time: 4,  out: 1, in: { 'Limestone': 3 } },
      'Steel Beam':    { time: 4,  out: 1, in: { 'Steel Ingot': 4 } },
      'Steel Pipe':    { time: 6,  out: 1, in: { 'Steel Ingot': 3 } },
      'Motor':         { time: 12, out: 1, in: { 'Rotor': 2, 'Stator': 2 } },
      'Stator':        { time: 8,  out: 1, in: { 'Steel Pipe': 3, 'Wire': 8 } },
      'Circuit Board': { time: 8,  out: 1, in: { 'Copper Sheet': 2, 'Plastic': 4 } },
      'Copper Sheet':  { time: 6,  out: 1, in: { 'Copper Ingot': 2 } },
      'Plastic':       { time: 6,  out: 2, in: { 'Crude Oil': 3 } },
      'Rubber':        { time: 6,  out: 2, in: { 'Crude Oil': 3 } },
      'Heavy Frame':   { time: 30, out: 1, in: { 'Modular Frame': 5, 'Steel Pipe': 15, 'Concrete': 10 } },
      'Computer':      { time: 24, out: 1, in: { 'Circuit Board': 10, 'Cable': 18, 'Plastic': 18 } },
      'Supercomputer': { time: 32, out: 1, in: { 'Computer': 2, 'Circuit Board': 14, 'Wire': 28 } },
      'Iron Ingot':    { time: 2,  out: 1, in: { 'Iron Ore': 1 } },
      'Copper Ingot':  { time: 2,  out: 1, in: { 'Copper Ore': 1 } },
      'Steel Ingot':   { time: 4,  out: 3, in: { 'Iron Ore': 3, 'Coal': 3 } },
    }
  },
  factorio: {
    machine: { name: 'Assembling Machine 3', speed: 1.25, unit: '/ s' },
    items: {
      'Iron Gear Wheel':     { time: 0.5, out: 1, in: { 'Iron Plate': 2 } },
      'Iron Plate':          { time: 3.2, out: 1, in: { 'Iron Ore': 1 } },
      'Copper Plate':        { time: 3.2, out: 1, in: { 'Copper Ore': 1 } },
      'Steel Plate':         { time: 16,  out: 1, in: { 'Iron Plate': 5 } },
      'Copper Cable':        { time: 0.5, out: 2, in: { 'Copper Plate': 1 } },
      'Electronic Circuit':  { time: 0.5, out: 1, in: { 'Iron Plate': 1, 'Copper Cable': 3 } },
      'Advanced Circuit':    { time: 8,   out: 1, in: { 'Copper Cable': 4, 'Electronic Circuit': 2, 'Plastic Bar': 2 } },
      'Processing Unit':     { time: 10,  out: 1, in: { 'Advanced Circuit': 2, 'Electronic Circuit': 20, 'Sulfuric Acid': 1 } },
      'Engine Unit':         { time: 10,  out: 1, in: { 'Iron Gear Wheel': 1, 'Steel Plate': 1, 'Pipe': 2 } },
      'Pipe':                { time: 0.5, out: 1, in: { 'Iron Plate': 1 } },
      'Electric Engine Unit':{ time: 10,  out: 1, in: { 'Engine Unit': 1, 'Electronic Circuit': 1, 'Lubricant': 1.25 } },
      'Plastic Bar':         { time: 1,   out: 2, in: { 'Coal': 1, 'Petroleum Gas': 1.25 } },
      'Sulfuric Acid':       { time: 1,   out: 5, in: { 'Iron Plate': 0.5, 'Sulfur': 0.5, 'Water': 1 } },
      'Battery':             { time: 4,   out: 1, in: { 'Iron Plate': 1, 'Copper Plate': 1, 'Sulfuric Acid': 2 } },
      'Red Science':         { time: 5,   out: 1, in: { 'Iron Gear Wheel': 1, 'Copper Plate': 1 } },
      'Green Science':       { time: 6,   out: 1, in: { 'Inserters': 1, 'Transport Belt': 1 } },
      'Gray Science':        { time: 10,  out: 1, in: { 'Iron Gear Wheel': 1, 'Stone Wall': 1, 'Grenade': 1 } },
      'Blue Science':        { time: 24,  out: 1, in: { 'Advanced Circuit': 3, 'Engine Unit': 1, 'Sulfuric Acid': 0.5 } },
      'Purple Science':      { time: 21,  out: 1, in: { 'Advanced Circuit': 3, 'Electric Engine Unit': 2 } },
      'Yellow Science':      { time: 21,  out: 1, in: { 'Advanced Circuit': 3, 'Processing Unit': 1 } },
      'Rocket Part':         { time: 10,  out: 1, in: { 'Low Density Structure': 10, 'Rocket Fuel': 10, 'Rocket Control Unit': 10 } },
    }
  },
  dsp: {
    machine: { name: 'Assembling Machine Mk.II', speed: 1.0, unit: '/ s' },
    items: {
      'Iron Ingot':        { time: 1, out: 1, in: { 'Iron Ore': 1 } },
      'Copper Ingot':      { time: 1, out: 1, in: { 'Copper Ore': 1 } },
      'Magnet':            { time: 1.5, out: 1, in: { 'Iron Ore': 1 } },
      'Stone Brick':       { time: 1.5, out: 1, in: { 'Stone': 1 } },
      'Circuit Board':     { time: 2, out: 1, in: { 'Copper Ingot': 2, 'Iron Ingot': 1 } },
      'Prism':             { time: 2, out: 1, in: { 'Glass': 3 } },
      'Glass':             { time: 2, out: 2, in: { 'Stone': 2 } },
      'Steel':             { time: 3, out: 1, in: { 'Iron Ingot': 3 } },
      'Gear':              { time: 1, out: 1, in: { 'Iron Ingot': 1 } },
      'Magnetic Coil':     { time: 2, out: 1, in: { 'Copper Ingot': 2, 'Magnet': 2 } },
      'Electric Motor':    { time: 3, out: 1, in: { 'Iron Ingot': 2, 'Gear': 1, 'Magnetic Coil': 1 } },
      'Processor':         { time: 3, out: 1, in: { 'Circuit Board': 2, 'Silicon': 2 } },
      'Titanium Ingot':    { time: 2, out: 1, in: { 'Titanium Ore': 1 } },
      'High-Purity Silicon': { time: 2, out: 1, in: { 'Silicon': 2 } },
      'Quantum Chip':      { time: 6, out: 1, in: { 'Processor': 2, 'Plane Filter': 2, 'Graviton Lens': 1 } },
      'Graviton Lens':     { time: 8, out: 1, in: { 'Diamond': 4, 'Strange Matter': 1 } },
      'Solar Sail':        { time: 4, out: 2, in: { 'Graphene': 1, 'Photon Combiner': 1 } },
      'Frame Material':    { time: 6, out: 1, in: { 'High-Purity Silicon': 1, 'Carbon Nanotube': 1, 'Titanium Alloy': 1 } },
      'Titanium Alloy':    { time: 8, out: 1, in: { 'Titanium Ingot': 4, 'Steel': 4, 'Sulfuric Acid': 4 } },
      'Dyson Sphere Component': { time: 12, out: 1, in: { 'Frame Material': 3, 'Solar Sail': 3, 'Processor': 3 } },
    }
  }
};

/* --- UI Logic --- */
const gameSelect = document.getElementById('game-select');
const recipeSelect = document.getElementById('recipe-select');
const targetRate = document.getElementById('target-rate');
const rateUnit = document.getElementById('rate-unit');
const calcBtn = document.getElementById('calc-btn');
const results = document.getElementById('results');
const summary = document.getElementById('result-summary');
const chainOutput = document.getElementById('chain-output');

gameSelect.addEventListener('change', () => {
  const game = gameSelect.value;
  recipeSelect.innerHTML = '<option value="">— Select an item —</option>';
  if (!game || !DATA[game]) return;
  const data = DATA[game];
  Object.keys(data.items).sort().forEach(name => {
    const opt = document.createElement('option');
    opt.value = name;
    opt.textContent = name;
    recipeSelect.appendChild(opt);
  });
  rateUnit.textContent = data.machine.unit;
  results.style.display = 'none';
});

calcBtn.addEventListener('click', calculate);

function calculate() {
  const game = gameSelect.value;
  const item = recipeSelect.value;
  const rate = parseFloat(targetRate.value);

  if (!game || !item || !rate || rate <= 0) {
    results.style.display = 'block';
    summary.innerHTML = '<span style="color:#f87171;">⚠️ Please select a game and item, and enter a valid target rate.</span>';
    chainOutput.innerHTML = '';
    return;
  }

  const data = DATA[game];
  const recipe = data.items[item];
  if (!recipe) {
    summary.innerHTML = `<span style="color:#f87171;">⚠️ Recipe data not found for "${item}".</span>`;
    return;
  }

  const adjustedSpeed = (game === 'factorio' || game === 'dsp') ? data.machine.speed : 1.0;
  const unitsPerMachine = (recipe.out / recipe.time) * adjustedSpeed;
  const machinesNeeded = rate / unitsPerMachine;
  const inputRates = {};

  for (const [mat, qty] of Object.entries(recipe.in)) {
    inputRates[mat] = (qty / recipe.time) * adjustedSpeed * machinesNeeded;
  }

  /* Display results */
  results.style.display = 'block';

  let html = `
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px;">
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Machines needed</div>
        <div style="font-size:1.3rem; font-weight:700; color:#f97316;">${machinesNeeded.toFixed(2)}</div>
        <div style="font-size:0.7rem; color:#475569;">${data.machine.name}</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Per machine output</div>
        <div style="font-size:1.3rem; font-weight:700; color:#22c55e;">${unitsPerMachine.toFixed(2)}</div>
        <div style="font-size:0.7rem; color:#475569;">${data.machine.unit}</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Recipe time</div>
        <div style="font-size:1.3rem; font-weight:700; color:#60a5fa;">${recipe.time}s</div>
        <div style="font-size:0.7rem; color:#475569;">${recipe.out}× per craft</div>
      </div>
    </div>
  `;
  summary.innerHTML = html;

  /* Chain table */
  let chainHtml = '<table style="width:100%; border-collapse:collapse; margin-top:8px;">';
  chainHtml += '<thead><tr style="border-bottom:1px solid rgba(255,255,255,0.1);"><th style="text-align:left; padding:8px;">Input Material</th><th style="text-align:right; padding:8px;">Required Rate</th><th style="text-align:right; padding:8px;">Unit</th></tr></thead><tbody>';

  for (const [mat, matRate] of Object.entries(inputRates).sort()) {
    chainHtml += `<tr style="border-bottom:1px solid rgba(255,255,255,0.03);">
      <td style="padding:8px;">${mat}</td>
      <td style="text-align:right; padding:8px; font-weight:600; color:#eab308;">${matRate.toFixed(2)}</td>
      <td style="text-align:right; padding:8px; color:#64748b;">${data.machine.unit}</td>
    </tr>`;
  }

  chainHtml += '<tr style="border-bottom:1px solid rgba(255,255,255,0.03);"><td colspan="3" style="padding:8px; font-size:0.8rem; color:#64748b;">→ Target: ' + rate + ' ' + item + ' ' + data.machine.unit + '</td></tr>';
  chainHtml += '</tbody></table>';
  chainOutput.innerHTML = chainHtml;
}
