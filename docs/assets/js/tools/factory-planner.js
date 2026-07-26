/* Factory Planner / Production Line Visualizer — Satisfactory, Factorio, DSP, Timberborn */
/* End-to-end production chain with vertical step-by-step display */

const FACTORY_DATA = {
  satisfactory: {
    name: '⚙️ Satisfactory',
    unit: '/ min',
    items: {
      'Supercomputer': {
        final: 'Supercomputer',
        steps: [
          { step: 1, label: 'Raw ore processing', outputs: { 'Iron Ingot': '1 Iron Ore → 1 Ingot (2s)', 'Copper Ingot': '1 Copper Ore → 1 Ingot (2s)' } },
          { step: 2, label: 'Basic components', outputs: { 'Wire': '1 Copper Ingot → 4 Wire (2s)', 'Cable': '2 Wire → 2 Cable (4s)', 'Copper Sheet': '2 Copper Ingot → 1 Sheet (6s)' } },
          { step: 3, label: 'Mid-tier components', outputs: { 'Circuit Board': '2 Copper Sheet + 4 Plastic → 1 Board (8s)' } },
          { step: 4, label: 'High-tier components', outputs: { 'Computer': '10 Circuit Board + 18 Cable + 18 Plastic → 1 Computer (24s)' } },
          { step: 5, label: 'Final assembly', outputs: { 'Supercomputer': '2 Computer + 14 Circuit Board + 28 Wire + 28 Plastic → 1 Supercomputer (32s)' } },
        ],
        rawRecipe: { 'Supercomputer': { time: 32, out: 1, in: { 'Computer': 2, 'Circuit Board': 14, 'Wire': 28, 'Plastic': 28 } } },
      },
      'Turbo Motor': {
        final: 'Turbo Motor',
        steps: [
          { step: 1, label: 'Raw processing', outputs: { 'Iron Ingot': '1 Iron Ore → 1 Ingot (2s)', 'Copper Ingot': '1 Copper Ore → 1 Ingot (2s)', 'Steel Ingot': '3 Iron Ore + 3 Coal → 3 Ingot (4s)' } },
          { step: 2, label: 'Basic parts', outputs: { 'Iron Rod': '1 Iron Ingot → 1 Rod (4s)', 'Screw': '1 Iron Rod → 4 Screw (6s)', 'Wire': '1 Copper Ingot → 4 Wire (2s)', 'Steel Pipe': '3 Steel Ingot → 1 Pipe (6s)' } },
          { step: 3, label: 'Rotors & Stators', outputs: { 'Rotor': '5 Iron Rod + 25 Screw → 1 Rotor (12s)', 'Stator': '3 Steel Pipe + 8 Wire → 1 Stator (8s)' } },
          { step: 4, label: 'Motors', outputs: { 'Motor': '2 Rotor + 2 Stator → 1 Motor (12s)' } },
          { step: 5, label: 'Radio & cooling', outputs: { 'Radio Control Unit': '1 Circuit Board + 2 Crystal Oscillator → 1 RCU (8s)', 'Cooling System': '5 Motor + 5 Heat Sink + 5 Rubber → 1 Cooling System (12s)' } },
          { step: 6, label: 'Final: Turbo Motor', outputs: { 'Turbo Motor': '3 Cooling System + 3 RCU + 6 Motor + 9 Rubber → 1 Turbo Motor (32s)' } },
        ],
        rawRecipe: { 'Turbo Motor': { time: 32, out: 1, in: { 'Cooling System': 3, 'Radio Control Unit': 3, 'Motor': 6, 'Rubber': 9 } } },
      },
      'Assembly Director System': {
        final: 'Assembly Director System',
        steps: [
          { step: 1, label: 'Raw processing', outputs: { 'Iron Ingot': '1 Iron Ore → 1 Ingot (2s)', 'Copper Ingot': '1 Copper Ore → 1 Ingot (2s)' } },
          { step: 2, label: 'Basic components', outputs: { 'Wire': '1 Copper Ingot → 4 Wire (2s)', 'Cable': '2 Wire → 2 Cable (4s)', 'Copper Sheet': '2 Copper Ingot → 1 Sheet (6s)' } },
          { step: 3, label: 'Mid assembly', outputs: { 'Circuit Board': '2 Copper Sheet + 4 Plastic → 1 Board (8s)', 'AI Limiter': '5 Circuit Board + 2 Copper Sheet → 1 AI Limiter (12s)' } },
          { step: 4, label: 'High assembly', outputs: { 'Computer': '10 Circuit Board + 18 Cable + 18 Plastic → 1 Computer (24s)', 'High-Speed Connector': '4 Cable + 4 Circuit Board → 1 Connector (8s)' } },
          { step: 5, label: 'Final: ADS', outputs: { 'Assembly Director System': '1 Computer + 2 AI Limiter + 2 High-Speed Connector + 12 Plastic → 1 ADS (48s)' } },
        ],
        rawRecipe: { 'Assembly Director System': { time: 48, out: 1, in: { 'Computer': 1, 'AI Limiter': 2, 'High-Speed Connector': 2, 'Plastic': 12 } } },
      },
      'Magnetic Field Generator': {
        final: 'Magnetic Field Generator',
        steps: [
          { step: 1, label: 'Raw & smelting', outputs: { 'Iron Ingot': '1 Ore → 1 (2s)', 'Copper Ingot': '1 Ore → 1 (2s)', 'Steel Ingot': '3 Ore + 3 Coal → 3 (4s)' } },
          { step: 2, label: 'Basic parts', outputs: { 'Wire': '1 Cu Ingot → 4 (2s)', 'Cable': '2 Wire → 2 (4s)', 'Steel Pipe': '3 Steel → 1 Pipe (6s)', 'Steel Beam': '4 Steel → 1 Beam (4s)' } },
          { step: 3, label: 'Mid parts', outputs: { 'Stator': '3 Steel Pipe + 8 Wire → 1 Stator (8s)', 'Motor': '2 Rotor + 2 Stator → 1 Motor (12s)' } },
          { step: 4, label: 'Electromagnet', outputs: { 'Electromagnetic Control Rod': '2 Stator + 1 AI Limiter + 1 Cable → 1 Rod (12s)' } },
          { step: 5, label: 'Final: MFG', outputs: { 'Magnetic Field Generator': '2 Electromagnetic Control Rod + 5 Motor + 8 Wire + 4 Rubber → 1 MFG (30s)' } },
        ],
        rawRecipe: { 'Magnetic Field Generator': { time: 30, out: 1, in: { 'Electromagnetic Control Rod': 2, 'Motor': 5, 'Wire': 8, 'Rubber': 4 } } },
      },
      'Thermal Propulsion Rocket': {
        final: 'Thermal Propulsion Rocket',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Steel Ingot': '3 Iron Ore + 3 Coal → 3 (4s)', 'Aluminum Ingot': '4 Bauxite + 4 Silica → 4 (2s)' } },
          { step: 2, label: 'Basic assembly', outputs: { 'Steel Pipe': '3 Steel → 1 (6s)', 'Steel Beam': '4 Steel → 1 (4s)', 'Alclad Sheet': '3 Al + 2 Copper → 1 Sheet (6s)' } },
          { step: 3, label: 'Mid assembly', outputs: { 'Motor': '2 Rotor + 2 Stator → 1 (12s)', 'Heat Sink': '3 Alclad + 2 Copper → 1 Heat Sink (8s)' } },
          { step: 4, label: 'Fuel & frame', outputs: { 'Turbo Fuel': '4 Fuel + 3 Compacted Coal → 5 (8s)', 'Fused Frame': '2 Heavy Frame + 2 Alclad → 1 (30s)' } },
          { step: 5, label: 'Final: TPR', outputs: { 'Thermal Propulsion Rocket': '3 Fused Frame + 3 Turbo Motor + 5 RCU + 6 Cooling System → 1 TPR (60s)' } },
        ],
        rawRecipe: { 'Thermal Propulsion Rocket': { time: 60, out: 1, in: { 'Fused Modular Frame': 3, 'Turbo Motor': 3, 'Radio Control Unit': 5, 'Cooling System': 6 } } },
      },
      'Automated Wiring': {
        final: 'Automated Wiring',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Ingot': '1 Ore → 1 (2s)', 'Copper Ingot': '1 Ore → 1 (2s)', 'Steel Ingot': '3 Ore + 3 Coal → 3 (4s)' } },
          { step: 2, label: 'Basic parts', outputs: { 'Wire': '1 Cu → 4 (2s)', 'Cable': '2 Wire → 2 (4s)', 'Iron Rod': '1 Fe → 1 (4s)', 'Steel Pipe': '3 Steel → 1 (6s)' } },
          { step: 3, label: 'Assembly', outputs: { 'Stator': '3 Steel Pipe + 8 Wire → 1 (8s)', 'Screw': '1 Iron Rod → 4 (6s)', 'Rotor': '5 Iron Rod + 25 Screw → 1 Rotor (12s)' } },
          { step: 4, label: 'Final: Automated Wiring', outputs: { 'Automated Wiring': '3 Stator + 2 Cable + 40 Wire + 10 Screw → 1 Automated Wiring (24s)' } },
        ],
        rawRecipe: { 'Automated Wiring': { time: 24, out: 1, in: { 'Stator': 3, 'Cable': 2, 'Wire': 40, 'Screw': 10 } } },
      },
      'Modular Engine': {
        final: 'Modular Engine',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Ingot': '1 → 1 (2s)', 'Copper Ingot': '1 → 1 (2s)', 'Steel Ingot': '3+3 → 3 (4s)' } },
          { step: 2, label: 'Basic parts', outputs: { 'Iron Rod': '1 Fe → 1 (4s)', 'Screw': '1 Rod → 4 (6s)', 'Wire': '1 Cu → 4 (2s)', 'Rubber': '3 Oil → 2 (6s)', 'Steel Pipe': '3 Steel → 1 Pipe (6s)' } },
          { step: 3, label: 'Medium assembly', outputs: { 'Rotor': '5 Rod + 25 Screw → 1 (12s)', 'Stator': '3 Pipe + 8 Wire → 1 (8s)' } },
          { step: 4, label: 'High assembly', outputs: { 'Motor': '2 Rotor + 2 Stator → 1 (12s)', 'Rubber': '3 Crude Oil → 2 (6s)' } },
          { step: 5, label: 'Final: Modular Engine', outputs: { 'Modular Engine': '2 Motor + 2 Rubber + 16 Iron Rod + 8 Screw → 1 Modular Engine (30s)' } },
        ],
        rawRecipe: { 'Modular Engine': { time: 30, out: 1, in: { 'Motor': 2, 'Rubber': 2, 'Iron Rod': 16, 'Screw': 8 } } },
      },
      'Adaptive Control Unit': {
        final: 'Adaptive Control Unit',
        steps: [
          { step: 1, label: 'Smelting & refining', outputs: { 'Copper Ingot': '1 → 1 (2s)', 'Iron Ingot': '1 → 1 (2s)', 'Plastic': '3 Oil → 2 (6s)', 'Silica': '3 Quartz → 5 (8s)' } },
          { step: 2, label: 'Basic parts', outputs: { 'Wire': '1 Cu → 4 (2s)', 'Cable': '2 Wire → 2 (4s)', 'Copper Sheet': '2 Cu → 1 (6s)' } },
          { step: 3, label: 'Circuitry', outputs: { 'Circuit Board': '2 Sheet + 4 Plastic → 1 (8s)', 'Crystal Oscillator': '3 Quartz Crystal + 4 Cable → 1 (12s)' } },
          { step: 4, label: 'Computing', outputs: { 'Computer': '10 Board + 18 Cable + 18 Plastic → 1 (24s)', 'AI Limiter': '5 Board + 2 Sheet → 1 (12s)' } },
          { step: 5, label: 'Final: ACU', outputs: { 'Adaptive Control Unit': '1 Computer + 4 AI Limiter + 20 Wire + 12 Plastic → 1 ACU (24s)' } },
        ],
        rawRecipe: { 'Adaptive Control Unit': { time: 24, out: 1, in: { 'Computer': 1, 'AI Limiter': 4, 'Wire': 20, 'Plastic': 12 } } },
      },
    },
    rawMats: {
      'Iron Ore': { raw: true }, 'Copper Ore': { raw: true }, 'Limestone': { raw: true },
      'Coal': { raw: true }, 'Crude Oil': { raw: true }, 'Raw Quartz': { raw: true },
      'Bauxite': { raw: true }, 'Sulfur': { raw: true }, 'Nitrogen Gas': { raw: true },
      'Caterium Ore': { raw: true }, 'Uranium': { raw: true },
    }
  },
  factorio: {
    name: '💡 Factorio',
    unit: '/ s',
    items: {
      'Science Pack 1 (Red)': {
        final: 'Science Pack 1',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 Iron Ore → 1 Plate (3.2s)', 'Copper Plate': '1 Copper Ore → 1 Plate (3.2s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Iron Plate → 1 Gear (0.5s)' } },
          { step: 3, label: 'Final: Red Science', outputs: { 'Science Pack 1': '1 Iron Gear Wheel + 1 Copper Plate → 1 Red (5s)' } },
        ],
        rawRecipe: { 'Science Pack 1': { time: 5, out: 1, in: { 'Iron Gear Wheel': 1, 'Copper Plate': 1 } } },
      },
      'Science Pack 2 (Green)': {
        final: 'Science Pack 2',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 Ore → 1 (3.2s)', 'Copper Plate': '1 Ore → 1 (3.2s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Iron → 1 (0.5s)', 'Copper Cable': '1 Copper → 2 (0.5s)' } },
          { step: 3, label: 'Sub-assemblies', outputs: { 'Transport Belt': '1 Gear + 1 Iron → 2 Belt (0.5s)', 'Inserter': '1 Gear + 1 Circuit + 1 Iron → 1 (0.5s)', 'Electronic Circuit': '1 Iron + 3 Cable → 1 (0.5s)' } },
          { step: 4, label: 'Final: Green Science', outputs: { 'Science Pack 2': '1 Transport Belt + 1 Inserter → 1 Green (6s)' } },
        ],
        rawRecipe: { 'Science Pack 2': { time: 6, out: 1, in: { 'Transport Belt': 1, 'Inserter': 1 } } },
      },
      'Military Science (Gray)': {
        final: 'Military Science',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 Ore → 1 (3.2s)', 'Copper Plate': '1 Ore → 1 (3.2s)', 'Stone Brick': '2 Stone → 1 (3.2s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Iron → 1 (0.5s)', 'Copper Cable': '1 Copper → 2 (0.5s)', 'Stone Wall': '5 Stone Brick → 1 (6s)', 'Pipe': '1 Iron Plate → 1 (0.5s)' } },
          { step: 3, label: 'Ammo', outputs: { 'Grenade': '5 Coal + 1 Iron + 2 Pipe → 1 (8s)', 'Piercing Magazine': '4 Steel + 1 Copper + 1 Firearm → 1 (5s)' } },
          { step: 4, label: 'Final: Gray Science', outputs: { 'Military Science': '1 Gear + 1 Wall + 1 Grenade → 1 Gray (10s)' } },
        ],
        rawRecipe: { 'Military Science': { time: 10, out: 1, in: { 'Iron Gear Wheel': 1, 'Stone Wall': 1, 'Grenade': 1 } } },
      },
      'Production Science (Purple)': {
        final: 'Production Science',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 Ore → 1 (3.2s)', 'Copper Plate': '1 Ore → 1 (3.2s)', 'Steel Plate': '5 Iron → 1 (16s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Fe → 1 (0.5s)', 'Copper Cable': '1 Cu → 2 (0.5s)', 'Pipe': '1 Fe → 1 (0.5s)', 'Engine Unit': '1 Gear + 1 Steel + 2 Pipe → 1 (10s)' } },
          { step: 3, label: 'Advanced parts', outputs: { 'Electronic Circuit': '1 Fe + 3 Cable → 1 (0.5s)', 'Advanced Circuit': '4 Cable + 2 Electronic + 2 Plastic → 1 (8s)', 'Electric Engine Unit': '1 Engine + 1 Circuit + 1.25 Lubricant → 1 (10s)' } },
          { step: 4, label: 'Final: Purple Science', outputs: { 'Production Science': '3 Advanced Circuit + 2 Electric Engine → 1 Purple (21s)' } },
        ],
        rawRecipe: { 'Production Science': { time: 21, out: 1, in: { 'Advanced Circuit': 3, 'Electric Engine Unit': 2 } } },
      },
      'Utility Science (Yellow)': {
        final: 'Utility Science',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 → 1 (3.2s)', 'Copper Plate': '1 → 1 (3.2s)', 'Steel Plate': '5 Fe → 1 (16s)', 'Plastic Bar': '1 Coal + 1.25 Gas → 2 (1s)' } },
          { step: 2, label: 'Parts', outputs: { 'Copper Cable': '1 Cu → 2 (0.5s)', 'Electronic Circuit': '1 Fe + 3 Cable → 1 (0.5s)', 'Advanced Circuit': '4 Cable + 2 Electronic + 2 Plastic → 1 (8s)' } },
          { step: 3, label: 'Processing units', outputs: { 'Processing Unit': '2 Advanced + 20 Electronic + 4 Acid → 1 (10s)', 'Battery': '1 Fe + 1 Cu + 2 Acid → 1 (4s)' } },
          { step: 4, label: 'Final: Yellow Science', outputs: { 'Utility Science': '3 Advanced Circuit + 1 Processing Unit → 1 Yellow (21s)' } },
        ],
        rawRecipe: { 'Utility Science': { time: 21, out: 1, in: { 'Advanced Circuit': 3, 'Processing Unit': 1 } } },
      },
      'Space Science': {
        final: 'Space Science',
        steps: [
          { step: 1, label: 'Rocket parts', outputs: { 'Rocket Part': '10 LDS + 10 Fuel + 10 RCU → 1 (10s)', 'Low Density Structure': '10 Steel + 5 Copper + 5 Plastic → 1 (10s)', 'Rocket Fuel': '10 Solid Fuel + 1 Light Oil → 1 (3s)' } },
          { step: 2, label: 'Rocket control', outputs: { 'Rocket Control Unit': '1 Processing Unit + 1 Blue Circuit → 1 (30s)' } },
          { step: 3, label: 'Launch', outputs: { 'Space Science': 'Launch rocket → 1000 Space Science' } },
        ],
        rawRecipe: { 'Space Science': { time: 1, out: 1000, in: { 'Rocket Part': 100 } } },
      },
      'Green Circuit': {
        final: 'Electronic Circuit',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 Ore → 1 (3.2s)', 'Copper Plate': '1 Ore → 1 (3.2s)' } },
          { step: 2, label: 'Cable', outputs: { 'Copper Cable': '1 Copper Plate → 2 Cable (0.5s)' } },
          { step: 3, label: 'Final: Green Circuit', outputs: { 'Electronic Circuit': '1 Iron Plate + 3 Copper Cable → 1 Circuit (0.5s)' } },
        ],
        rawRecipe: { 'Electronic Circuit': { time: 0.5, out: 1, in: { 'Iron Plate': 1, 'Copper Cable': 3 } } },
      },
      'Red Circuit (Advanced)': {
        final: 'Advanced Circuit',
        steps: [
          { step: 1, label: 'Smelting & oil', outputs: { 'Copper Plate': '1 Ore → 1 (3.2s)', 'Plastic Bar': '1 Coal + 1.25 Gas → 2 (1s)' } },
          { step: 2, label: 'Cable & Green Circuits', outputs: { 'Copper Cable': '1 Cu → 2 (0.5s)', 'Electronic Circuit': '1 Fe + 3 Cable → 1 (0.5s)' } },
          { step: 3, label: 'Final: Red Circuit', outputs: { 'Advanced Circuit': '4 Copper Cable + 2 Electronic Circuit + 2 Plastic → 1 (8s)' } },
        ],
        rawRecipe: { 'Advanced Circuit': { time: 8, out: 1, in: { 'Copper Cable': 4, 'Electronic Circuit': 2, 'Plastic Bar': 2 } } },
      },
      'Blue Circuit (Processing Unit)': {
        final: 'Processing Unit',
        steps: [
          { step: 1, label: 'Smelting & refining', outputs: { 'Copper Plate': '1 Ore → 1 (3.2s)', 'Iron Plate': '1 Ore → 1 (3.2s)', 'Plastic Bar': '1 Coal + 1.25 Gas → 2 (1s)', 'Sulfuric Acid': '0.5 Fe + 0.5 S + 1 Water → 5 (1s)' } },
          { step: 2, label: 'Basic circuits', outputs: { 'Copper Cable': '1 Cu → 2 (0.5s)', 'Electronic Circuit': '1 Fe + 3 Cable → 1 (0.5s)', 'Advanced Circuit': '4 Cable + 2 Electronic + 2 Plastic → 1 (8s)' } },
          { step: 3, label: 'Final: Processing Unit', outputs: { 'Processing Unit': '2 Advanced + 20 Electronic + 4 Sulfuric Acid → 1 (10s)' } },
        ],
        rawRecipe: { 'Processing Unit': { time: 10, out: 1, in: { 'Advanced Circuit': 2, 'Electronic Circuit': 20, 'Sulfuric Acid': 4 } } },
      },
      'Engine Unit': {
        final: 'Engine Unit',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Plate': '1 → 1 (3.2s)', 'Steel Plate': '5 Iron → 1 (16s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Iron → 1 (0.5s)', 'Pipe': '1 Iron Plate → 1 (0.5s)' } },
          { step: 3, label: 'Final: Engine Unit', outputs: { 'Engine Unit': '1 Gear + 1 Steel Plate + 2 Pipe → 1 (10s)' } },
        ],
        rawRecipe: { 'Engine Unit': { time: 10, out: 1, in: { 'Iron Gear Wheel': 1, 'Steel Plate': 1, 'Pipe': 2 } } },
      },
      'Electric Engine Unit': {
        final: 'Electric Engine Unit',
        steps: [
          { step: 1, label: 'Smelting & oil', outputs: { 'Iron Plate': '1 → 1 (3.2s)', 'Steel Plate': '5 Fe → 1 (16s)', 'Lubricant': '1 Heavy Oil → 1 (1s)' } },
          { step: 2, label: 'Parts', outputs: { 'Iron Gear Wheel': '2 Fe → 1 (0.5s)', 'Pipe': '1 Fe → 1 (0.5s)', 'Copper Cable': '1 Cu → 2 (0.5s)', 'Electronic Circuit': '1 Fe + 3 Cable → 1 (0.5s)' } },
          { step: 3, label: 'Sub-assemblies', outputs: { 'Engine Unit': '1 Gear + 1 Steel + 2 Pipe → 1 (10s)' } },
          { step: 4, label: 'Final: Electric Engine', outputs: { 'Electric Engine Unit': '1 Engine + 1 Electronic Circuit + 1.25 Lubricant → 1 (10s)' } },
        ],
        rawRecipe: { 'Electric Engine Unit': { time: 10, out: 1, in: { 'Engine Unit': 1, 'Electronic Circuit': 1, 'Lubricant': 1.25 } } },
      },
    },
    rawMats: {
      'Iron Ore': { raw: true }, 'Copper Ore': { raw: true }, 'Coal': { raw: true },
      'Stone': { raw: true }, 'Water': { raw: true }, 'Crude Oil': { raw: true },
      'Sulfur': { raw: true },
    }
  },
  dsp: {
    name: '🌌 Dyson Sphere Program',
    unit: '/ s',
    items: {
      'Processor': {
        final: 'Processor',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Ingot': '1 Iron Ore → 1 (1s)', 'Copper Ingot': '1 Copper Ore → 1 (1s)', 'Silicon': '2 Stone → 1 (2s) — or mine directly' } },
          { step: 2, label: 'Basic components', outputs: { 'Circuit Board': '2 Copper + 1 Iron → 1 (2s)' } },
          { step: 3, label: 'Final: Processor', outputs: { 'Processor': '2 Circuit Board + 2 Silicon → 1 (3s)' } },
        ],
        rawRecipe: { 'Processor': { time: 3, out: 1, in: { 'Circuit Board': 2, 'High-Purity Silicon': 2 } } },
      },
      'Quantum Chip': {
        final: 'Quantum Chip',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Ingot': '1 Ore → 1 (1s)', 'Copper Ingot': '1 Ore → 1 (1s)', 'Silicon': '2 Stone → 1 (2s)', 'Titanium Ingot': '1 Ore → 1 (2s)' } },
          { step: 2, label: 'Basic components', outputs: { 'Circuit Board': '2 Cu + 1 Fe → 1 (2s)', 'Steel': '3 Fe → 1 (3s)', 'Magnet': '1 Fe Ore → 1 (1.5s)', 'Prism': '3 Glass → 1 (2s)', 'Glass': '2 Stone → 2 (2s)' } },
          { step: 3, label: 'Mid components', outputs: { 'Processor': '2 Board + 2 Silicon → 1 (3s)', 'Plane Filter': '2 Titanium + 1 Circuit → 1 (4s)', 'Graphene': '3 Graphite + 1 Acid → 2 (3s)', 'Strange Matter': '2 Particle Container + 2 Processor → 1 (6s)' } },
          { step: 4, label: 'Graviton Lens', outputs: { 'Diamond': '2 Graphite → 1 (2s)', 'Graviton Lens': '4 Diamond + 1 Strange Matter → 1 (8s)' } },
          { step: 5, label: 'Final: Quantum Chip', outputs: { 'Quantum Chip': '2 Processor + 2 Plane Filter + 1 Graviton Lens → 1 (6s)' } },
        ],
        rawRecipe: { 'Quantum Chip': { time: 6, out: 1, in: { 'Processor': 2, 'Plane Filter': 2, 'Graviton Lens': 1 } } },
      },
      'Titanium Alloy': {
        final: 'Titanium Alloy',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Iron Ingot': '1 Ore → 1 (1s)', 'Titanium Ingot': '1 Ore → 1 (2s)' } },
          { step: 2, label: 'Steel', outputs: { 'Steel': '3 Iron Ingot → 1 (3s)' } },
          { step: 3, label: 'Sulfuric Acid', outputs: { 'Sulfuric Acid': '6 Stone → 1 (1s) — or pump from oceans' } },
          { step: 4, label: 'Final: Titanium Alloy', outputs: { 'Titanium Alloy': '4 Titanium Ingot + 4 Steel + 4 Sulfuric Acid → 1 (8s)' } },
        ],
        rawRecipe: { 'Titanium Alloy': { time: 8, out: 1, in: { 'Titanium Ingot': 4, 'Steel': 4, 'Sulfuric Acid': 4 } } },
      },
      'Particle Container': {
        final: 'Particle Container',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Copper Ingot': '1 Ore → 1 (1s)', 'Titanium Ingot': '1 Ore → 1 (2s)', 'Stone': '— from mining' } },
          { step: 2, label: 'Components', outputs: { 'Magnetic Coil': '2 Copper + 2 Magnet → 1 (2s)', 'Magnet': '1 Fe Ore → 1 (1.5s)' } },
          { step: 3, label: 'Electric Motor', outputs: { 'Electric Motor': '2 Fe + 1 Gear + 1 Magnetic Coil → 1 (3s)', 'Gear': '1 Fe → 1 (1s)' } },
          { step: 4, label: 'Final: Particle Container', outputs: { 'Particle Container': '2 Electric Motor + 2 Titanium Ingot → 1 (4s)' } },
        ],
        rawRecipe: { 'Particle Container': { time: 4, out: 1, in: { 'Electric Motor': 2, 'Titanium Ingot': 2 } } },
      },
      'Graviton Lens': {
        final: 'Graviton Lens',
        steps: [
          { step: 1, label: 'Smelting', outputs: { 'Copper Ingot': '1 Ore → 1 (1s)', 'Iron Ingot': '1 Ore → 1 (1s)', 'Silicon': '2 Stone → 1 (2s)', 'Stone': '— from mining' } },
          { step: 2, label: 'Components', outputs: { 'Glass': '2 Stone → 2 (2s)', 'Prism': '3 Glass → 1 (2s)', 'Circuit Board': '2 Cu + 1 Fe → 1 (2s)' } },
          { step: 3, label: 'Mid components', outputs: { 'Processor': '2 Board + 2 Silicon → 1 (3s)', 'Magnetic Coil': '2 Cu + 2 Magnet → 1 (2s)', 'Particle Container': '2 Motor + 2 Ti → 1 (4s)' } },
          { step: 4, label: 'Strange Matter', outputs: { 'Strange Matter': '2 Particle Container + 2 Processor → 1 (6s)' } },
          { step: 5, label: 'Diamond', outputs: { 'Graphite': '1 Coal → 1 (1s)', 'Diamond': '2 Graphite → 1 (2s)' } },
          { step: 6, label: 'Final: Graviton Lens', outputs: { 'Graviton Lens': '4 Diamond + 1 Strange Matter → 1 (8s)' } },
        ],
        rawRecipe: { 'Graviton Lens': { time: 8, out: 1, in: { 'Diamond': 4, 'Strange Matter': 1 } } },
      },
    },
    rawMats: {
      'Iron Ore': { raw: true }, 'Copper Ore': { raw: true }, 'Stone': { raw: true },
      'Coal': { raw: true }, 'Titanium Ore': { raw: true }, 'Silicon': { raw: true },
      'Water': { raw: true }, 'Crude Oil': { raw: true }, 'Fire Ice': { raw: true },
      'Kimberlite': { raw: true }, 'Fractal Silicon': { raw: true },
    }
  },
  timberborn: {
    name: '🌳 Timberborn',
    unit: '/ day',
    items: {
      'Mechanical Pump': {
        final: 'Mechanical Pump',
        steps: [
          { step: 1, label: 'Gather resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank (1h)', 'Gear': '1 Log → 1 Gear (1h at Gear Workshop)' } },
          { step: 2, label: 'Final: Mechanical Pump', outputs: { 'Mechanical Pump': '20 Plank + 4 Gear → 1 Mechanical Pump' } },
        ],
        rawRecipe: { 'Mechanical Pump': { time: 1, out: 1, in: { 'Plank': 20, 'Gear': 4 } } },
      },
      'Large Water Wheel': {
        final: 'Large Water Wheel',
        steps: [
          { step: 1, label: 'Gather resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank (1h)', 'Paper': '1 Log → 1 Paper (1h at Paper Mill)', 'Gear': '1 Log → 1 Gear (1h)' } },
          { step: 2, label: 'Metal parts', outputs: { 'Metal Block': '1 Scrap Metal → 1 Block (1h at Smelter)' } },
          { step: 3, label: 'Final: Large Water Wheel', outputs: { 'Large Water Wheel': '50 Plank + 10 Paper + 5 Gear + 5 Metal Block → 1 Wheel' } },
        ],
        rawRecipe: { 'Large Water Wheel': { time: 1, out: 1, in: { 'Plank': 50, 'Paper': 10, 'Gear': 5, 'Metal Block': 5 } } },
      },
      'Engine': {
        final: 'Engine',
        steps: [
          { step: 1, label: 'Basic resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank', 'Gear': '1 Log → 1 Gear' } },
          { step: 2, label: 'Metal processing', outputs: { 'Metal Block': '1 Scrap Metal → 1 Block', 'Explosive': '1 Sulphur + 1 Paper → 1 Explosive (at Explosives Factory)' } },
          { step: 3, label: 'Final: Engine', outputs: { 'Engine': '100 Plank + 50 Gear + 30 Metal Block + 15 Explosive → 1 Engine' } },
        ],
        rawRecipe: { 'Engine': { time: 1, out: 1, in: { 'Plank': 100, 'Gear': 50, 'Metal Block': 30, 'Explosive': 15 } } },
      },
      'Mine': {
        final: 'Mine',
        steps: [
          { step: 1, label: 'Basic resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank', 'Gear': '1 Log → 1 Gear' } },
          { step: 2, label: 'Metal & paper', outputs: { 'Metal Block': '1 Scrap → 1 Block', 'Paper': '1 Log → 1 Paper' } },
          { step: 3, label: 'Final: Mine', outputs: { 'Mine': '30 Plank + 10 Gear + 10 Metal Block + 10 Paper → 1 Mine' } },
        ],
        rawRecipe: { 'Mine': { time: 1, out: 1, in: { 'Plank': 30, 'Gear': 10, 'Metal Block': 10, 'Paper': 10 } } },
      },
      'Deep Mine': {
        final: 'Deep Mine',
        steps: [
          { step: 1, label: 'Basic resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank', 'Gear': '1 Log → 1 Gear' } },
          { step: 2, label: 'Metal processing', outputs: { 'Metal Block': '1 Scrap → 1 Block', 'Explosive': '1 Sulphur + 1 Paper → 1' } },
          { step: 3, label: 'Final: Deep Mine', outputs: { 'Deep Mine': '80 Plank + 30 Gear + 30 Metal Block + 20 Explosive + 20 Paper → 1 Deep Mine' } },
        ],
        rawRecipe: { 'Deep Mine': { time: 1, out: 1, in: { 'Plank': 80, 'Gear': 30, 'Metal Block': 30, 'Explosive': 20, 'Paper': 20 } } },
      },
      'Observatory': {
        final: 'Observatory',
        steps: [
          { step: 1, label: 'Basic resources', outputs: { 'Log': 'From trees', 'Plank': '1 Log → 1 Plank', 'Gear': '1 Log → 1 Gear' } },
          { step: 2, label: 'Metal & science', outputs: { 'Metal Block': '1 Scrap → 1 Block', 'Paper': '1 Log → 1 Paper', 'Science Points': 'Generated by Observatory itself' } },
          { step: 3, label: 'Final: Observatory', outputs: { 'Observatory': '60 Plank + 25 Gear + 15 Metal Block + 30 Paper → 1 Observatory' } },
        ],
        rawRecipe: { 'Observatory': { time: 1, out: 1, in: { 'Plank': 60, 'Gear': 25, 'Metal Block': 15, 'Paper': 30 } } },
      },
    },
    rawMats: {
      'Log': { raw: true }, 'Scrap Metal': { raw: true }, 'Sulphur': { raw: true },
      'Water': { raw: true }, 'Berries': { raw: true }, 'Carrots': { raw: true },
    }
  }
};

