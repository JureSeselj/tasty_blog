![Logo](./static/images/logos/apple-touch-icon.png)
# Tasty Blog 

# Goal for this Project
Welcome to Tasty Blog, this project is a Full Stack website built using the Django framework. Tasty Blog 
is a recipe book where users can look or search for a recipe to prepare. When the user is logged in they can also 
like/unlike a post and comment on a post. They can also share their favourite cookbooks by adding a post 
on the Books Page and upload or update their user image and details.

[Live Project Here](https://tasty-blog-app.herokuapp.com/)

<p align="center"><img src="./assets/readme/features/tasty-blog-responsive.png"
        alt="Tasty Blog webpage on multiple devices"></p>

# Table of Contents
- [Tasty Blog - Introduction](#tasty-blog---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
      - [Main Site Goals](#main-site-goals)
  - [Design](#design)
      - [Colours](#colours)
      - [Typography](#typography)
      - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
    - [Home Page - Highlight Posts](#home-page---highlight-posts)
    - [About Page](#about-page)
    - [Blog Page](#blog-page)
    - [Post Detail Page - Top](#post-detail-page---top)
    - [Post Detail Page - Steps](#post-detail-page---steps)
    - [Post Detail Page - Comments](#post-detail-page---comments)
    - [Edit Comments Page](#edit-comments-page)
    - [Contact Page](#contact-page)
    - [Categories Page](#categories-page)
    - [Categories Results](#categories-results)
    - [Books Page](#books-page)
    - [Add/Edit Books Page](#addedit-books-page)
    - [Search Box](#search-box)
    - [Search Results Page](#search-results-page)
    - [Search Results - Input Empty](#search-results---input-empty)
    - [Search Results - No Results Found](#search-results---no-results-found)
    - [Signup Page](#signup-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [User Profile Page](#user-profile-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
  - [Messages and Interaction With Users](#messages-and-interaction-with-users)
    - [Sign up](#sign-up)
    - [Login](#login)
    - [Logout](#logout)
    - [Profile Update](#profile-update)
    - [Like Post](#like-post)
    - [Unlike Post](#unlike-post)
    - [Comment Post](#comment-post)
    - [Comment Post - 2](#comment-post---2)
    - [Delete/Edit Comment](#deleteedit-comment)
    - [Delete Comment - 1](#delete-comment---1)
    - [Delete Comment - 2](#delete-comment---2)
    - [Edit Comment](#edit-comment)
    - [Email Sent - Success](#email-sent---success)
    - [Email Sent - Failed](#email-sent---failed)
    - [Add Book](#add-book)
    - [Edit Book](#edit-book)
    - [Delete Book 1](#delete-book-1)
    - [Delete Book 2](#delete-book-2)
    - [Empty Search](#empty-search)
    - [No Search Found](#no-search-found)
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Testing](#testing)
  - [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Special Thanks](#special-thanks)

## User Experience - UX

### User Stories

* As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of recipes and choose accordingly.
3. Search recipes to find specific recipes.
4. Click on post to read the recipe details.
5. Register for an account to avail of the services offered to members.
6. View the number of likes on a recipe thereby showing which is most popular.
7. View comments on recipes so that I can read other users opinions.

* As logged in website user, I can:

1. Like/unlike recipes marking the recipes I enjoyed.
2. Comment on recipes and give my opinion about the posts.
3. Delete my previous comments.
4. Manage my profile by updating my details and user image.
5. Share my favourites cookbooks by posting them on the Books Page.
6. Edit my favourite cookbook posted previously.
7. Delete my favourite cookbook posted previously
8. Logout from the website.

* As a website superuser, I can:

1. Create and publish a new recipe.
2. Create draft recipe posts that can be reviewed and finalised later.
3. Create a new user, recipes, author and categories.
4. Delete user, recipes, author, categories and comments.
5. Approve user's comments.
6. Edit user's favourite cookbook posted previously
7. Delete user's favourite cookbook posted previously
8. Change the website permissions for a user.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/JureSeselj/tasty_blog/issues)

### The Scope

#### Main Site Goals

* To provide users with a good experience when using the food recipes website.
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
* To provide a website with a clear purpose.
* To provide role-based permissions that allows user to interact with the website.
* To provide tools that allow users to search for recipes.

## Design

#### Colours

![Colours Palete](./assets/readme/extras/screenshot-colour-used.png)

* The colour scheme is kept simple by opting for a combination of white text set against the image
background and black text against the white background. For the navbar was set as a white background
colour.

#### Typography

* The Lato font is used as the main font for the whole project and the Kaushan font is used to
display the word enjoy in the Post Details and About pages.

#### Imagery

* All the imagery is related to the recipes and website design.

### Wireframes

Wireframes for this project can be located [here](WIREFRAMES.md)

## Database Diagram

![Database Diagrama](./assets/readme/extras/tasty_blog_database_diagrama_1.jpg)<br>

[Back to Top](#table-of-contents)

## Features

### Home Page

![Home Page](./assets/readme/features/home-page.png)

* The hero image welcomes the user with a short message advertising what the website is about. These
are 3 carousel images with a button. When the button is pressed, it brings the user down to the highlighted recipes.<br>

### Home Page - Highlights Posts

![Home Page - Highlight Posts](./assets/readme/features/home-highlights.png)

* In the highlighted posts, users can see a selection of 6 recipes. These recipes are
chosen by the site admin by clicking the featured box in the post database.<br>

### About Page

![About Page](./assets/readme/features/tasty-about-us.png)

* The About Page gives, users information about the Tasty Blog website. It introduces the users to the
website. It also details the main purpose and the goal of the blog.<br>

### Blog Page

![Blog Page](./assets/readme/features/blog-page.png)

* On the Blog Page, users have access to the full recipes posts available on the website.
The user can choose to see the recipe detail by clicking on the recipe card.<br>

### Post Detail Page - Top

![Post Detail Page - Top](./assets/readme/features/post-detail-top.png)

* At the top of the Post Details Page, users can see the post's main
image and they can also have access to information about the post. The
post information includes category, recipe name, rating stars,
time to prepare, author name and image, posted date and the
option to like/unlike the post. It will also show how many likes and
comments the post has received.<br>

### Post Detail Page - Steps

![Post Detail Page - Steps](./assets/readme/features/post-details-steps.png)

* In this page section, users can read the ingredients and follow the steps to complete the recipe.<br>

### Post Detail Page - Comments

![Post Detail Page - Comments](./assets/readme/features/post-details-comments.png)

* At the bottom of this page, users can read the comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments.

### Edit Comments Page

![Post Detail Page - Comments](./assets/readme/features/edit-comment.png)

* On this page, users are allowed to comment, delete and edit their own post comments. The website superuser can 
  delete or update any comments on the blog without having to access the admin panel.

### Contact Page

![Contact Page](./assets/readme/features/tasty-contact.png)

* The Contact Page allows users to have access to the Tasty blog
contact details. Users can also send an email to info@tastyblog by
using the contact form available on this page.

### Categories Page

![Categories Page ](./assets/readme/features/categories-page.png)

* On the Categories Page, users can see the categories available in the blog and filter the posts by category.

### Categories Results

![Categories Results Page](./assets/readme/features/category-desserts.png)

* On the Categories Results Page, users can access the post filtered by the chosen category.

### Books Page

![Books Page](./assets/readme/features/books-page.png)

* On this page, registered users can see favourite books posted by other users. If they had already
 published a post they are allowed to edit or delete their own posts.

### Add/Edit Books Page

![Add/Edit Book Page](./assets/readme/features/add-book-page.png)

* On this page, register users can fill out the form to add or edit a post with their favourite cookbooks.

### Search Box

![Search Box](./assets/readme/features/search-box.png)

* In this box, the users can search by inputting a keyword in the search tool. This allows the user to try and find 
  the recipe they are looking for.

### Search Results Page

![Search Results Page](./assets/readme/features/search-results.png)

* On the Search Results Page, users can see the recipes found by their search.  When their recipe is located, the user can go to the 
  Post Details Page by clicking on the card result.

### Search Results - Input Empty

![Search Results - Input Empty](./assets/readme/features/search-empty.png)

* On the Search Results Page - Input Empty, users will see this message if their search returns with an empty input.

### Search Results - No Results Found

![Search Results - No Results Found](./assets/readme/features/no-results-search.png)

* On the Search Results Page - No Results Found, users will see this message if there is nothing found for the search.

### Signup Page

![Signup Page](./assets/readme/features/sign-up.png)

* On the Signup Page, a new user can sign up for the Tasty Blog website by filling out and then submitting the form.

### Login Page

![Login Page](./assets/readme/features/signin-page.png)

* On the Login Page, users can log in to the website by inputting the username and password and have access 
  to website services for a user registered.

### Logout Page

![Logout Page](./assets/readme/features/log-out.png)

* On the Logout Page, users can confirm that they wish to exit the website.

### User Profile Page

![User Profile Page](./assets/readme/features/user-profil.png)

*On the Profile Page, users have access to their own information and can update their user name, email and profile image.

### Navbar

![Navbar](./assets/readme/features/navbar.png)

* The navigation bar is present at the top of every page and houses all links to the various other pages.
* The options to Register or Log in will change to the option to log out once a user has logged in.
* Once a user has signed in, more options such as profile page and user image will be available in the navbar.
* A search icon is nested in the navbar and once clicked it will open the search box.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

![Navbar](./assets/readme/features/dropdown-navbar.png)

* In the navbar users can access on categories list by clicking on the dropdown menu.

### Footer

![Footer](./assets/readme/features/footer.png)

* On the website footer, users can see basic information about the blog such as contact, social media, 
  copyright, and a quote about food recipes.

[Back to Top](#table-of-contents)

## Messages and Interaction With Users

* Some interactive messages were added to the project to make the navigation on the website easier and to improve the
user's experience.

### Sign up
* When users sign up to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>
### Login
* When users sign in to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>
### Logout
* When users log out of the website they will see a message at the top of the page saying "You have signed out".<br>

### Profile Update
* When users update their profile they will see a message at the top of the page saying that their account has been updated.<br>
### Like Post
* *When users are logged in to the website they can like a post and they will see a message at the top of the page 
  saying "You have liked this post".<br>
### Unlike Post
* When users are logged in to the website they can unlike a post that has been liked by the user and they will see a message 
  at the top of the page saying "You have unliked this post".<br>
### Comment Post
* When users are logged in to the website they can comment on a post and after they submit the comment they will see a 
  message at the top of the page saying "Your comment was sent successfully and is awaiting approval".<br>
### Comment Post - 2
* After a user submits a comment, they will see a message over the input comment saying "Thanks (username). Your 
  comment is awaiting approval! <br>

### Delete/Edit Comment

![Delete Comment](./assets/readme/features/delete%3Aedit-comment.png)

* When user is logged in to website and they have previously posted a comment or if the user is a superuser they will see the 
Delete and Edit buttons at the bottom of comments.<br>

### Delete Comment - 1

![Delete Comment - 1](./assets/readme/features/delete%3Dcomment.png)

* If they wish to delete their comment, they can press the button Delete and a Bootstrap box model will pop up with the message 
  "Are you sure you want to delete your comment?".<br>

### Delete Comment - 2
* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your comment was deleted successfully".<br>

### Edit Comment
* After pressing the Update, users will see a message on the top of the page, "The comment was successfully updated".<br>

### Email Sent - Success
* After users submit the form to info@tastyblog successfully, they will see the message, "Thanks for your email! 
  We will contact you as soon as possible".<br>

### Email Sent - Failed
* If the email was not submitted successfully, users will see the message, "Sorry, something went wrong! 
  Try to submit your email again".<br>

### Add Book
* When user is logged in to website they can publish a post with a favourite cookbook and after they submit the 
post they will see a message at the top of the page saying "Your post was sent successfully and is awaiting approval".<br>

### Edit Book
* When user is logged in to website they can edit their own posts published previously and they will see the message 
"The post was successfully updated" after pressing the Submit button.<br>

### Delete Book 1 
* When user is logged in to website and they wish to delete their posts, they can press the button Delete and a 
Bootstrap box model will pop up with the message "Are you sure you want to delete your post?".<br>  

### Delete Book 2
* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your post was deleted successfully".<br>

### Empty Search

![Empty Search](./assets/readme/features/empty-search.png)

* Any user can search for a keyword using the input search and if the search is done with an empty input they will see a
message saying, "You forgot to search a recipe. Please try searching again.".<br>

### No Search Found

![No Search Found](./assets/readme/features/no-results-search.png)

* And if there are no results matching or similar to the keyword, the user will see the following message, "We are sorry. 
  There are no searches for (keyword) on the website. Try the search again".<br>

[Back to Top](#table-of-contents)

## Admin Panel/Superuser

![No Search Found](./assets/readme/features/admin-panel.png)

* On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:
1. Posts
2. Comments
3. Author
4. Categories
5. Profiles
6. Books

* As admin/superuser I can also approve comments and change the status and give other premissions to the users.<br>

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Django](https://www.python.org/)
* [Python](https://www.djangoproject.com/)

#### Django Packages

* [Gunicorn](https://gunicorn.org/) as the server for Heroku.
* [Cloudinary](https://cloudinary.com/) was used to host the static files and media.
* [Dj_database_url](https://pypi.org/project/dj-database-url/) to parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/) as an adaptor for Python and PostgreSQL databases.
* [Summernote](https://summernote.org/) as a text editor.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) for authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style the forms.

### Frameworks - Libraries - Programs Used

* [Bootstrap](https://getbootstrap.com/)
* Was used to style the website, add responsiveness and interactivity
* [Jquery](https://jquery.com/)
* All the scripts were written using jquery library
* [Git](https://git-scm.com/)
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
* [GitHub](https://github.com/)
* GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com)
* Heroku was used to deploy the live project
* [PostgreSQL](https://www.postgresql.org/)
* Database used through heroku.
* [VSCode](https://code.visualstudio.com/)
* VSCode was used to create and edit the website
* [Lucidchart](https://lucid.app/)
* Lucidchart was used to create the database diagram
* [PEP8](http://pep8online.com/)
* PEP8 was used to validate all the Python code
* [W3C - HTML](https://validator.w3.org/)
* W3C- HTML was used to validate all the HTML code
* [W3C - CSS](https://jigsaw.w3.org/css-validator/)
* W3C - CSS was used to validate the CSS code
* [Fontawesome](https://fontawesome.com/)
* To add icons to the website
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
* To check App responsiveness and debugging
* [Google Fonts](https://fonts.google.com/)
* To add the 2 fonts that were used throughout the project
* [Balsamiq](https://balsamiq.com/)
* To build the wireframes for the project
* [CANVA](https://www.canva.com/)
* To build the logos for the project
* [Coolors](https://coolors.co/)
* To build the colour palette of the project
* [Emailjs](https://www.emailjs.com/)
* To send emails from the contact form

### Testing

Testing results [here](TESTING.md)

## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip3 freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project???s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

## Final Deployment 

1. Create a Procfile `web: gunicorn your_project_name.wsgi`
2. When development is complete change the debug setting to: `DEBUG = False in settings.py`
3. In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN` to settings.py.
4. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/JureSeselj/tasty_blog)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/JureSeselj/tasty_blog)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

## Credits

### Content

* Some food recipes were taken from [Taste Atlas](https://www.tasteatlas.com/)
* Also some food recipes were taken from [TheTaste](https://www.thetaste.ie/)
* The cookbook's information and images were sourced from [Dubray Books](https://www.dubraybooks.ie/)
* The images were taken from [Pixabay](https://pixabay.com/)
* The Tasty Blog logos and favicon are my own design

### Information Sources / Resources

* [Code Institute](https://codeinstitute.net/ie/)
* [Free Code Camp](https://www.freecodecamp.org/learn)
* [W3Schools - Python](https://www.w3schools.com/python/)
* [Stack Overflow](https://stackoverflow.com/)
* [Scrimba - Pyhton](https://scrimba.com/learn/python)
