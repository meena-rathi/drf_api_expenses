# ExpensesTracking
I've developed a budget expenses project where users can add their monthly budget and expenses for various products. This allows them to track and identify which products have higher expenses compared to others.

## Project goals

This project offers a Django Rest Framework API to support the [ExpensesTracking React web app](https://github.com/meena-rathi/expensestracker).

### Data Models

The data model schema was designed alongside the API endpoints, using an entity relationship diagram.

![ERD](/drf_api/erd/erd.JPG)

### User Stories 

* I have designed the user stories outlined in my [GitHub project](https://github.com/users/meena-rathi/projects/3).

#### **Expenses**

The model includes two classes: Budget and Expenses.

1. The budget model has a user field, which is a foreign key, and an amount field, which is a decimal field. The amount field is used to set the monthly budget.

2. Expenses Model: The amount field is a decimal field that allows up to 10 digits, including 2 decimal places. The description field stores the details of the expense. The date field automatically records the date when the expense is added. The user field is a foreign key that links each expense to a specific user, ensuring that when the user is deleted, all related expenses are also removed.

3. Profile Model: Oner filed is the fk filed from the User. Image field is the imagefield.

| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| Non-authenticated user tries accessing URL endpoints '/expenses/budgets' | Displays Welcome message requesting user to sign in/up  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/' | Displays Welcome message requesting user to sign in/up  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/:id' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/2' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/Profiles' | Redirected to Sign In page | ✅ |

* Admin has all rights to delete create update all data.

* I have create a superuser on the postgres database [link](https://expensesapi-6d53f1465c6d.herokuapp.com/admin/login/?next=/admin/ ) log into the admin panel on the deployed API with that user.

Currently you have a DEV variable commeted in env.py, so the API running in gitpod is using the postgres, not db.sqlite3 file

* All bugs are resloved my API is woring fine.

## BUGS ##

I hope this not a in profile I can't update in API.

## Frameworks, Libraries, and Dependencies

The TribeHub API is built using the following technologies and packages:

### Django

Django is a high-level Python web framework that facilitates rapid development and clean, pragmatic design.

### Django Rest Framework

Django Rest Framework (DRF) is used to create RESTful APIs with Django, enabling serialization, authentication, and other RESTful functionalities.

### django-cloudinary-storage

Django-cloudinary-storage integrates Cloudinary for media storage, allowing user profile images to be stored in Cloudinary.

### dj-allauth

Dj-allauth provides authentication and registration capabilities, including support for social media logins. Although not currently used, this package may be implemented in future updates.

### dj-rest-auth

Dj-rest-auth offers REST API endpoints for user authentication operations such as login and logout. Custom user registration functionality is implemented separately in the TribeHub API.

### djangorestframework-simplejwt

Djangorestframework-simplejwt enables JSON Web Token (JWT) authentication for securing API endpoints.

### dj-database-url

Dj-database-url simplifies database configuration by allowing connection details to be set via environment variables.

### psycopg2

Psycopg2 is a PostgreSQL adapter for Python, providing the necessary database connectivity for Django applications using PostgreSQL.

### django-filter

django-filter helps with filtering API results based on date ranges. Users can request events that fall within specific dates, and the API also checks for recurring events that might fall within the range.

### django-cors-headers

Django-cors-headers adds headers to allow requests from other websites or apps. TribeHub is set up to accept requests from any origin, making it easier to develop mobile apps that use this API.

##### Deployment Guide for Expenses Tracking API

The Expenses Tracking API is hosted on Heroku and uses an Postgres database. To deploy it yourself, follow these steps:

- Fork or Clone the Repository: Start by copying the project from GitHub.
- Set Up Cloudinary: You'll need Cloudinary to host user profile images.
- Log in to Cloudinary.
- Go to the dashboard.
- Find the 'API Environment variable' starting with cloudinary://. Copy this value and keep it safe for later use.
- Create a Heroku App:

- Log in to Heroku.
- Click 'Create new app' from the 'New' menu at the top right.
- Choose a name and region for your app.
- Click 'Create app'.
- Configure Environment Variables:

- Go to the 'Settings' tab of your Heroku app.
- Click 'Reveal Config Vars'.
- Enter these settings:
- CLOUDINARY_URL: Paste the Cloudinary URL you copied earlier.
- DATABASE_URL: Get this from codeInstution.
- SECRET_KEY: Your secret key for the app.
- ALLOWED_HOST: Your Heroku app’s URL without https://.

- Go back to Heroku.
- In the 'Deploy' tab, choose 'GitHub' for deployment.
- Search for and connect your GitHub repo.
- Optionally, enable 'Automatic Deploys' to redeploy automatically when you push changes to GitHub.
- For a manual deploy, choose the 'main' branch and click 'Deploy Branch'.
- Your app will be deployed, and you’ll receive a link to your live site once it’s done.

## Credits

- [Stackoverflow](https://stackoverflow.com/questions/30203652/how-to-get-request-user-in-django-rest-framework-serializer)

- [Stackoverflow](https://stackoverflow.com/questions/30203652/how-to-get-request-user-in-django-rest-framework-serializer)

- [StackOverflow article](https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement)
 
 - [StackOverflow article](https://stackoverflow.com/questions/51042871/how-to-access-url-kwargs-in-generic-api-views-listcreateapiview-to-be-more-spec)

- walk thruogh project[https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106]
- readme[TribeHub]

#### Acknowledgments

I would like to express my gratitude to the following individuals:

- My Mentor, jubril, whose guidance and support have been invaluable.

- Who provided significant assistance with my readme file[https://github.com/andy-guttridge/tribehub_react?tab=readme-ov-file#validator-testing].

- kristyna_ci, whose contributions were immensely helpful throughout the project.

- Thanks to all my classmates who provided feedback about my project. How can I make it even better?