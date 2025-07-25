import os

# Define the project structure
folders = [
    "francis_ndegwa_portfolio/static/css",
    "francis_ndegwa_portfolio/static/js",
    "francis_ndegwa_portfolio/static/img/projects",
    "francis_ndegwa_portfolio/static/pdfs",
    "francis_ndegwa_portfolio/templates",
    "francis_ndegwa_portfolio/assets/wireframes",
    "francis_ndegwa_portfolio/assets/brand",
    "francis_ndegwa_portfolio/venv"  # Placeholder; virtualenv created manually
]

files = {
    "francis_ndegwa_portfolio/app.py": '''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
''',

    "francis_ndegwa_portfolio/requirements.txt": "flask\n",

    "francis_ndegwa_portfolio/README.md": "# Francis Ndegwa Portfolio\n\nThis is a personal portfolio website built with Flask.",

    "francis_ndegwa_portfolio/.gitignore": "venv/\n__pycache__/\n*.pyc\n*.pyo\n.env\n.DS_Store\n",

    "francis_ndegwa_portfolio/templates/base.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Francis Ndegwa Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/script.js') }}" defer></script>
</head>
<body>
    <header>
        <h1>Francis Ndegwa</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>© 2025 Francis Ndegwa. All rights reserved.</p>
    </footer>
</body>
</html>
''',

    "francis_ndegwa_portfolio/templates/index.html": '''{% extends "base.html" %}
{% block content %}
<h2>Welcome</h2>
<p>This is the home page of my portfolio.</p>
{% endblock %}''',

    "francis_ndegwa_portfolio/templates/about.html": '''{% extends "base.html" %}
{% block content %}
<h2>About Me</h2>
<p>This is the about page of my portfolio.</p>
{% endblock %}''',

    "francis_ndegwa_portfolio/templates/projects.html": '''{% extends "base.html" %}
{% block content %}
<h2>Projects</h2>
<p>This is the projects page of my portfolio.</p>
{% endblock %}''',

    "francis_ndegwa_portfolio/templates/contact.html": '''{% extends "base.html" %}
{% block content %}
<h2>Contact</h2>
<p>This is the contact page of my portfolio.</p>
{% endblock %}''',

    "francis_ndegwa_portfolio/static/css/style.css": '''body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 0;
    color: #333;
}

header {
    background-color: #004080;
    color: white;
    padding: 1rem;
    text-align: center;
}

nav a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}

main {
    padding: 20px;
}

footer {
    background-color: #ddd;
    text-align: center;
    padding: 10px;
}
''',

    "francis_ndegwa_portfolio/static/js/script.js": '''console.log("Francis Ndegwa Portfolio loaded.");'''
}


def create_project():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for filepath, content in files.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Created file: {filepath}")

    print("\n✅ Project structure created successfully!")
    print("👉 Next step: Activate virtualenv, install Flask, and run app.py")


if __name__ == "__main__":
    create_project()
