# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

VibeFinder 1.1

---

## 2. Goal / Task

This recommender suggests the top 5 songs for a user profile. The goal is to match the user’s vibe using genre, mood, and energy.

---

## 3. Data Used

The dataset has 18 songs from `data/songs.csv`. Each song has features like genre, mood, energy, tempo, valence, danceability, and acousticness. Most genres show up only once, so some users get limited variety.

---

## 4. Algorithm Summary

The model scores each song using simple rules. It gives +1 for a genre match and +1 for a mood match. It also adds 2 times energy similarity, so songs close to the target energy get more points. Then it sorts by score and returns the top 5.

---

## 5. Observed Behavior / Biases

For clear profiles, the results usually felt right. For edge-case profiles, the model leaned a lot on energy and repeated songs like "Gym Hero." This can create a filter-bubble effect where similar songs keep showing up. The small dataset makes this issue worse.

---

## 6. Evaluation Process

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Sad But High-Energy, and Genre-Mood Mismatch. I compared baseline weights (genre +2, mood +1, energy x1) with experiment weights (genre +1, mood +1, energy x2). I looked for whether top songs felt right and whether the same songs kept repeating.

For High-Energy Pop, "Sunrise City" at #1 made sense because it matched genre and mood and had strong energy closeness. One surprise was that "Gym Hero" still ranked high across very different profiles.

---

## 7. Intended Use and Non-Intended Use

Intended use: classroom learning, scoring experiments, and explainable recommendation demos.

Non-intended use: real-world decisions about people, production recommendation systems, or any high-stakes use case. The dataset is too small and the logic is too simple for that.

---

## 8. Ideas for Improvement

- Add tempo, valence, danceability, and acousticness to the score.
- Add a diversity rule so the same song appears less often.
- Use a larger and more balanced catalog.

---

## 9. Personal Reflection

My biggest learning moment was seeing how one weight change can shift a lot of rankings. I used AI tools to brainstorm edge-case profiles, speed up edits, and draft first-pass explanations. I still double-checked AI output by rerunning `src/main.py`, reading the score reasons, and comparing baseline vs experiment results. I was surprised that simple rules can still feel like real recommendations when they match the user profile. Next, I would test richer features and tune for both accuracy and diversity.
