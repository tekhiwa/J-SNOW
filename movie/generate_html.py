import os
import re  # For using regular expressions

# Path to the folder where movie images are stored
image_folder = '../movie/posters/'

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
<html>
<head>
  <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-G0XGGE2R86"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-G0XGGE2R86');
</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="../css/style.css">
<link rel="stylesheet" type="text/css" href="../css/Movie.css">
<style>
</style>
</head>
<body style="font-family:Verdana;">

<div style="background-color:brown;padding:15px; border-radius: 5px;">
  <h1>Media Port</h1>
  <h3>The Home Of Entertainment</h3>
</div>

<div style="overflow:auto">
  <div class="menu">
    <div class="menuitem"><a href="../index.html">Home</a></div>
    <div class="menuitem"><a href="../html/movies.html">Movies</a></div>
    <div class="menuitem"><a href="../html/videos.html">Videos</a></div>
    <div class="menuitem"><a href="../html/audios.html">Audios</a></div>
    <div class="menuitem"><a href="../html/feedback.html">Feedback</a></div>
    <div class="menuitem"><a href="../html/about.html">About us</a></div>
  </div>

  <div class="main">
    <div class="row">
"""

# Generate movie blocks dynamically from the list of movies
for movie in movies:
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
  </div>

  <div class="right">
    <div style="position: relative;">
    <h2>What's new today?</h2>
    <p>Eli Njuchi JU.</p>
    <p>Saint Una.</p>
    <a href="../html/most trend.html"> Most Trending </a>
    <p>Onessmas controller.</p>
    <h2>Most downloaded?</h2>
    <p>Movie: fighting in a park!</p>
    <p>Audio: Martse mwapindulanji</p>
  </div>
  </div>
</div>

<script>
  const audioElements = document.querySelectorAll('audio');
  audioElements.forEach((audio) => {
    audio.addEventListener('play', () => {
      audioElements.forEach((otherAudio) => {
        if (otherAudio !== audio) {
          otherAudio.pause();
        }
      });
    });
  });
</script>

</body>

<footer>
  <div style="background-color:brown;text-align:center;padding:10px;margin-top:7px;font-size:20px; color: white; padding-bottom: 10px;"> Media Port 2024</div>
</footer>
</html>
"""

# Save the generated movie list HTML to a file
output_file = "movies.html"
with open(output_file, "w") as file:
    file.write(html_template)

print(f"{output_file} has been generated with {len(movies)} movies!")
