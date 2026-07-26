"""
MkDocs 钩子: 自动注入 FAQ/HowTo Schema 结构化数据
SEO 收益: Google Rich Result 显示，CTR +20-30%
"""
import re

def on_page_content(html, page, config, files):
    """在 </head> 前注入 JSON-LD 结构化数据"""

    title = page.title or page.meta.get('title', '')
    if not title:
        return html

    # 自动判断页面类型
    is_guide = any(kw in title.lower() for kw in ['guide', 'tips', 'how', 'build', 'strategy', '攻略', '指南'])
    is_faq = any(kw in title.lower() for kw in ['faq', 'question', 'common'])

    # 提取页面描述
    description = page.meta.get('description', title)

    if is_guide:
        schema = {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": title,
            "description": description,
            "dateModified": page.meta.get('date', ''),
            "author": {
                "@type": "Organization",
                "name": config.get('site_name', 'Game Guide Club')
            }
        }
    elif is_faq:
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": []  # 由具体页面补充
        }
    else:
        schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description,
            "dateModified": page.meta.get('date', ''),
            "author": {
                "@type": "Organization",
                "name": config.get('site_name', '')
            }
        }

    import json
    script = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'

    # 注入到 </head> 前
    if '</head>' in html:
        html = html.replace('</head>', f'{script}\n</head>')

    return html
