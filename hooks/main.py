"""
Macros plugin module for game-guide.club
Provides template helpers for batch page generation.
"""

import re

def define_env(env):
    """Define template variables and functions for MkDocs macros plugin."""

    @env.macro
    def tier_badge(tier):
        """Render a tier ranking badge (S/A/B/C/D/F)."""
        colors = {
            "S": "#FF4444", "A": "#FF8C00", "B": "#FFD700",
            "C": "#44AA44", "D": "#4488FF", "F": "#888888"
        }
        color = colors.get(tier.upper(), "#888")
        return f'<span style="display:inline-block;padding:2px 8px;border-radius:4px;background:{color};color:#fff;font-weight:bold;font-size:0.85em">{tier.upper()}</span>'

    @env.macro
    def stat_bar(value, max_val=100, color="#FF5722"):
        """Render a horizontal stat bar."""
        pct = min(100, int(value / max_val * 100))
        return (
            f'<div style="background:#333;border-radius:4px;overflow:hidden;height:20px;min-width:120px">'
            f'<div style="width:{pct}%;background:{color};height:100%;display:flex;align-items:center;padding-left:6px;font-size:0.75em;color:#fff;font-weight:bold">{value}</div>'
            f'</div>'
        )

    @env.macro
    def star_rating(rating):
        """Render star rating (0-5)."""
        full = "★" * int(rating)
        half = "½" if rating - int(rating) >= 0.5 else ""
        empty = "☆" * max(0, 5 - int(rating) - (1 if half else 0))
        return f'<span style="color:#FFD700;font-size:1.1em">{full}{half}{empty}</span>'

    @env.macro
    def tier_table(items, title="Tier排名"):
        """Generate a tier ranking table from a list of dicts.
        Each item: name, tier, description, icon
        """
        if not items:
            return "<p>暂无数据</p>"
        tier_order = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4, "F": 5}
        rows = ""
        for item in sorted(items, key=lambda x: tier_order.get(x.get("tier", "F").upper(), 9)):
            t = item.get("tier", "?").upper()
            rows += f"""<tr>
                <td>{tier_badge(t)}</td>
                <td><strong>{item.get("icon", "")} {item.get("name", "")}</strong></td>
                <td>{item.get("description", "")}</td>
            </tr>"""
        return f"""<table class="datatable" style="width:100%">
            <thead><tr><th>Tier</th><th>名称</th><th>说明</th></tr></thead>
            <tbody>{rows}</tbody>
        </table>"""

    @env.macro
    def affiliate_section(game_name, steam_id="", humble_url="", epic_url=""):
        """Standard affiliate section for bottom of guides."""
        html = '\n---\n\n### 🛒 购买链接\n\n'
        if steam_id:
            html += f'<a href="https://store.steampowered.com/app/{steam_id}/" target="_blank" rel="nofollow sponsored" style="display:inline-block;padding:8px 16px;margin:4px;background:#FF5722;color:#fff;border-radius:8px;text-decoration:none;font-size:0.9em">🎮 Steam 购买</a>\n'
        if humble_url:
            html += f'<a href="{humble_url}" target="_blank" rel="nofollow sponsored" style="display:inline-block;padding:8px 16px;margin:4px;background:#cc4749;color:#fff;border-radius:8px;text-decoration:none;font-size:0.9em">📦 Humble Bundle</a>\n'
        if epic_url:
            html += f'<a href="{epic_url}" target="_blank" rel="nofollow sponsored" style="display:inline-block;padding:8px 16px;margin:4px;background:#404040;color:#fff;border-radius:8px;text-decoration:none;font-size:0.9em">⭐ Epic Games</a>\n'
        html += '\n\n*以上链接为推广链接，购买后本站可获得少量佣金，不影响您的购买价格。*\n'
        return html