/* --- Helper: compute raw input requirements --- */
function computeRawInputs(gameKey, itemKey, ratePerUnit) {
  const data = FACTORY_DATA[gameKey];
  if (!data || !data.items[itemKey]) return { error: 'Item not found' };

  const item = data.items[itemKey];
  const recipe = item.rawRecipe[item.final];
  if (!recipe) return { error: 'Recipe not found' };

  const unit = data.unit;
  const isPerSec = (unit === '/ s');
  const isPerDay = (unit === '/ day');

  /* Calculate per-machine output rate */
  let rateFactor = 1;
  if (isPerSec) {
    /* Convert per-second to per-minute for display */
    rateFactor = 60;
  } else if (isPerDay) {
    /* Timberborn: assume a day cycle. For simplicity, use 1x */
    rateFactor = 1;
  }

  /* Adjust rate: recipe.time is in seconds for Satisfactory/Factorio/DSP */
  /* For a given desired output rate (per minute for SF, per sec for F/DSP, per day for TB) */
  const timeInSec = recipe.time;
  let baseRate;

  if (isPerSec) {
    baseRate = recipe.out / timeInSec;
  } else if (isPerDay) {
    baseRate = recipe.out / (timeInSec / 3600); /* approximate */
  } else {
    /* / min: Satisfactory */
    baseRate = recipe.out / (timeInSec / 60);
  }

  const machines = ratePerUnit / baseRate;

  const inputRates = {};
  for (const [mat, qty] of Object.entries(recipe.in)) {
    if (isPerSec) {
      inputRates[mat] = (qty / timeInSec) * machines;
    } else if (isPerDay) {
      inputRates[mat] = (qty / (timeInSec / 3600)) * machines;
    } else {
      inputRates[mat] = (qty / (timeInSec / 60)) * machines;
    }
  }

  return { machines: machines, inputRates: inputRates, baseRate: baseRate, unit: unit };
}

