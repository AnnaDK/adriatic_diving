## [Testing](#testing)

# Automated Testing

### Validation services

Services used to check the validity of the code:

[W3C Markup Validation used to validate HTML.](https://validator.w3.org/)<br>

[W3C CSS validation used to validate CSS.](https://jigsaw.w3.org/css-validator/)<br>

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
    while trying to Add empty field in the Course form or shopping cart form was showing an Error

    - **Solution:** <br>
    Added a "required" to the input field



# Real-Time Testing

Asked my friends and family to check the website on their devices.
Go through all the pages, open/close . Repeat many times. Press all buttons. Switch fast between pages
Move through the navigation bar menu back and forward. Resize screen. Use forms :
Contact, Add product, Remove Product, Checkout form, Comment form. Go through quiz questions

**Feed back**.

The website was checked on different mobile devices and desktops.
Everything working

---
