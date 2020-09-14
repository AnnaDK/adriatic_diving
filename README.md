# Full Stack Frameworks with Django Milestone Project 



[![Build Status](https://travis-ci.org/AnnaDK/adriatic_diving.svg?branch=master)](https://travis-ci.org/AnnaDK/adriatic_diving)

 <p align="center">
   <img  src="wireframes/images_readme/for_readme.png">
 </p>


 # **Adriatic Diving** 

 The "Adriatic Diving" was developed as the last project for the Code Institute Software Development diploma. This website is a diving school webpage that provides for clients information about the diving school and diving courses. Clients can contact the school, buy courses online, read a diving blog, or take a diving quiz to check their knowledge.

 ## [Click To Open !](https://adriatic-diving.herokuapp.com/)

 ****
 # **Table of Contents**


 ## 1. [UX](#ux) 

   - **[Project Goals](#project-goals)**
   - **[User Goals](#user-goals)**
   - **[Developer Goals](#developer-goals)**
   - **[User Stories](#user-stories)**
   - **[Wireframes](#wireframes)**

 ## 2. [Features](#features)

   - **[Existing Features](#existing-features)**
   - **[Features Left To Implement](#features-left-to-implement)**

 ## 3. [Technologies Used](#technologies-used)

 ## 4. [Testing](#testing)

 ## 5. [Deployment](#deployment)

 ## 6. [Acknowledgments](#acknowledgments)
 ---------------------------------------------------------------

 ## [UX](#ux)

 ### [Project Goals](#project-goals)

  To create a full-stack site with an authentication mechanism, business logic, and the possibility for clients the purchase of a product/service.

 ### [User goals](#user-goals)

 Clients goals:

 - Have the possibility to visit a web page of a diving school, find more information about service provided and diving courses.
 - Be able to check information about diving courses with details.
 - Be able to contact the diving school for more question.
 - Find more information about diving it that area and diving education.
 - Buy courses online with extra benefits
 - Easy navigate around the page without extra time spending for finding information.
 - Have fun from visiting a web site and get the motivation to choose this school

 The Adriatic Diving web page is meeting these goals because:

 - The web page is online presence of a company with provided information about its services
 - Information about diving courses presented on the "Courses" page. Each course described separately in the details following standards of the SSI diving association.
 - School address, phone number, and form for direct email contact available and easily can be found on the page
 - The diving blog providing articles about local dive sites, standards of diving, safety rules, and more recommendation.
 - In the online webshop, clients can buy courses with extra online discount
 - The web site has a simple intuitive design and all parts of a web site named according to their context 
 - Extra bonus is a diving quiz. Everybody can check or refresh their basic knowledge about diving. Motivation to learn more or take a skills update course


 ### [Developer Goals](#developer-goals)

 - Create the Fourth Milestone Project which meets requirements from Code Institute
 - An independent project after learning Django Frameworks
 - The fourth independent project in the portfolio of the developer
 - Create an e-commerce web page 
 - Create a functional web site which can be used by any company which will  promote their service and sell their products

 ### [User Stories](#user-stories)

 As a potential client of "Adriatic Diving" school I want:

 1. Fast and easy understand which services provided by this school and their web site.
 2. See enough information on the front page to understand what I can find and where.
 3. Have an easy navigation menu which giving information about each page.
 4. I want to see how I can contact the shop owner if I have more questions.
 5. Have a full detailed description of the products promoted on the web site.
 6. Have a clear understanding of how to make the registration or log in/log out with a response on my action.
 7. Easy access to the possibility to buy the product, adding it to a shopping cart, and see if the action completed.
 8. Be able to change the number of products in the shopping cart and see the final price before checkout.
 9. Have a clear explanation about form fields in forms I have to fill. See response if I did a mistake.
10. Fast and easy checkout out system with well-provided information about what I need to do.
11. Easy navigation between different pages.
12. I would like to see more information about diving, different diving sites, and more opportunities to get new experience
13. Get chance to refresh knowledge about the subject or learn something new.
14. Have an extra discount from buying courses online.
15. Get motivated to choose this school for my activities.

 
 ### [Wireframes](#wireframes)

 The wireframes were created using  [Balsamiq Wireframes](https://balsamiq.com/).

 All information can be found in [wireframes.md](./WIREFRAMES.md)

 ----------------------------------------------------------------------


 ## [Features](#features)

 ### [Existing Features](#existing-features)

 #### All Pages

 1. **Navigation bar**.
 *  Logo: "Adriatic Diving". Allows users to come back to Home Page.<br>
    Navigation menu allows users to navigate throug web site:<br>
    Home<br>
    Courses<br>
    Quiz<br>
    Blog<br>
    Cart<br>
    If user is not logged in :<br>
    Log in<br>
    Registration<br>
    If user is logged in :<br>
    Log out<br>
    Profile<br>

 2. **Footer**.
 Allows users to see post address of the school and contact the school via email <br>
 by pressing the "Contact" button and filling a contact email form.

 *  Post Address of the diving school with phone number.<br>
    Button "Contact" opening a modal window with contact form<br>
    Copyright sign

 #### Home Page

 
 1. **Jumbotron**
    Main home page image.<br>
     Buttons links to Log In or Register.<br>
     Allows users to go to the registration form or login form<br>
     

 2. **Cards**<br>
 Allows users to see a short description about web site pages such as Courses, Blog, Quiz and go there by following arrows links.
 ##### Do you want to get certified?
 text + link to courses page
 ##### Welcome in our Blog
 text + link to blog page
 ##### Check yourself
 text + link to quiz page


 #### Courses Page <br>

 Allows users to see all diving courses and by clicking on the course image move to the separate page with a full explanation

 1. Image cards.
 * Each working as a link to the diving course page<br>
 2. Text card.
 * Explanation about courses and discount.

 #### Course Page <br>

 Allows users to see parameters for each course.<br>
 Details represented as a table with the course price below. <br>
 By choosing a quantity and clicking the "Buy" button the user will add a course to the shopping cart

 #### Blog Page
 Allows users to see all blog posts. <br>
 Pagination at the button of the page allows the switch between pages.<br>
 Each blog card has a button. By clicking on it the user will open the blog post as a separate page<br>

 1. List of cards with blog posts.<br>
 * Image
 * Short description
 * Button 'read more'

 #### Blog Post
 Allows users to see chosen blog post on the separate page
 Users can live comments by clicking on the ''Comment" button if he is logged in. Or log in button and fill an authorization form before leaving a comment. 
 Comments will appear after approval from the admin

 #### Quiz Page
  Allows users to see all quiz questions. <br>
  Pagination at the bottom of the page allows users to switch between pages.<br>
  Each question working as a link and by clicking on it user will open a separate page with a question

 1. Cards :<br>
 * Quiz number
 * Question

 #### Log in Page
 Allows users to log in by filling a simple form with 'username' and a 'password'.<br>
 If user forgot the password he clicks the link below 'Reset Password' and will redirect to the reset password page
 

 #### Register Page
 Allows users to make a registration on the web site by filling a form:<br>
 "Email"<br>
 "Username"<br>
 "Password"<br>
 "Password confirmation"<br>
 #### Log out Page
 Allows users to ''Log out" by clicking Log out button in the navigation menu bar

 #### Profile Page
 Allows users to see their profile page with information :<br>
 "Username"<br>
 "email"<br>
 and "Reset Password" link

 #### Shopping Cart Page
 Allows users to see which products they choose to buy. <br>
 Change a quantity or go back to the product page by clicking on the product name.<br>
 If the user is satisfied by his choose he can check the total amount below including discount and proceed father by clicking on the "Checkout " button
 
 #### Checkout Page
 Allows users to complete their purchase by filling a checkout form. <br>
 If all fields filled correct and the form submitted user will see a verifying message 

 #### Contact Page
 Allows users to send an email to diving school by filling a contact form. <br>
 Link to the modal window with a contact form at the bottom of the page. Button "Contact us"
 
 ### [Features Left to Implement](#features-left-to-implement)

 1. In the Blog create functionality which allows users to remove or edit their own comment. 

 2. Create a search in the Blog app. Which will allow users to find a blog post by tags or subjects.
     
 3. Create a control functionality in the Quiz. Will show different reactions depending on the user answers <br>
   If it is wrong or right.<br>
   For example different colors of answer messages. Red or Green. With "You are wrong" or "You are right" on top. 
     
 4. In the Quiz app create functionality which will count how many right answers gave the user and show a result at the end.

 5. Add more quizzes with different levels of difficulty.

 6. Create a functionality which will save order details in the user profile and send a confirmation letter after checkout.


 ------------------------------------------------------------------------

  ## [Technologies Used](#technologies-used)

 ### Languages
  This project uses HTML, CSS, JavaScript and Python programming languages.

  * **[Balsamiq](https://balsamiq.com/)** <br/>
   The project uses Balsamiqo to build wireframes in the planning stage of development.
  * **[GitPod](https://www.gitpod.io/)** <br/>
   The project uses GitPod to build the website.
  * **[JQuery](https://jquery.com/)**<br/>
   The project uses JQuery as JS library to make HTML document traversal and manipulative
  * **[Bootstrap](https://getbootstrap.com/)**<br/>
   The project uses the Bootstrap framework to help create some elements 
  * **[FontAwesome](https://fontawesome.com/)**<br/>
   The project uses FonAwesome to use an icons from the library.
  * **[Google Fonts](https://fonts.google.com/)**<br/>
   The project uses Google fonts to style the website fonts.
  * **[GitHub](https://github.com/)**<br/>
   To store and share all project code remotely.
  * **[AutoPrefixer](https://autoprefixer.github.io/)**<br/>
   The project used AutoPrefixer to add prefixes in the CSS for cross-browser support.
  * **[Google Chrome - Dev Tools]()**<br/>
   The project used Google Chrome Dev Tools to debug code. Check responsiveness.
  * **[EmailJS](https://www.emailjs.com/)**<br/>
   To connect mail service to the web site and be able to receive feedback and messages from users.
  * **[Stripe](https://stripe.com/ie)**<br/>
   To receive payments.
  * **[Google](https://www.google.com)**<br/>
    Images for the project were found by using Google image search.
  * **[Stackoverflow](https://stackoverflow.com/)** <br/>
   To find a thousand answers for a thousand questions.
  * **[Heroku](https://heroku.com/)** <br/>
    For hosting the application and deploy.
  * **[AWS S3](https://aws.amazon.com/s3/)** <br/>
    As a cloud service to host static files.
  * **[CkEditor](https://ckeditor.com/docs/)** <br/>
    To better format texts in the text fields.
  * **[SqLite](https://www.sqlite.org/index.html)** <br/>
    A database provided by django.
  * **[PostgreSQL](https://www.postgresql.org/)** <br/>
    A database provided by heroku.
  * **[Travis CI](https://travis-ci.org/)** <br/>
    For integration and testing
  * **[Django](https://www.djangoproject.com/)** <br/>
    High level python web-framework used to design this project
 --------------------------------------------------------------------------
 ## [Testing](#testing)

   All information can be found in [testing.md](./TESTING.md)

 ------------------------------------------------------------------------------
 ## [Deployment](#deployment)
  
  --------------------------------------------------------------------
  website was codded on GitPod.

 - Open account on GitHub.
 - Create a project repository using the CI full template.
 - Use the Gitpod extension to open a working-space.
 - Commits were done through Gitpod.

 ### How to run this project locally: 
  To run this project on your own IDE :<br>
  Install on your machine: - PIP - Python 3 - Git<br>
  You must to have accounts with the following services: <br>

     - Stripe - AWS and set up an S3 bucket - emailjs

  Save a copy of the github repository located at <br>

     https://github.com/AnnaDK/adriatic_diving.git 

 clicking the "download zip" button at the top of the page.<br>
 Extract the zip file to your chosen folder. <br>
 Or clone the repository <br>
 If necessary  Upgrade pip with:<br>
      pip install --upgrade pip.<br>
 Install all required modules :<br>

     pip -r requirements.txt.

 Set up the following environment variables in env.py file <br>

     $ touch .gitignore

 Add the env.py to the .gitignore file.<br>
     
     import os 

     os.environ.setdefault('SECRET_KEY', '<secrete key>')
     os.environ.setdefault('DATABASE_URL', '<postgres key>')

 ### STRIPE API Keys 
     os.environ.setdefault('STRIPE_PUBLISHABLE', '<stripe publishable key>')
     os.environ.setdefault('STRIPE_SECRET', '<stripe secret key>')
 
 ### Email Keys 
     os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
     os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')

 ### AWS API Keys 
     os.environ.setdefault('AWS_ACCESS_KEY_ID', '<aws access key id>')
     os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<aws secret access key>')

 ### Email Keys 
     os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
     os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')

 Migrate the models to crete a database template.

      $ python manage.py migrate

 Create superuser

 python manage.py createsuperuser
 Run the program locally :

     python manage.py runserver

 ### Deployment to Heroku
  Log in to Heroku <br>
  Install Heroku-CLI <br>
  Type in the terminal: <br>

     $ heroku login

 Enter  Heroku credentials.<br>

     Email: your@email.com
     Password :

 Save all the requirements into the requirements.txt :<br>

     $ pip freeze > requirements.txt

  Create a Procfile and add there:<br>

     web: gunicorn adriaticdiving.wsgi:application

  Now can do <br>

     add ., git commit and git push 

  your application to a GitHub repository <br>
 In the Heroku account create new app.<br>
 Select  region and name for the project.<br>
 From the heroku dashboard  click on "Deploy" click "Deployment method" and select GitHub.<br>
 Link heroku app to the correct GitHub repository.<br>
 In the Heroku settings - reveal config vars.<br>
 Config variables must be set:<br>

     KEY	VALUE
     AWS_ACCESS_KEY_ID	<your aws access key>
     AWS_SECRET_ACCESS_KEY	<your aws secret access key>
     DATABASE_URL	<your postgres database url>
     EMAIL_ADDRESS	<your email address>
     EMAIL_PASSWORD	<your email password>
     SECRET_KEY	<your secret key>
     STRIPE_PUBLISHABLE	<your stripe publishable key>
     STRIPE_SECRET	<your stripe secret key>
     AWS_ACCESS_KEY_ID	<your aws access key>
 
 From the command line :<br>

 Enter the heroku postres shell
 Migrate the database models
 Create your superuser account 
 Information at [ heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql)

 Heroku dashboard:<br>
 click "Deploy"<br>
 At  "Manual Deploy" select the master branch and click "Deploy Branch".<br>
 After the build is complete, click the "View app" .<br>
 At the link provided add   /admin .<br>
 Can log in with your superuser account<br>
 Once instances of these items exist in your database your heroku site will run as expected.<br>

 To add Add static files to AWS s3<br>
 can follow this [tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).

 ------------------------------------------------------------------------------
 ## [Acknowledgments](#acknowledgments)

 - Text within this project was written by the developer.
 - Text for a description of courses and different information about diving taken from the [SSI web site.](https://www.divessi.com/en-IC/home/)
 - Images for courses and home page taken from the [SSI web site.](https://www.divessi.com/en-IC/home/)
 
 - Project idea and design were created by the developer


 - Code Institute lessons from "Full Stack Frameworks with Django " modules were used as the main reference in the process of creating this project.
 - Apps: Accounts, Cart, Checkout were coded by following Code Institute lessons from "Full Stack Frameworks with Django " modules 
 - Blog App created with help of CI lessons and tutorial from [Django girls.org](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/)
 - Quiz App created with help of tutorial from [prettyprinted](https://prettyprinted.com/tutorials/creating-a-poll-app-in-django)
 - Quiz questions from [dive-college](http://www.dive-college.com.cy/test-your-knowledge.html)
 - Shopping cart snippep from bootstrapious.com. Changed and adjusted for the project [bootstrapious](https://bootstrapious.com/p/bootstrap-shopping-cart)
 - Nav-bar brand icon from [here](https://www.flaticon.com/free-icon/diving_3145026?term=diving&page=1&position=84)
 - Docs.djangoproject used as helpfull sourse in creating this project [docs.djangoproject](https://docs.djangoproject.com/)
  
### Special thanks to:

  Code Institute Mentor Spencer Barriball for his help in this project and support.<br>
  Code Institute Tutor support. Special thanks to CI tutors Xavier and Tim<br>
  Code Institute Slack Community for the shared experience.

 ## [Disclaimer](#disclamer)

 The "Adriatic Diving" project is created for educational purposes only.