/* --- UI Elements --- */
const gameSelect = document.getElementById('fp-game-select');
const itemSelect = document.getElementById('fp-item-select');
const targetRate = document.getElementById('fp-target-rate');
const calcBtn = document.getElementById('fp-calc-btn');
const results = document.getElementById('fp-results');
const chainDisplay = document.getElementById('fp-chain-display');
const summaryDisplay = document.getElementById('fp-summary');

gameSelect.addEventListener('change', () => {
  const game = gameSelect.value;
  itemSelect.innerHTML = '<option value="">— Select an item —</option>';
  results.style.display = 'none';
  if (!game || !FACTORY_DATA[game]) return;

  const data = FACTORY_DATA[game];
  Object.keys(data.items).sort().forEach(name => {
    const opt = document.createElement('option');
    opt.value = name;
    opt.textContent = name;
    itemSelect.appendChild(opt);
  });
});

calcBtn.addEventListener('click', calculate);

function calculate() {
  const game = gameSelect.value;
  const item = itemSelect.value;
  const rate = parseFloat(targetRate.value);

  if (!game || !item || !rate || rate <= 0) {
    results.style.display = 'block';
    summaryDisplay.innerHTML = '<span style="color:#f87171;">⚠️ Please select a game and item, and enter a valid target rate.</span>';
    chainDisplay.innerHTML = '';
    return;
  }

  const data = FACTORY_DATA[game];
  const itemData = data.items[item];
  if (!itemData) {
    summaryDisplay.innerHTML = `<span style="color:#f87171;">⚠️ Item data not found for "${item}".</span>`;
    chainDisplay.innerHTML = '';
    return;
  }

  /* Build vertical chain display */
  let chainHtml = '';

  itemData.steps.forEach(step => {
    chainHtml += `<div style="margin: 12px 0; padding: 12px 16px; background: rgba(255,255,255,0.03); border-left: 3px solid #f97316; border-radius: 0 8px 8px 0;">`;
    chainHtml += `<div style="font-size:0.75rem; color:#f97316; font-weight:600; margin-bottom:6px; text-transform:uppercase; letter-spacing:0.5px;">Step ${step.step}: ${step.label}</div>`;

    for (const [outName, desc] of Object.entries(step.outputs)) {
      chainHtml += `<div style="display:flex; align-items:center; gap:8px; padding:3px 0;">
        <span style="color:#eab308; font-weight:600; font-size:0.9rem;">→</span>
        <span style="color:#e8e6e3; font-size:0.85rem;">${outName}:</span>
        <span style="color:#94a3b8; font-size:0.78rem;">${desc}</span>
      </div>`;
    }
    chainHtml += `</div>`;
  });

  chainDisplay.innerHTML = chainHtml;

  /* Calculate raw inputs */
  const calc = computeRawInputs(game, item, rate);

  if (calc.error) {
    summaryDisplay.innerHTML = `<span style="color:#f87171;">⚠️ ${calc.error}</span>`;
    return;
  }

  results.style.display = 'block';

  let summaryHtml = `
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px;">
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Target Output</div>
        <div style="font-size:1.3rem; font-weight:700; color:#22c55e;">${rate}</div>
        <div style="font-size:0.7rem; color:#475569;">${itemData.final} ${calc.unit}</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Machines / Buildings</div>
        <div style="font-size:1.3rem; font-weight:700; color:#f97316;">${calc.machines.toFixed(2)}</div>
        <div style="font-size:0.7rem; color:#475569;">at 100% clock speed</div>
      </div>
      <div style="padding:12px; background:rgba(255,255,255,0.03); border-radius:8px;">
        <div style="font-size:0.75rem; color:#64748b;">Base rate per machine</div>
        <div style="font-size:1.3rem; font-weight:700; color:#60a5fa;">${calc.baseRate.toFixed(2)}</div>
        <div style="font-size:0.7rem; color:#475569;">${calc.unit}</div>
      </div>
    </div>
  `;

  /* Raw input table */
  if (Object.keys(calc.inputRates).length > 0) {
    summaryHtml += '<h4 style="margin:16px 0 8px;">📦 Raw Input Requirements</h4>';
    summaryHtml += '<table style="width:100%; border-collapse:collapse;">';
    summaryHtml += '<thead><tr style="border-bottom:1px solid rgba(255,255,255,0.1);"><th style="text-align:left; padding:8px; font-size:0.78rem;">Material</th><th style="text-align:right; padding:8px; font-size:0.78rem;">Required Rate</th></tr></thead><tbody>';

    for (const [mat, matRate] of Object.entries(calc.inputRates).sort()) {
      const isRaw = data.rawMats && data.rawMats[mat] && data.rawMats[mat].raw;
      const color = isRaw ? '#22c55e' : '#eab308';
      const badge = isRaw ? ' ⛏️' : ' 🔧';
      summaryHtml += `<tr style="border-bottom:1px solid rgba(255,255,255,0.03);">
        <td style="padding:8px; font-size:0.85rem;">${mat}${badge}</td>
        <td style="text-align:right; padding:8px; font-weight:600; color:${color};">${matRate.toFixed(2)} <span style="color:#64748b; font-weight:400; font-size:0.75rem;">${calc.unit}</span></td>
      </tr>`;
    }

    summaryHtml += '</tbody></table>';
    summaryHtml += '<p style="font-size:0.7rem; color:#475569; margin-top:8px;">⛏️ = Raw resource &nbsp;|&nbsp; 🔧 = Crafted intermediate</p>';
  }

  summaryDisplay.innerHTML = summaryHtml;
}
