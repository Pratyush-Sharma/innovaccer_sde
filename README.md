# Entry Management Software

This project is an entry management software for visitors that we have in office and outside, which can capture details of the visitor.
Once the user enters the information in the form, it triggers an email to host from the host itself, informing  him of the details of the visitor with checkin time.
At the time of checkout, when the visitor enters his details, this triggers an email to the visitor from the host stating his visit details :

- Name
- Phone
- Checkout time
- Host name
- Address visited

## Getting Started

This project requires Django and Python installed on your PC.
If you wish to install Django using the Ubuntu repositories, the process is very straight forward.

For Python2-
```
sudo apt-get update
sudo apt-get install python-django
```

For Python3-
```
sudo apt-get update
sudo apt-get install python3-django
```
You will also need to have software installed to run and execute a Django project.(Recommended - **PyCharm**)

## Approach

Built a home page for the entry system, which contains two buttons(**CheckIn** and **ChekcOut**). 
Each button is hyperlinked to it's own corresponding webpage(**login.html** and **logout.html**). 
When a visitor comes he clicks on CheckIn button, he is redirected to a login form, where he enters his details and submit the form.
After submitting the form, the host recieves a mail from the host itself of the checkin details and time of the visitor and the app is automatically redirected to homepage.
When the visitor is checking out, he clicks on checkout button at homepage and is redirected to logout form, where he again enters his details, and on submission, 
visitor recieves a mail from the host stating his checkout time & details, and the app is again automatically redirected to homepage.


## Files Description

- manage.py - for running server and managing 

**website**

- settings.py - contains all the settings, installed apps, host details and databases
- urls.py - to specify URL link for a webpage and redirect

**accounts**
- forms.py - form template
- views.py - to specify how a webpage will look/view and rendering requests of functions specified
- templates/account/(*.html) - html webpages (home, login, logout) where base.html contains the base/common structure of all webpages and the changes in other html files and rendered through ginger2. 


**Host details used -**

Name - Vishesh Singh

Email - vs@xyz.com

For sending mails, a host email has to be set up. Here, above arbitrary menioned email is used. 


## Running the app

- For proper functioning of mailing system, replace the above mentioned arbitrary host email with a valid email details in the host details in **settings.py** and in functions myform & outform in **views.py**

- For a gmail host email id, enable the allow access to unsecure apps in the account settings, to be able to send emails through the server. 

Once you have created your project repository, open the terminal in it and run the server-
```
python manage.py runserver
```

After this, open your browser(Chrome) and open-
```
http://127.0.0.1:8000/account/
```

This shall lead you to **homepage** of the app.
