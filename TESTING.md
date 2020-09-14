## [Testing](#testing)

# Automated Testing

### Validation services

Services used to check the validity of the code:

[W3C Markup Validation used to validate HTML.](https://validator.w3.org/)<br>

[W3C CSS validation used to validate CSS.](https://jigsaw.w3.org/css-validator/)<br>

* Erros found which I couldn't fix. Description in the "Problems" below
---
### Django TestCase
I used TestCase for the testing of the the models and forms. 
I had one error in test_models "Checkout" app which I could't fix

     AssertionError: datetime.datetime(2020, 9, 11, 23, 18, 32) != datetime.datetime(2020, 9, 13, 21, 18, 26, 817765, tzinfo=<UTC>)
 
All other tests were running without errors
 
Because of limited time unfortunetly I didn't learn how  to apply tests into the production database. 

To run tests in setting.py I had to set:<br>

     DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
     }
and use command :

     python3 manage.py test 

# Travis-CI

 Travis was used for continuous integration service. Tests were done every time the project is deployed to github.

# Manual testing

Information about all manual testing that has been done
to make sure all areas of the website are working as expected.

Browsers: **Google; Opera; Firefox ; Microsoft Edge.**

Browser width

xs = Extra small <576px

sm = Small ≥576px

md = Medium ≥768px

lg = Large ≥992px

xl = Extra large ≥1200px

|         | XS  | SM  | MD  | LG  | XL  |
| ------- | --- | --- | --- | --- | --- |
| Google  | Ok  | Ok  | Ok  | Ok  | Ok  |
| Firefox | Ok  | Ok  | Ok  | Ok  | Ok  |
| Opera   | Ok  | Ok  | Ok  | Ok  | Ok  |
| ME      | Ok  | Ok  | Ok  | Ok  | Ok  |

In each browser in each size were tested :

Web page :

- Open/Close .
- Switch between navigation bar links.
- Refresh.
- Resize with browser window.
- Responsiveness with dev tools

Design :

- Colors.
- Text
- Fonts
- Images

Layout :

- Bootstrap Grid Layout.

Website functionality:

- Loading of Images
- Loading of Links from database
- Loading of text from the database
- Open close pages.
- Navigation between pages
- Pagination
- Add products to the shopping cart
- The functionality of forms:
  Contact form
  Registration form
  Log in form
  Comment form
  Checkout form
  Shopping cart form to add or remove product
  Password reset form
- All buttons are working
- A modal window is working

---

# Problems discovered

1.  **Problems with Quiz app navbar link :**

    - **Problem:** <br>
      The Quiz nav link element when clicked also were trigger Log in link.
      

    - **Solution:** <br>
     Removed annesasary part of code in quiz.views. 
     
2)  **Error while trying to Add empty field in the form:**

    **Problem** <br>
    while trying to Add empty field in the Course form or shopping cart form was redirecting to Error page

    - **Solution:** <br>
    Added a "required" to the input field

3)  **Error while checking code on html validator:**

   **Problem**<br>
    while checking code in validator  an Errors found :

        Misplaced non-space characters inside a table.
        <tr>↩{% for item in cart_items %}↩<form class="form" method="post" action="{% url 'adjust_cart' item.id %}">↩


   The error in <br>
   cart.html, Cart app <br>
   checkout.html, Checkout app <br>
  
 **Solution:** <br>
    unfortunetly I didn't find solution. Try to change code as much as I can without destroying the functionality. <br>
    
    

# Real-Time Testing

Asked my friends and family to check the website on their devices.
Go through all the pages, open/close . Repeat many times. Press all buttons. Switch fast between pages
Move through the navigation bar menu back and forward. Resize screen. Use forms :
Contact, Add product, Remove Product, Checkout form, Comment form. Go through quiz questions

**Feed back**.

The website was checked on different mobile devices and desktops.
Everything working

-----
# User Stories Testing

### As a potential client of "Adriatic Diving" school and web site visitor I want:

 1. Fast and easy understand which services provided by this school and their web site.<br>

     From the home page very easy to understand that this web site about diving.<br>
     "Welcome" text front image, everything about diving.
 ---------------
 2. See enough information on the front page to understand what I can find and where.<br>

     Information can be found on the navigation bar, jumbotron image and on the cards below.<br>
     The user can see short text with links to the following pages
 -----------------
 3. Have an easy navigation menu which giving information about each page.<br>

     Navigation bar giving a full list of pages. Name of the pages straight reference to their context. <br>
 ---------------
 4. I want to see how I can contact the shop owner if I have more questions.<br>

     "Contact us" button opening the contact form. The button displayed on the footer and visible on each page. <br>
     The functionality of the contact form very clear and simple. User can send an email straight from the website<br>
 --------------------
 5. Have a full detailed description of the products promoted on the web site.<br>

     Information about each course can be found on separate pages. User can see all requirements<br>
     and very easy to understand if this course fit to his needs and level of experience or not<br>
 -------------------
 6. Have a clear understanding of how to make the registration or log in/log out with a response on my action.<br>

     Registration/Log in forms very easy to find. Visible at the navigation bar menu. <br>
     Forms are clear and simple with the response on the user action<br>
 -------------------
 7. Easy access to the possibility to buy the product, adding it to a shopping cart, and see if the action completed.<br>

     The product can be added from the Course page. Under the table with parameters is an input field.<br>
     Very easy to understand the functionality and as soon as the product in the shopping cart there appear yellow bage with the number<br>
 --------------------
 8. Be able to change the number of products in the shopping cart and see the final price before checkout.<br>

     The number of products changeable in the shopping cart. Can be increased, decreased, or removed. <br>
     At the bottom of the shopping, cart user can see the Total amount including the discount<br>
 ----------------------
 9. Have a clear explanation about form fields in forms I have to fill. See response if I did a mistake.<br>

     Each form has text explanation at all fields and giving notification if filled wrong<br>
 -----------------------
 10. Fast and easy checkout out system with well-provided information about what I need to do.<br>

     On the checkout page, the User can see his order details one more time. And form below. <br>
     Standart checkout form with labels on each field. Submit button below<br>
 ----------------------
 11. Easy navigation between different pages.<br>

     Pages in each up very well connected. Users can easily move from page to page without using the navigation bar menu.<br>
     The navigation bar menu always can be found on each page<br>
 ------------------------
 12. I would like to see more information about diving, different diving sites, and more opportunities to get new experience<br>
 
     The diving blog has articles about skills improvement  local dive sites and more information for divers of all levels<br>
 --------------------
 13. Get chance to refresh knowledge about the subject or learn something new.<br>

     The diving blog has articles which referencing to the courses. It's giving chance to the clients to find a new information <br>
     and straight see how he can use it. <br>
     The quiz can be a good chance to check yourself. Learn or refresh some information<br>
 ------------------------
 14. Have an extra discount from buying courses online.<br>

     Discount is a great motivation to buy courses online. <br>
 ------------------
 15. Get motivated to choose this school for my activities.<br>

     According to the testing experience, users love website. <br>
     Some get more interest in diving then before. Even non-divers had fun playing with the quiz and read a blog.<br> 
     Detailed information about each course giving more understanding about possibilities. Design of the web page very pleasurable and really giving filling of connection to the sea.
 -------------------------