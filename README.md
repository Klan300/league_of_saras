# league of saras

[![Build Status](https://travis-ci.com/Klan300/league_of_saras.svg?branch=master)](https://travis-ci.com/Klan300/league_of_saras)
[![codecov](https://codecov.io/gh/Klan300/league_of_saras/branch/master/graph/badge.svg)](https://codecov.io/gh/Klan300/league_of_saras)

## Description
League of Saras is a web-based game that lets players guess a word. This game contains many types of educational words organized by school subject. The game is played by two or more people; one player tries to guess the word, while others try to give hint without saying that word. The goal of this game is to let children have fun and gain more knowledge by the card game with their friends.
While playing this game, a player will have a time limit, the game will end when time is over. If a player guesses the correct word, the referee will click the correct button. On the other hand, if not, the referee will click on the wrong button. both buttons will step into the next word.

## Team Members
| Name                   | id         | Roles                    | GitHub                                        |
|------------------------|------------|--------------------------|-----------------------------------------------|
| Apipark Withedvorrakit | 6110546429 | Developer                | [Parkkung](https://github.com/Parkkung )                  |
| Kritpawit Soongswang   | 6110545414 | Developer                | [Kritpawit](https://github.com/kornkritpawit)              |
| Thun Thunkijjanukij    | 6110545546 | Scrum Master, Developer  | [Klan300](https://github.com/Klan300)           |
| Vichyawat Nakarugsa    | 6110545635 | Developer                | [EJEunjiyaz](https://github.com/EJEunjiyaz)     |


## Documents
- **Project Proposal**: [Google Docs](https://docs.google.com/document/d/1kjmwQOL9fKmXiI1_uqLdV-asIle4mSzEQGIRGIKzBFo/edit#)
- **Iteration plans**: [Google Docs](https://docs.google.com/document/d/1C6C2YfqwmR7YsCBz39rs0z9va9YHM7S1Zz55n6cdEh8/edit)
- **Iteration Script**: [Google Docs](https://docs.google.com/document/d/10C5QuEddw02vy9iqMQmwP2vWviJNh3yp-Oah81X_mXQ/edit?usp=sharing)
- **Task Board**: [Trello](https://trello.com/b/5IZQzFnU/league-of-saras)
- **Code Review Script and Checklist**: [Google Docs](https://docs.google.com/document/d/1zPOBC1oeVHnR0qHtA764ClV9Aj7-xVub59CRoCc4p6o/edit?usp=sharing)
- **Sprint Retrospective and Milestones**: [Google Docs](https://docs.google.com/document/d/16zYudrIcDCM-InB-exEYpuzSn05VFGZU2sFMxBeu_Aw/edit?usp=sharing)

## Get started (run locally)
1. Clone this repository to your local machine and change the directory to `league_of_saras` directory.
    ```
    $ git clone https://github.com/Klan300/league_of_saras.git
    ```
2. Use virtualenv in the directory by this command.
    ```
    $ virtualenv venv
    ```
3. Install requirements package.
    ```
    (venv) pip install -r requirements.txt
    ```
4. Migrate the data to your database.
    ```
    (venv) python manage.py migrate
    ```
5. Run the server and enjoy the experience.
    ```
    (venv) python manage.py runserver
    ```
    After runserver, you will see the server run at default URL in your local machine. You can access by that shown URL.