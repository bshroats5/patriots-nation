from flask import Flask, render_template
import os

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'title': 'Soccer teams win MSC Championships',
        'date': 'November 14, 2024',
        'author': 'Bret Shroats',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.',
        'slug': 'exciting-game-highlights'
    },
    {
        'title': 'Player Spotlight: John Doe',
        'date': 'January 2, 2023',
        'author': 'Author Name',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.',
        'slug': 'player-spotlight-john-doe'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<slug>')
def post(slug):
    post = next((p for p in posts if p['slug'] == slug), None)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)