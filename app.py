from flask import Flask, render_template
import os

app = Flask(__name__)

# Sample data for blog posts
posts = [
    {
        'title': 'Soccer teams win MSC Championships',
        'date': 'November 18, 2024',
        'author': 'Bret Shroats',
        'content': 'The men and Women/s Cumberlands Patriots soccer teams won their Mid-South Conference titles on November 13th. It was the first time both soccer teams had won the Mid-South Conference since 2020. The Women/s team stayed undefeated by beating the always-tough Cumberland Phoenix 4-1. Jayden Boelter led the Patriots with goals in the 30th and 70th minutes as she continues to shatter the school record of goals in a season and a career at UC. Just 2 minutes after Jayden scored the match/s first goal, Nicole Araujo added a goal to double the lead. However, 3 minutes later, the Phoenix would cut the lead in half with a goal from Gabby Jones. The Pats would go into halftime up 2-1. Then, like in the first half, Boelter opens up the scoring with her 70th-minute goal. Then, just 4 minutes later, Alba Ramirez got her first goal of the season to give the Pats their 4-1 win and the MSC Title. The Lady Patriots will host Saturday the winner of the Hastings vs. Olivet Nazarene on Thursday. The Mens match would contain more drama as they went up against #1 seed Lindsey Wilson. The Blue Raiders wasted no time going up 1-0 in the 1st minute of the match. They would maintain that 1-0 lead until the 41st minute when the Patriots would get an equalizer from Carlos Diez Herrero. The teams would play the next 68- minutes equally, and the match would head into penalty kicks. The Patriots would show dominance, winning 4-2 and bringing home their first title since 2020. They will host the winner of the Rio Grande vs Bryan match on Saturday, which will be played in Williamsburg on Thursday at 3 PM. ',
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)