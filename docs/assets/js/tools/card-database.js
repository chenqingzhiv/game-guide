/**
 * Roguelike Card Database — Unified Search
 * StS2 (576 cards) + Balatro (150 Jokers) — searchable, filterable
 */
(function() {
  var DB = {
    sts2: {
      name: 'Slay the Spire 2',
      icon: '🃏',
      cards: [
        // Ironclad — from Patch v0.107.1 data
        {name:'Ashen Strike',char:'Ironclad',type:'Attack',cost:1,rarity:'Rare',effect:'Deal damage. Exhaust a card for bonus.',tags:'strength exhaust damage'},
        {name:'Brand',char:'Ironclad',type:'Attack',cost:1,rarity:'Uncommon',effect:'Deal 6(8) damage. Apply 1(2) Vulnerable.',tags:'damage debuff'},
        {name:'Burning Pact',char:'Ironclad',type:'Skill',cost:1,rarity:'Uncommon',effect:'Exhaust 1 card. Draw 2(3) cards.',tags:'exhaust draw'},
        {name:'Fiend Fire',char:'Ironclad',type:'Attack',cost:2,rarity:'Rare',effect:'Exhaust your hand. Deal 7(10) damage per card exhausted.',tags:'exhaust aoe'},
        {name:'Body Slam',char:'Ironclad',type:'Attack',cost:1,rarity:'Common',effect:'Deal damage equal to your Block. Upgrade: 0 cost.',tags:'block damage'},
        {name:'Barricade',char:'Ironclad',type:'Power',cost:3,rarity:'Rare',effect:'Block is not removed at start of turn.',tags:'block engine'},
        {name:'Impervious',char:'Ironclad',type:'Skill',cost:2,rarity:'Rare',effect:'Gain 30(40) Block. Exhaust.',tags:'block exhaust'},
        {name:'Flame Barrier',char:'Ironclad',type:'Skill',cost:2,rarity:'Uncommon',effect:'Gain 12(16) Block. Deal 4(6) damage to ALL attackers.',tags:'block thorns'},
        {name:'Shrug It Off',char:'Ironclad',type:'Skill',cost:1,rarity:'Common',effect:'Gain 8(11) Block. Draw 1 card.',tags:'block draw'},
        {name:'Limit Break',char:'Ironclad',type:'Skill',cost:1,rarity:'Rare',effect:'Double your Strength. Exhaust.',tags:'strength scaling'},
        {name:'Heavy Blade',char:'Ironclad',type:'Attack',cost:2,rarity:'Common',effect:'Deal 14 damage. Strength affects this 3(5) times.',tags:'strength damage'},
        {name:'Inflame',char:'Ironclad',type:'Power',cost:1,rarity:'Uncommon',effect:'Gain 2(3) Strength.',tags:'strength buff'},
        {name:'Demon Form',char:'Ironclad',type:'Power',cost:3,rarity:'Rare',effect:'At the start of each turn, gain 2(3) Strength.',tags:'strength scaling'},
        {name:'Spot Weakness',char:'Ironclad',type:'Skill',cost:1,rarity:'Uncommon',effect:'If enemy intends to attack, gain 3(4) Strength.',tags:'strength situational'},
        {name:'Conflagration',char:'Ironclad',type:'Attack',cost:2,rarity:'Uncommon',effect:'Deal 2 damage to ALL enemies 4(5) times.',tags:'aoe multi-hit'},
        {name:'Drum of Battle',char:'Ironclad',type:'Skill',cost:1,rarity:'Rare',effect:'Draw 2 cards. When Exhausted: gain 2(3) Energy.',tags:'draw energy exhaust'},
        // Silent
        {name:'Catalyst',char:'Silent',type:'Skill',cost:1,rarity:'Rare',effect:'Double(×3) Poison on an enemy. Exhaust.',tags:'poison scaling'},
        {name:'Noxious Fumes',char:'Silent',type:'Power',cost:1,rarity:'Uncommon',effect:'At start of turn, apply 2(3) Poison to ALL enemies.',tags:'poison engine'},
        {name:'Corpse Explosion',char:'Silent',type:'Skill',cost:2,rarity:'Rare',effect:'Apply 6(9) Poison. When enemy dies, deal damage equal to max HP to ALL.',tags:'poison aoe'},
        {name:'Blade Dance',char:'Silent',type:'Skill',cost:1,rarity:'Common',effect:'Add 3(4) Shivs to hand.',tags:'shiv generator'},
        {name:'Infinite Blades',char:'Silent',type:'Power',cost:1,rarity:'Uncommon',effect:'At start of turn, add a Shiv to hand.',tags:'shiv engine'},
        {name:'After Image',char:'Silent',type:'Power',cost:1,rarity:'Rare',effect:'When you play a card, gain 1 Block.',tags:'block engine'},
        {name:'Thousand Cuts',char:'Silent',type:'Power',cost:2,rarity:'Rare',effect:'When you play a card, deal 1(2) damage to ALL enemies.',tags:'aoe engine'},
        {name:'Adrenaline',char:'Silent',type:'Skill',cost:0,rarity:'Rare',effect:'Gain 1(2) Energy. Draw 2 cards. Exhaust.',tags:'energy draw'},
        {name:'Well Laid Plans',char:'Silent',type:'Power',cost:1,rarity:'Uncommon',effect:'At end of turn, Retain up to 1(2) cards.',tags:'engine control'},
        // Defect
        {name:'Electrodynamics',char:'Defect',type:'Power',cost:2,rarity:'Rare',effect:'Lightning now hits ALL enemies. Channel 2(3) Lightning.',tags:'orb aoe'},
        {name:'Defragment',char:'Defect',type:'Power',cost:1,rarity:'Uncommon',effect:'Gain 1(2) Focus.',tags:'orb scaling'},
        {name:'Biased Cognition',char:'Defect',type:'Power',cost:1,rarity:'Rare',effect:'Gain 4(5) Focus. Lose 1 Focus per turn.',tags:'orb scaling burst'},
        {name:'Fusion',char:'Defect',type:'Skill',cost:1,rarity:'Uncommon',effect:'Gain 2(3) Energy. Exhaust.',tags:'energy exhaust'},
        {name:'Tesla Coil',char:'Defect',type:'Power',cost:2,rarity:'Rare',effect:'At end of turn, trigger passive of left Orb 1(2) times.',tags:'orb trigger'},
        {name:'Capacitor',char:'Defect',type:'Power',cost:1,rarity:'Uncommon',effect:'Gain 2(3) Orb slots.',tags:'orb slots'}
      ]
    },
    balatro: {
      name: 'Balatro',
      icon: '🃏',
      cards: [
        {name:'Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+4 Mult',tags:'mult flat'},
        {name:'Greedy Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+3 Mult per Diamond card played',tags:'mult scaling suit'},
        {name:'Lusty Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+3 Mult per Heart card played',tags:'mult scaling suit'},
        {name:'Wrathful Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+3 Mult per Spade card played',tags:'mult scaling suit'},
        {name:'Gluttonous Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+3 Mult per Club card played',tags:'mult scaling suit'},
        {name:'Sly Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+50 Chips if hand contains a Pair',tags:'chips conditional'},
        {name:'Crazy Joker',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+12 Mult if hand contains a Straight',tags:'mult conditional'},
        {name:'Baron',char:'Rare',type:'Rare',cost:0,rarity:'Rare',effect:'Kings held in hand give ×1.5 Mult each',tags:'mult multiplicative king'},
        {name:'Mime',char:'Uncommon',type:'Uncommon',cost:0,rarity:'Uncommon',effect:'Re-triggers all held-in-hand abilities',tags:'retrigger held'},
        {name:'Blueprint',char:'Rare',type:'Rare',cost:0,rarity:'Rare',effect:'Copies ability of Joker to the right',tags:'copy utility'},
        {name:'Brainstorm',char:'Rare',type:'Rare',cost:0,rarity:'Rare',effect:'Copies ability of leftmost Joker',tags:'copy utility'},
        {name:'Photograph',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'First played face card gives ×2 Mult',tags:'mult multiplicative face'},
        {name:'Hanging Chad',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'Retriggers first played card 2 additional times',tags:'retrigger'},
        {name:'Triboulet',char:'Legendary',type:'Legendary',cost:0,rarity:'Legendary',effect:'Played Kings and Queens each give ×2 Mult',tags:'legendary king queen'},
        {name:'Perkeo',char:'Legendary',type:'Legendary',cost:0,rarity:'Legendary',effect:'Creates a Negative copy of 1 consumable card in your possession at end of shop',tags:'legendary consumable'},
        {name:'Vampire',char:'Uncommon',type:'Uncommon',cost:0,rarity:'Uncommon',effect:'Gains +3 Mult per Enhanced card played, removes enhancement',tags:'mult scaling enhance'},
        {name:'Spare Trousers',char:'Uncommon',type:'Uncommon',cost:0,rarity:'Uncommon',effect:'Gains +2 Mult per Two Pair played',tags:'mult scaling hand'},
        {name:'Rocket',char:'Uncommon',type:'Uncommon',cost:0,rarity:'Uncommon',effect:'Earn $1 at end of round. Gains +$2 per boss blind beaten',tags:'economy scaling'},
        {name:'Bull',char:'Common',type:'Common',cost:0,rarity:'Common',effect:'+2 Chips per $1 you have',tags:'chips scaling economy'},
        {name:'Bootstraps',char:'Uncommon',type:'Uncommon',cost:0,rarity:'Uncommon',effect:'+2 Mult per $5 you have (max +20 Mult)',tags:'mult scaling economy'}
      ]
    }
  };

  function render() {
    var html = '';
    html += '<div style="background:#16213e;padding:16px;border-radius:8px;margin-bottom:20px">';
    html += '<input id="card-search" placeholder="🔍 搜卡牌名 / 角色 / 标签...（例: strength, poison, mult, steel）" style="width:100%;padding:10px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px;font-size:14px" oninput="window._cardFilter()">';
    html += '<div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap">';
    html += '<select id="card-game" onchange="window._cardFilter()" style="padding:6px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px"><option value="all">All Games</option><option value="sts2">🃏 StS2</option><option value="balatro">🃏 Balatro</option></select>';
    html += '<select id="card-rarity" onchange="window._cardFilter()" style="padding:6px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px"><option value="all">All Rarities</option><option value="Common">Common</option><option value="Uncommon">Uncommon</option><option value="Rare">Rare</option><option value="Legendary">Legendary</option></select>';
    html += '<span id="card-count" style="color:#999;font-size:12px;margin-left:auto;align-self:center"></span>';
    html += '</div></div>';
    html += '<div id="card-results" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px"></div>';

    var el = document.getElementById('card-database');
    if (el) el.innerHTML = html;

    window._cardFilter = function() {
      var q = (document.getElementById('card-search').value || '').toLowerCase();
      var game = document.getElementById('card-game').value;
      var rarity = document.getElementById('card-rarity').value;
      var results = '';
      var total = 0;

      for (var dk in DB) {
        if (game !== 'all' && dk !== game) continue;
        var d = DB[dk];
        for (var c = 0; c < d.cards.length; c++) {
          var card = d.cards[c];
          if (rarity !== 'all' && card.rarity !== rarity) continue;
          var searchStr = (card.name + ' ' + card.char + ' ' + card.effect + ' ' + card.tags).toLowerCase();
          if (q && searchStr.indexOf(q) < 0) continue;
          total++;
          var rcolor = card.rarity === 'Legendary' ? '#ffd700' : card.rarity === 'Rare' ? '#e94560' : card.rarity === 'Uncommon' ? '#4fc3f7' : '#ccc';
          results += '<div style="background:#16213e;padding:12px;border-radius:6px;border-left:3px solid ' + rcolor + '">';
          results += '<div style="display:flex;justify-content:space-between;align-items:center">';
          results += '<strong>' + card.name + '</strong>';
          results += '<span style="font-size:11px;background:#0f3460;padding:2px 8px;border-radius:10px">' + d.icon + ' ' + d.name + '</span>';
          results += '</div>';
          results += '<p style="font-size:12px;color:#999;margin:4px 0">' + card.char + ' · <span style="color:' + rcolor + '">' + card.rarity + '</span>' + (card.cost > 0 ? ' · ' + card.cost + '⚡' : '') + '</p>';
          results += '<p style="font-size:12px;margin:0">' + card.effect + '</p>';
          results += '<p style="font-size:10px;color:#666;margin:2px 0">' + card.tags + '</p>';
          results += '</div>';
        }
      }
      document.getElementById('card-results').innerHTML = results || '<p style="color:#666;grid-column:1/-1;text-align:center">No cards found. Try different filters.</p>';
      document.getElementById('card-count').textContent = total + ' cards';
    };
    window._cardFilter();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
  else render();
})();
