from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'title': 'Soccer Teams Win MSC Championships',
        'date': 'November 14, 2024',
        'author': 'Bret Shroats',
        'content': (
            "This year, both the men's and women's soccer teams won the MSC Championships.\n"
            "The men's team triumphed 4-2 in penalty kicks against the Lindsey Wilson Blue Raiders, "
            "while the women's team secured a 2-0 victory over Cumberland University.\n"
            "Both teams will advance to the NAIA National Championships in Orange Beach, Alabama.\n"
            "The men's team will play their first game on November 18, and the women's team will play their first game on November 19.\n"
            "Go Knights!"
        ),
        'slug': 'soccer-teams-win-msc-championships'
    },
    {
        'title': 'Player Spotlight: John Doe',
        'date': 'January 2, 2023',
        'author': 'Author Name',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.',
        'slug': 'player-spotlight-john-doe'
    }
]

@app.route('/post/<slug>')
def post(slug):
    post = next((item for item in posts if item["slug"] == slug), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)