import os

# Path to the folder where movie images are stored
image_folder = '../pics.html'

# Get the list of all files in the image folder that are .jpg files
movies = []
for file_name in os.listdir(pics):
    if file_name.endswith('.jpg'):  # Check if the file is a .jpg image
        # Remove the file extension to use it as the movie title
        movie_title = file_name.replace('.jpg', '').replace('_', ' ').title()
        movies.append({"title": movie_title, "file_name": file_name.replace('.jpg', '')})

# Template for the download page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediaPort - Movies</title>
    <link rel="stylesheet" type="text/css" href="../css/movies.css">
</head>
<body>
    <header>
        <h1>MediaPort</h1>
        <nav>
            <ul>
                <li><a href="../index.html">HOME</a></li>
                <li><a href="../html/audio.html">AUDIO</a></li>
                <li><a href="../html/videos.html">VIDEOS</a></li>
                <li><a href="../html/movies.html">MOVIES</a></li>
                <li><a href="../html/feedback.html">FEEDBACK</a></li>
                <li><a href="../html/about.html">ABOUT</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="movie">
            <h1>Available Movies</h1>
            <div class="row">
"""

# Generate movie blocks dynamically from the list of movies
for i, movie in enumerate(movies, start=1):
    html_template += f"""
                <div class="movie-col">
                    <a href="download.html?movie_id={i}">
                        <img src="../{image_folder}{movie['file_name']}.jpg" width="300px" height="200px" alt="{movie['title']}">
                        <p><b>{movie['title']}</b></p>
                    </a>
                </div>
    """

# Close the HTML structure
html_template += """
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 MediaPort. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Save the generated HTML to a file
output_file = "movies.html"
with open(output_file, "w") as file:
    file.write(html_template)

print(f"{output_file} has been generated with {len(movies)} movies!")
