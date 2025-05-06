import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes"
tables = pd.read_html(URL)          # grab everything

frames = []
for t in tables:
    # keep columns whose header mentions 'viewers'
    vcols = [c for c in t.columns if isinstance(c, str) and "viewers" in c.lower()]
    if not vcols:
        continue                    # skip non-episode tables
    frame = t[[t.columns[0], vcols[0]]].copy()
    frame.columns = ["episode_overall", "viewers_millions"]
    frames.append(frame)

df = pd.concat(frames, ignore_index=True)
df.to_csv("data/bb_viewership.csv", index=False)
print(f"Saved {len(df)} episodes → data/bb_viewership.csv")
