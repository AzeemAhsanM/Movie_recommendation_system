from flask import Flask, render_template, request
from backend import recommend_movies, get_all_titles

app = Flask(__name__)

# Load all titles once, for autocomplete
ALL_TITLES = get_all_titles()


@app.route("/", methods=["GET", "POST"])
def home():
    movie_name = ""
    recommendations = []
    error = ""

    if request.method == "POST":
        movie_name = request.form.get("movie_name", "").strip()

        if not movie_name:
            error = "Please type a movie name."
        else:
            recommendations = recommend_movies(movie_name)
            if not recommendations:
                error = "Sorry, I couldn't find that movie in the database."

    return render_template(
        "index.html",
        movie_name=movie_name,
        recommendations=recommendations,
        error=error,
        all_titles=ALL_TITLES,  # 👈 pass titles to template
    )


if __name__ == "__main__":
    # for local testing
    app.run(host="0.0.0.0", port=5000, debug=True)
