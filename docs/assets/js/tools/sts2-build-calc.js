/**
 * Slay the Spire 2 — Build Synergy Calculator
 * 评估卡组协同度 + 给出改进建议
 */
(function() {
  'use strict';

  var ARCHETYPES = {
    ironclad: {
      name: 'Ironclad',
      icon: '🛡️',
      builds: {
        strength: {
          name: 'Strength Stack',
          key: ['Ashen Strike','Brand','Burning Pact','Fiend Fire','Limit Break','Heavy Blade','Sword Boomerang','Inflame','Spot Weakness','Demon Form'],
          support: ['Shrug It Off','True Grit','Impervious','Flame Barrier','Offering','Battle Trance'],
          relic: ['Charon\'s Ashes','Toasty Mittens','Burning Sticks','Red Skull','Brimstone'],
          desc: '叠力量 → 多段攻击爆发。核心是 Ashen Strike + Brand 的消耗引擎。'
        },
        block: {
          name: 'Body Slam Defense',
          key: ['Body Slam','Barricade','Entrench','Impervious','Flame Barrier','Juggernaut','Ghostly Armor','Power Through','Second Wind','Evolve'],
          support: ['Shrug It Off','True Grit','Offering','Battle Trance'],
          relic: ['Bronze Scales','Oddly Smooth Stone','Horn Cleat','Calipers','Self-Forming Clay'],
          desc: '堆超高 Block → Body Slam 转化伤害。遗物加成后一回合能打 200+。'
        }
      }
    },
    silent: {
      name: 'Silent',
      icon: '🗡️',
      builds: {
        poison: {
          name: 'Poison Catalyst',
          key: ['Catalyst','Noxious Fumes','Bouncing Flask','Deadly Poison','Corpse Explosion','Crippling Cloud','Envenom'],
          support: ['Adrenaline','Well Laid Plans','Calculated Gamble','Acrobatics','Backflip'],
          relic: ['Snecko Skull','Specimen','Twisted Funnel','Busted Crown'],
          desc: '叠毒 → Catalyst 翻倍。Noxious Fumes 提供稳定毒源，Catalyst 爆发收尾。'
        },
        shiv: {
          name: 'Shiv Spam',
          key: ['Infinite Blades','Cloak and Dagger','Blade Dance','Storm of Steel','Accuracy','After Image','Finisher','Thousand Cuts','Envenom'],
          support: ['Adrenaline','Well Laid Plans','Calculated Gamble'],
          relic: ['Shuriken','Kunai','Ornamental Fan','Wrist Blade','Dead Branch'],
          desc: '大量 0 费 Shiv → 触发遗物连击。千刀万剐 + 余像 = 攻守一体。'
        }
      }
    },
    defect: {
      name: 'Defect',
      icon: '⚡',
      builds: {
        orb: {
          name: 'Lightning Orb Engine',
          key: ['Electrodynamics','Defragment','Capacitor','Biased Cognition','Fusion','Loop','Storm','Static Discharge','Thunder Strike'],
          support: ['Seek','Hologram','Reboot','Coolheaded','Charge Battery'],
          relic: ['Data Disk','Gold Plated Cables','Emotion Chip','Runic Capacitor','Frozen Core','Tesla Coil'],
          desc: '堆 Orb 位 → 被动伤害拉满。Fusion 1费0费补能。Tesla Coil+ 触发翻倍。'
        }
      }
    },
    necrobinder: {
      name: 'Necrobinder',
      icon: '💀',
      builds: {
        minion: {
          name: 'Minion Horde',
          key: ['Death March','Sic\' Em','The Scythe','Raise Dead','Grave Call','Bone Wall','Soul Harvest'],
          support: ['Offering','Battle Trance','Dark Ritual'],
          relic: ['Bone Charm','Grave Dust','Soul Urn'],
          desc: '快速铺随从 → Death March 全军突击。Debilitate 削弱 2-3 回合足够收尾。'
        }
      }
    },
    regent: {
      name: 'Regent',
      icon: '👑',
      builds: {
        sovereign: {
          name: 'Sovereign Blade',
          key: ['Sovereign Blade','Parry','Monarch\'s Gaze','Royal Decree','Tyranny','Bombardment','Crown of Thorns','Imperial Guard'],
          support: ['Adrenaline','Offering','Battle Trance'],
          relic: ['Royal Signet','Crown Jewel','Throne Room'],
          desc: 'Sovereign Blade 主输出 → Parry 给格挡（受敏捷影响）→ Monarch 2费1费加速循环。'
        }
      }
    }
  };

  function scoreBuild(selected, build) {
    var keyMatch = 0, supportMatch = 0;
    for (var i = 0; i < selected.length; i++) {
      if (build.key.indexOf(selected[i]) >= 0) keyMatch++;
      if (build.support.indexOf(selected[i]) >= 0) supportMatch++;
    }
    var keyScore = build.key.length > 0 ? keyMatch / build.key.length : 0;
    var supportScore = build.support.length > 0 ? supportMatch / build.support.length : 0;
    var total = Math.round((keyScore * 70 + supportScore * 30));
    return {
      total: total,
      keyMatch: keyMatch,
      keyTotal: build.key.length,
      supportMatch: supportMatch,
      missing: build.key.filter(function(c){return selected.indexOf(c) < 0;})
    };
  }

  function renderCalc() {
    var html = '<div style="background:#16213e;padding:20px;border-radius:8px;margin-bottom:24px">';
    html += '<h3>🧮 Build 评分器</h3>';
    html += '<p>输入你的卡组（逗号分隔），选择角色和 Build 类型，看协同度评分。</p>';
    html += '<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px">';
    html += '<input id="sts2-cards" placeholder="例: Ashen Strike, Brand, Shrug It Off" style="flex:1;min-width:250px;padding:8px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px">';
    html += '<select id="sts2-class" style="padding:8px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px">';
    for (var ch in ARCHETYPES) {
      html += '<option value="' + ch + '">' + ARCHETYPES[ch].icon + ' ' + ARCHETYPES[ch].name + '</option>';
    }
    html += '</select>';
    html += '<select id="sts2-build" style="padding:8px;background:#0f3460;border:1px solid #333;color:#eee;border-radius:4px"></select>';
    html += '<button onclick="window._sts2score()" style="padding:8px 20px;background:#e94560;border:none;color:white;border-radius:4px;cursor:pointer;font-weight:bold">评 分</button>';
    html += '</div>';
    html += '<div id="sts2-result" style="margin-top:12px"></div>';
    html += '</div>';

    // Build selector
    html += '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(350px,1fr));gap:16px">';
    for (var ch in ARCHETYPES) {
      var cdata = ARCHETYPES[ch];
      for (var bk in cdata.builds) {
        var bdata = cdata.builds[bk];
        html += '<div style="background:#16213e;padding:16px;border-radius:8px;border-left:3px solid #e94560">';
        html += '<h4>' + cdata.icon + ' ' + bdata.name + '</h4>';
        html += '<p style="color:#999;font-size:13px">' + bdata.desc + '</p>';
        html += '<details><summary style="cursor:pointer;color:#e94560;font-size:12px">📋 卡牌列表</summary>';
        html += '<p style="font-size:12px"><strong>核心 (' + bdata.key.length + '):</strong> ' + bdata.key.join(', ') + '</p>';
        html += '<p style="font-size:12px"><strong>辅助 (' + bdata.support.length + '):</strong> ' + bdata.support.join(', ') + '</p>';
        html += '<p style="font-size:12px"><strong>遗物 (' + bdata.relic.length + '):</strong> ' + bdata.relic.join(', ') + '</p>';
        html += '</details></div>';
      }
    }
    html += '</div>';

    var el = document.getElementById('sts2-build-calc');
    if (el) el.innerHTML = html;

    // Init build selector
    updateBuilds();
    document.getElementById('sts2-class').onchange = updateBuilds;
    window._sts2score = doScore;
  }

  function updateBuilds() {
    var ch = document.getElementById('sts2-class').value;
    var sel = document.getElementById('sts2-build');
    sel.innerHTML = '';
    var builds = ARCHETYPES[ch].builds;
    for (var bk in builds) {
      sel.innerHTML += '<option value="' + ch + '|' + bk + '">' + builds[bk].name + '</option>';
    }
  }

  function doScore() {
    var cards = document.getElementById('sts2-cards').value.split(',').map(function(s){return s.trim();}).filter(Boolean);
    var buildKey = document.getElementById('sts2-build').value.split('|');
    var cdata = ARCHETYPES[buildKey[0]];
    var bdata = cdata.builds[buildKey[1]];
    var score = scoreBuild(cards, bdata);

    var color = score.total >= 70 ? '#4caf50' : score.total >= 40 ? '#ff9800' : '#f44336';
    var grade = score.total >= 80 ? 'S' : score.total >= 60 ? 'A' : score.total >= 40 ? 'B' : score.total >= 20 ? 'C' : 'D';

    var html = '<div style="padding:16px;border-radius:6px;background:#0f3460">';
    html += '<h4 style="margin:0">协同度: <span style="color:' + color + ';font-size:24px">' + grade + ' (' + score.total + '%)</span></h4>';
    html += '<p>🃏 核心卡匹配: <strong>' + score.keyMatch + '/' + score.keyTotal + '</strong></p>';
    if (score.supportMatch > 0) html += '<p>🔄 辅助卡匹配: <strong>' + score.supportMatch + '</strong></p>';
    if (score.missing.length > 0) html += '<p>⚠️ 缺少关键卡: <strong>' + score.missing.join(', ') + '</strong></p>';
    if (score.total >= 60) html += '<p>✅ 卡组方向正确！在商店优先拿剩余核心卡。</p>';
    else if (score.total >= 30) html += '<p>🟡 卡组还在早期，继续收集核心组件。</p>';
    else html += '<p>🔴 这个 Build 缺少核心引擎，考虑转方向或在下一商店补卡。</p>';
    html += '</div>';

    document.getElementById('sts2-result').innerHTML = html;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderCalc);
  } else {
    renderCalc();
  }
})();
