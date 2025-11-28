# Movie Recommendation System 🎬

A small Streamlit-based movie recommender that suggests similar movies by analyzing movie metadata (genres, keywords, tagline, cast and director) using TF–IDF and cosine similarity. The app takes a movie title as input and returns a ranked list of similar movies from the bundled dataset (`movies.csv`).

## Key features

- Simple web UI built with Streamlit.
- Content-based recommendation using TF–IDF vectors and cosine similarity.
- Genre weighting to increase the importance of genres in recommendations.
- Fuzzy matching for user input (uses Python's `difflib`) so small typos still work.

## Built with

- Python
- Streamlit
- pandas, numpy
- scikit-learn (TF-IDF, cosine similarity)

## Files in this repository

- `app.py` — Streamlit app entrypoint.
- `backend.py` — Recommendation logic (loads `movies.csv`, builds TF-IDF features, computes similarity, exposes `recommend_movies`).
- `movies.csv` — Movie dataset used by the recommender (must be present in the project root).
- `requirements.txt` — Python dependencies.

## Quick start (Windows / PowerShell)

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .ven
.\.ven\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501) to use the app.

## Using the app

1. Type a movie name in the input box (partial names and small typos are tolerated).
2. Click the "Recommend" button.
3. The app displays a ranked list of recommended movies similar to the input.

If the app cannot find a close match for your input title, it will show an error message.

## How the recommender works (short)

1. `backend.py` loads `movies.csv` into a pandas DataFrame. Selected textual features are: `genres`, `keywords`, `tagline`, `cast`, and `director`.
2. Genres are repeated (multiplied) to give them additional weight when building TF–IDF vectors. This behavior is controlled by the `GENRE_WEIGHT` constant in `backend.py`.
3. All selected features are concatenated into a single combined-string per movie.
4. A TF–IDF vectorizer converts the combined text into numeric feature vectors.
5. Cosine similarity between vectors is computed, producing a similarity matrix.
6. For a user-supplied title, `difflib.get_close_matches` finds the closest matching title in the dataset. The app then looks up that movie's similarity scores and returns the top N movies ranked by similarity.

## API / Developer notes

- The main callable function is `recommend_movies(movie_name: str, num_recommendations: int = 10) -> list` exposed from `backend.py`.
- Important parameters you can tweak in `backend.py`:
	- `GENRE_WEIGHT` — numeric weight to repeat genre text (default: 3). Increasing this gives genres more influence.
	- `num_recommendations` — number of movies returned by `recommend_movies`.

Edge cases handled:
- Empty input returns an empty list.
- No close title match returns an empty list (the Streamlit UI shows an error message).

## Dataset

This project expects a `movies.csv` file in the project root with at least the following columns (the included dataset in this repo contains many more fields):

- `index` (unique integer for each movie) — used to map rows to the computed similarity matrix.
- `title` — movie title used for matching and display.
- `genres`, `keywords`, `tagline`, `cast`, `director` — textual fields used to compute content similarity.

If you replace `movies.csv`, make sure it contains these columns or adjust `backend.py` accordingly.

## Troubleshooting

- If Streamlit fails to run, ensure your virtual environment is active and dependencies from `requirements.txt` are installed.
- If the app shows no recommendations for a title you expect to find, open `movies.csv` and verify the exact title spelling. The app uses fuzzy matching but it relies on titles present in the dataset.

## Contributing

Contributions are welcome. Suggested small improvements:

- Improve the dataset (more metadata, cleaner text fields).
- Add caching for TF–IDF vectorization to speed up cold starts.
- Add unit tests for `recommend_movies`.

When submitting changes, please open a pull request and describe the intent and testing steps.

## License

This project is provided under the MIT License. Feel free to reuse and adapt.

---


