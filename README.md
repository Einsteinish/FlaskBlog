# FlaskBlog:
- simple blog  written in [Flask](http://flask.pocoo.org/)
- Used for [Memonimo.com](http://memonimo.com/)

# Under the hood:
- [Python](http://python.org/)
- [Flask](http://flask.pocoo.org/)
- [MongoDB](http://www.mongodb.org/)
- [Bootstrap 3](http://getbootstrap.com/)
- [jQuery](http://jquery.com)
- [Lightbox 2](https://github.com/lokesh/lightbox2)
- [Markdown](http://daringfireball.net/projects/markdown/syntax)
- [Polymer](http://www.polymer-project.org)

# What it can:
- create/preview/update/delete articles;
- create/update/delete users;
- search;
- atom feed.

# It contains:
- WYSIWYG Markdown editor;
- [AddThis](http://www.addthis.com/) social buttons;
- [Gravatar](http://gravatar.com) for userpic.


# Requirements:
- mongoDB >= 2.2


# Installation:

[Guide](http://bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB.php) Flask "Blog App" with MongoDB ;


After this edit the `config.py` file

- Replace the `CONNECTION_STRING` variable with your own connection string;

- Replace the `DATABASE` variable to your own one;

- If the default collection names don't work for you please replace the `POSTS_COLLECTION`, `USERS_COLLECTION` and `USERS_COLLECTION` variables to any names you like;

- If you use this code on a production sever replace the `DEBUG` variable with `False`.

# Run:
Start `mongod`, then when you are in project directory with actived environment just type in terminal

`python __init__.py`


or

`gunicorn __init__:app`


# Usage:
When you run the application for the first time the "Install" page appears. You need to create a user profile and set some display settings on this page.

![install_page](http://i.imgur.com/gkWI10v.png)

If you have an account on [Gravatar](http://gravatar.com) and your logged-in email links to it, the userpic will display. It will be a random gravatar image if it doesn't.

All necessary MongoDB indexes will be created during the installation. A test text post will be created as well.

There should be at least one post and one user for the database to be installed. That is why it's impossible to delete the last post or user.

If you want to start it from scratch please remove all existing collections from your database and delete the browser session cookie. The Install page will show up again.

# Tutorials:
- [Part 1](http://bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB.php) Flask "Blog App" with MongoDB (Local via Flask server)
- [Part 2](http://bogotobogo.com/python/Flask/Python_Flask_Blog_App_with_MongoDB_and_Apache_WSGI.php) Flask "Blog App" with MongoDB on Ubuntu 14 (Local Apache WSGI)
- [Part 3](http://bogotobogo.com/python/Flask/Python_Flask_Blog_App_Production_with_MongoDB_and_Apache_WSGI.php) Flask "Blog App" with MongoDB on CentOS 7 (Production Apache WSGI)
