import os 
import re  # For using regular expressions

# Path to the folder where movie images are stored
image_folder = '../movies/posters/'

# Get the list of all files in the image folder that are .jpg files
movies = []
for file_name in os.listdir(image_folder):
    if file_name.endswith('.jpg'):
        # Remove the file extension and replace underscores with spaces
        base_name = file_name.replace('.jpg', '').replace('_', ' ')

        # Use regex to clean up the title: Match the title until the year (XXXX)
        match = re.match(r'(.+?)(\(\d{4}\))', base_name)

        if match:
            # Extract the movie title and year (group 1 + group 2)
            movie_title = f"{match.group(1).strip()} {match.group(2)}"
        else:
            # If no year is found, just use the cleaned base name
            movie_title = base_name.title()

        # Assuming movie download files have .mp4 extensions
        download_link = file_name.replace('.jpg', '.mp4')

        # Append the movie to the list with the cleaned-up title
        movies.append({"title": movie_title, "file_name": file_name.replace('.jpg', ''), "download_link": download_link})

# Template for the movie list page
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediaPort - Movies</title>
    <link rel="stylesheet" type="text/css" href="../movies/movies.css">
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
                    <a href="download.html?title={movie['title']}&image={movie['file_name']}.jpg&download={movie['download_link']}">
                        <img src="{image_folder}{movie['file_name']}.jpg" width="300px" height="200px" alt="{movie['title']}">
                        <p><b>{movie['title']}</b></p>
                    </a>
                </div>
    """

# Close the HTML structure for the main movie list page
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

# Save the generated movie list HTML to a file
output_file = "movies.html"
with open(output_file, "w") as file:
    file.write(html_template)

print(f"{output_file} has been generated with {len(movies)} movies!")
