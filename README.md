# python_algo_project

Django app using SQLite and Bootstrap

### User Story

Search collection of algorithms by tag, language, or title

Challenge yourself with a random algorithm

Show and hide the solution

Enjoy the aesthetically pleasing format of the solution, thanks to Ace in-browser editor

Toggle between Night and Day Mode on the algorithm page!

### Technical Points of Interest

Model relationships defined such that algorithms can have many tags and many solutions in different languages

The database has four tables: Algorithms, Solutions, Tags, and Languages
- Algorithms have a many-to-many relationship with tags
- Algorithms have a one-to-many relationship with solutions
- Languages have a one-to-many relationship with solutions

CRUD operations are handled with Django admin, replacing the original manually coded CRUD operations (original design remains commented in codebase)

Show / hide feature for the solution is handled using jQuery, minimizing requests to the server

Ace editors are created dynamically for each solution using jQuery in conjunction with Django-embedded HTML

Switching between Day and Night modes uses Ace built-in methods and jQuery to change the HTML and editor themes
