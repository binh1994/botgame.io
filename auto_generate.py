#!/usr/bin/env python3
# Auto post daily (OpenAI optional). Falls back to templated content.
import os, datetime, random

DOMAINS = ['botgame.io', 'metaversebot.io', 'nftgameai.com', 'hubgaming.io', 'botdefi.io', 'esportsai.io', 'nftgamepro.com', 'botesports.com', 'aiesports.io', 'pronftgame.com', 'botplay.io', 'botweb3ai.com', 'botblockchain.io']   # injected list of domains for backlinks
IMAGES = {'botgame.io': ['https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?esports', 'https://picsum.photos/1200/630?random=772535'], 'metaversebot.io': ['https://images.pexels.com/photos/8132695/pexels-photo-8132695.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?metaverse', 'https://picsum.photos/1200/630?random=185474'], 'nftgameai.com': ['https://images.pexels.com/photos/8370753/pexels-photo-8370753.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?nft', 'https://picsum.photos/1200/630?random=797807'], 'hubgaming.io': ['https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?esports', 'https://picsum.photos/1200/630?random=351547'], 'botdefi.io': ['https://images.pexels.com/photos/6770612/pexels-photo-6770612.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?defi', 'https://picsum.photos/1200/630?random=416338'], 'esportsai.io': ['https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?esports', 'https://picsum.photos/1200/630?random=210263'], 'nftgamepro.com': ['https://images.pexels.com/photos/8370753/pexels-photo-8370753.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?nft', 'https://picsum.photos/1200/630?random=915557'], 'botesports.com': ['https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?esports', 'https://picsum.photos/1200/630?random=462161'], 'aiesports.io': ['https://images.pexels.com/photos/3945662/pexels-photo-3945662.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://images.pexels.com/photos/7915359/pexels-photo-7915359.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?gaming', 'https://picsum.photos/1200/630?random=700664'], 'pronftgame.com': ['https://images.pexels.com/photos/3945662/pexels-photo-3945662.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://images.pexels.com/photos/7915359/pexels-photo-7915359.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?gaming', 'https://picsum.photos/1200/630?random=903151'], 'botplay.io': ['https://images.pexels.com/photos/3945662/pexels-photo-3945662.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://images.pexels.com/photos/7915359/pexels-photo-7915359.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?gaming', 'https://picsum.photos/1200/630?random=471285'], 'botweb3ai.com': ['https://images.pexels.com/photos/844124/pexels-photo-844124.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?web3', 'https://picsum.photos/1200/630?random=640141'], 'botblockchain.io': ['https://images.pexels.com/photos/6770615/pexels-photo-6770615.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop', 'https://source.unsplash.com/1200x630/?blockchain', 'https://picsum.photos/1200/630?random=892476']}     # injected dict domain->image pool

TOPICS = [
  "AI-driven trading playbook for 2025",
  "How AI agents boost esports performance",
  "NFT + AI: smarter collectibles and gaming",
  "Web3 automation: bots, risk & execution",
  "Reinforcement Learning for real-time markets",
  "DeFi alpha: market-making & liquidity bots",
  "Edge analytics for bots and players",
]

def pick_image(domain):
    pool = IMAGES.get(domain, [])
    if pool:
        return random.choice(pool)
    return "https://picsum.photos/1200/630?random=" + str(random.randint(1,999999))

def pick_backlinks(domain):
    others = [d for d in DOMAINS if d != domain]
    random.shuffle(others)
    take = others[:3]
    return "\n".join([f"- [{d}](https://{d})" for d in take])

def generate_md(domain):
    today = datetime.date.today().isoformat()
    title = random.choice(TOPICS)
    image = pick_image(domain)
    desc = title + " — quick insights for practitioners."
    keywords = "AI, trading, gaming, blockchain, automation"
    backlinks = pick_backlinks(domain)

    md = \"\"\"---
layout: post
title: \"__TITLE__\"
date: __DATE__
author: "Alex Reed – AI Financial Analyst"
description: "__DESC__"
image: "__IMAGE__"
---

_In today’s fast-moving AI-driven markets, traders are adapting faster than ever. Let’s break down what’s happening in 2025…_

{% raw %}{% include ad.html %}{% endraw %}

### Fast highlights
- Model-based execution & policy learning
- Real-time risk & anomaly detection
- Low-latency pipelines for gamers & traders

### Why it matters
When milliseconds matter, automation is no longer optional.

---

## Related Articles (internal)
{% raw %}{% for p in site.posts limit:4 %}{% endraw %}
  {% raw %}{% if p.url != page.url %}{% endraw %}
  - [{{ p.title }}]({{ p.url }})
  {% raw %}{% endif %}{% endraw %}
{% raw %}{% endfor %}{% endraw %}

## Friendly Network Links
__BACKLINKS__
\"\"\".replace("__TITLE__", title).replace("__DATE__", today).replace("__DESC__", desc).replace("__IMAGE__", image).replace("__BACKLINKS__", backlinks)

    slug = title.lower().replace(" ","-").replace("/","-")
    return f"_posts/{today}-{slug}.md", md

def main():
    domain = os.environ.get("SITE_DOMAIN","").strip()
    if not domain:
        domain = os.path.basename(os.getcwd())
    os.makedirs("_posts", exist_ok=True)
    fn, content = generate_md(domain)
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print("Wrote:", fn)

if __name__ == "__main__":
    main()
