#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final fixed version for botgame.io (Netlify + Jekyll compatible)
- Fixed: Liquid tags now render correctly
- Includes ad and related posts
- Google Analytics can be included via _includes/analytics.html
"""

import os
import datetime
import random

SITE_DOMAIN = os.environ.get("SITE_DOMAIN", "").strip() or os.path.basename(os.getcwd())

DOMAINS = [
    'botgame.io', 'metaversebot.io', 'nftgameai.com', 'hubgaming.io',
    'botdefi.io', 'esportsai.io', 'nftgamepro.com', 'botesports.com',
    'aiesports.io', 'pronftgame.com', 'botplay.io', 'botweb3ai.com',
    'botblockchain.io'
]

IMAGES = {
    'botgame.io': [
        "https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop",
        "https://source.unsplash.com/1200x630/?esports,ai,bot",
        "https://picsum.photos/1200/630?random=88888"
    ],
    'default': [
        "https://source.unsplash.com/1200x630/?ai,gaming",
        "https://picsum.photos/1200/630?random=12345"
    ]
}

TOPICS = [
    "AI-powered Esports Analytics for 2025",
    "How Automation Shapes the Future of Gaming",
    "Reinforcement Learning in Competitive Play",
    "Smarter Bots, Smarter Players: The AI Era",
    "Web3 Meets Esports: Smart Gaming Economies",
    "The Rise of AI-driven Esports Coaches"
]


def pick_image(domain):
    pool = IMAGES.get(domain, IMAGES['default'])
    return random.choice(pool)


def pick_backlinks(domain):
    others = [d for d in DOMAINS if d != domain]
    random.shuffle(others)
    return "\n".join([f"- [{d}](https://{d})" for d in others[:3]])


def generate_md(domain):
    today = datetime.date.today().isoformat()
    title = random.choice(TOPICS)
    image = pick_image(domain)
    desc = f"{title} — insights from {domain}"
    backlinks = pick_backlinks(domain)

    md = f"""---
layout: post
title: "{title}"
date: {today}
author: "Alex Reed – AI Esports Analyst"
description: "{desc}"
image: "{image}"
---

_In today’s fast-moving AI-driven markets, gamers and analysts are adapting faster than ever. Let’s break down what’s changing in 2025…_

{{% include ad.html %}}

### What’s Changing Right Now?

AI is accelerating decision-making, improving latency, and reshaping strategies across esports.

1) **Model-driven gaming**
   Machine learning enables smarter in-game behavior and real-time predictions.

2) **Better strategy automation**
   Adaptive algorithms now analyze patterns faster than humans can react.

3) **Real-time analytics**
   Data pipelines provide instant insights — critical for professional gamers.

---

## Related Articles (internal)
{{% for p in site.posts limit:4 %}}
  {{% if p.url != page.url %}}
  - [{{{{ p.title }}}}]({{{{ p.url }}}})
  {{% endif %}}
{{% endfor %}}

## Friendly Network Links
{backlinks}

{{% include analytics.html %}}
"""

    slug = title.lower().replace(" ", "-").replace("/", "-")
    path = f"_posts/{today}-{slug}.md"
    return path, md


def main():
    os.makedirs("_posts", exist_ok=True)
    fn, content = generate_md(SITE_DOMAIN)
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Wrote:", fn)


if __name__ == "__main__":
    main()
