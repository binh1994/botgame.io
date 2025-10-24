#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixed auto_generate.py
- Avoids .format()/f-strings on content with Liquid tags
- Uses placeholder replace() so {% ... %} and {{ ... }} are preserved
- Writes one markdown post to _posts/
"""

import os
import datetime
import random

# If you want domain detection from repo folder name, keep this logic:
SITE_DOMAIN = os.environ.get("SITE_DOMAIN", "").strip()
if not SITE_DOMAIN:
    SITE_DOMAIN = os.path.basename(os.getcwd())  # fallback to current folder name

DOMAINS = [
    'botgame.io', 'metaversebot.io', 'nftgameai.com', 'hubgaming.io',
    'botdefi.io', 'esportsai.io', 'nftgamepro.com', 'botesports.com',
    'aiesports.io', 'pronftgame.com', 'botplay.io', 'botweb3ai.com',
    'botblockchain.io'
]

# image pools (Pexels direct + fallbacks)
IMAGES = {
    'botgame.io': [
        "https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
        "https://source.unsplash.com/1200x630/?esports,ai,game",
        "https://picsum.photos/1200/630?random=772535"
    ],
    'metaversebot.io': [
        "https://images.pexels.com/photos/8132695/pexels-photo-8132695.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
        "https://source.unsplash.com/1200x630/?metaverse,vr",
        "https://picsum.photos/1200/630?random=185474"
    ],
    'nftgameai.com': [
        "https://images.pexels.com/photos/8370753/pexels-photo-8370753.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
        "https://source.unsplash.com/1200x630/?nft,game",
        "https://picsum.photos/1200/630?random=797807"
    ],
    # fallback generic pool for other domains
    'default': [
        "https://images.pexels.com/photos/3945662/pexels-photo-3945662.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
        "https://source.unsplash.com/1200x630/?ai,technology",
        "https://picsum.photos/1200/630?random=123456"
    ]
}

TOPICS = [
    "AI-driven gaming strategies for 2025",
    "How AI analytics change esports performance",
    "NFT game economies and automated markets",
    "Web3 bots: automation and on-chain decisions",
    "Reinforcement learning for real-time game AI",
    "DeFi bots vs game econ bots: similarities"
]

def pick_image(domain):
    pool = IMAGES.get(domain, IMAGES.get('default', []))
    if not pool:
        pool = IMAGES['default']
    return random.choice(pool)

def pick_backlinks(domain):
    others = [d for d in DOMAINS if d != domain]
    random.shuffle(others)
    selected = others[:3]
    return "\n".join([f"- [{d}](https://{d})" for d in selected])

def generate_md_for_domain(domain):
    today = datetime.date.today().isoformat()
    title = random.choice(TOPICS)
    image = pick_image(domain)
    desc = f"{title} — quick insights for practitioners."
    backlinks_md = pick_backlinks(domain)

    # Template with safe placeholders (no .format on braces)
    template = """---
layout: post
title: "__TITLE__"
date: __DATE__
author: "Alex Reed – AI Financial Analyst"
description: "__DESC__"
image: "__IMAGE__"
---

{% raw %}
_In today’s fast-moving AI-driven markets, traders and gamers are adapting faster than ever. Let’s break down what’s happening in 2025…_

{% include ad.html %}

### Fast highlights
- Model-based execution & policy learning
- Real-time risk & anomaly detection
- Low-latency pipelines for players & bots

### Why it matters
When milliseconds matter, automation is no longer optional.

---

## Related Articles (internal)
{% for p in site.posts limit:4 %}
  {% if p.url != page.url %}
  - [{{ p.title }}]({{ p.url }})
  {% endif %}
{% endfor %}

## Friendly Network Links
__BACKLINKS__
{% endraw %}
"""

    # Replace placeholders (safe, no conflict with Liquid tags)
    md = template.replace("__TITLE__", title)\
                 .replace("__DATE__", today)\
                 .replace("__DESC__", desc)\
                 .replace("__IMAGE__", image)\
                 .replace("__BACKLINKS__", backlinks_md)

    # slug for filename
    slug = title.lower().replace(" ", "-").replace("/", "-")
    filename = f"_posts/{today}-{slug}.md"
    return filename, md

def write_post_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    domain = SITE_DOMAIN or os.path.basename(os.getcwd())
    # ensure posts dir exists
    os.makedirs("_posts", exist_ok=True)

    fn, md = generate_md_for_domain(domain)
    write_post_file(fn, md)
    print("Wrote:", fn)
    # exit success
    return 0

if __name__ == "__main__":
    main()
