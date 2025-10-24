#!/usr/bin/env python3
# Auto post generator for botgame.io
import os, datetime, random

CURRENT_DOMAIN = "botgame.io"
DOMAINS = [
    'metaversebot.io', 'nftgameai.com', 'hubgaming.io', 'botdefi.io',
    'esportsai.io', 'nftgamepro.com', 'botesports.com', 'aiesports.io',
    'pronftgame.com', 'botplay.io', 'botweb3ai.com', 'botblockchain.io'
]

IMAGES = [
    'https://images.pexels.com/photos/907221/pexels-photo-907221.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop',
    'https://source.unsplash.com/1200x630/?esports,ai,game',
    'https://picsum.photos/1200/630?random=772535'
]

TOPICS = [
    "AI-driven esports analytics for 2025",
    "Smarter bots and balance in pro gaming",
    "How AI predicts player performance in real-time",
    "Automation meets esports: the next wave",
    "Game data modeling with deep learning",
]

def pick_image():
    return random.choice(IMAGES)

def pick_backlinks():
    random.shuffle(DOMAINS)
    return "\n".join([f"- [{d}](https://{d})" for d in DOMAINS[:3]])

def generate_md():
    today = datetime.date.today().isoformat()
    title = random.choice(TOPICS)
    image = pick_image()
    desc = f"{title} — AI insights from botgame.io"
    backlinks = pick_backlinks()

    md = """---
layout: post
title: "{title}"
date: {date}
author: "Alex Reed – AI Esports Analyst"
description: "{desc}"
image: "{image}"
---

In today’s AI-driven gaming world, automation and analytics define performance and strategy.

{% include ad.html %}

### Highlights
- Smarter prediction models
- Reinforcement learning for esports
- AI-enhanced reaction analysis

---

## Related Network
{backlinks}
""".format(title=title, date=today, desc=desc, image=image, backlinks=backlinks)

    slug = title.lower().replace(" ", "-").replace("/", "-")
    return f"_posts/{today}-{slug}.md", md

def main():
    os.makedirs("_posts", exist_ok=True)
    fn, content = generate_md()
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Generated:", fn)

if __name__ == "__main__":
    main()
