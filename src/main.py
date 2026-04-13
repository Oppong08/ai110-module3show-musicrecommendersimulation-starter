"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from recommender import load_songs, recommend_songs
except ModuleNotFoundError:
    from src.recommender import load_songs, recommend_songs


TEST_PROFILES = [
    {
        "name": "High-Energy Pop",
        "prefs": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.92,
            "target_tempo_bpm": 128,
            "target_valence": 0.88,
            "target_danceability": 0.86,
            "target_acousticness": 0.10,
            "genre": "pop",
            "mood": "happy",
            "energy": 0.92,
        },
    },
    {
        "name": "Chill Lofi",
        "prefs": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.28,
            "target_tempo_bpm": 78,
            "target_valence": 0.40,
            "target_danceability": 0.45,
            "target_acousticness": 0.84,
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.28,
        },
    },
    {
        "name": "Deep Intense Rock",
        "prefs": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.88,
            "target_tempo_bpm": 145,
            "target_valence": 0.45,
            "target_danceability": 0.62,
            "target_acousticness": 0.12,
            "genre": "rock",
            "mood": "intense",
            "energy": 0.88,
        },
    },
    {
        "name": "Edge Case: Sad But High-Energy",
        "prefs": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.95,
            "target_tempo_bpm": 90,
            "target_valence": 0.15,
            "target_danceability": 0.78,
            "target_acousticness": 0.18,
            "genre": "pop",
            "mood": "sad",
            "energy": 0.95,
        },
    },
    {
        "name": "Edge Case: Genre-Mood Mismatch",
        "prefs": {
            "favorite_genre": "classical",
            "favorite_mood": "party",
            "target_energy": 0.52,
            "target_tempo_bpm": 110,
            "target_valence": 0.50,
            "target_danceability": 0.50,
            "target_acousticness": 0.50,
            "genre": "classical",
            "mood": "party",
            "energy": 0.52,
        },
    },
]


def main() -> None:
    songs = load_songs("data/songs.csv")

    print("\n" + "=" * 70)
    print("STRESS TEST: DIVERSE USER PROFILES")
    print("=" * 70)

    for profile in TEST_PROFILES:
        profile_name = profile["name"]
        user_prefs = profile["prefs"]
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nProfile: {profile_name}")
        print("-" * 70)

        for index, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

            print(f"{index}. {song['title']}")
            print(f"   Final Score: {score:.2f}")
            print("   Reasons:")
            for reason in reasons:
                print(f"   - {reason}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
