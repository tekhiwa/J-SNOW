import os
from urllib.parse import unquote
import sys

# Define the folder where movie images and files are stored
movies_folder = r"E:\J SNOW\WEB PROJECT\MEDIAPORT\NEW FOLDER (3)\movies\posters"
output_html_file = r"E:\J SNOW\WEB PROJECT\MEDIAPORT\NEW FOLDER (3)\movies\search_results.html"

# Simulating the query being passed via URL
if len(sys.argv) > 1:
    query = sys.argv[1].strip().lower()  # Get query from the command-line arguments
else:
    query = ''  # Default to an empty query if none is provided

# Unquote any URL encoded characters
query = unquote(query)

# List all movies in the folder
movies = os.listdir(movies_folder)

# Filter the movies based on the search query (exact or close match)
# We'll match if the movie title starts with the query or if it is exactly equal to the query
matching_movies = [
    movie for movie in movies 
    if movie.lower().startswith(query) or movie.lower() == query and movie.endswith(('.jpg', '.png'))
]

# Start the HTML content for the search results page
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
    <link rel="stylesheet" type="text/css" href="../css/movies.css">
</head>
<body>
    <header>
        <h1>MediaPort - Search Results</h1>
        <nav>
            <ul>
                <li><a href="../index.html">HOME</a></li>
                <li><a href="../html/audio.html">AUDIO</a></li>
                <li><a href="../html/videos.html">VIDEOS</a></li>
                <li><a href="../html/movies.html">MOVIES</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="movie">
            <h1>Results for '{}'</h1>
            <div class="row">
""".format(query)

# If there are matching movies, display them
if matching_movies:
    for i, movie in enumerate(matching_movies):
        movie_id = i + 1
        html_content += f"""
                <div class="movie-col">
                    <a href="download.html?movie_id={movie_id}">
                        <img src="../pics/{movie}" width="300px" height="200px" alt="{movie}">
                        <p><b>{os.path.splitext(movie)[0]}</b></p>
                    </a>
                </div>
        """
else:
    html_content += "<p>No movies found matching your search query.</p>"

# Close the HTML tags
html_content += """
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 MediaPort. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Write the search results to the HTML file
with open(output_html_file, 'w') as file:
    file.write(html_content)

print(f"Search results page generated at {output_html_file}")
