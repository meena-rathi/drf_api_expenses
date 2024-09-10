# ExpensesTracking

## Project goals

This project offers a Django Rest Framework API to support the [ExpensesTracking React web app](https://github.com/meena-rathi/expensestracker).

### Data Models
The data model schema was designed alongside the API endpoints, using an entity relationship diagram.

#### **Expenses**

The model includes two classes: Budget and Expenses.

1. The budget model has a user field, which is a foreign key, and an amount field, which is a decimal field. The amount field is used to set the monthly budget.

2. Expenses Model: The amount field is a decimal field that allows up to 10 digits, including 2 decimal places. The description field stores the details of the expense. The date field automatically records the date when the expense is added. The user field is a foreign key that links each expense to a specific user, ensuring that when the user is deleted, all related expenses are also removed.

| Test       | Expected           | Passed  |
| :------------- |:-------------:| :-----:|
| Non-authenticated user tries accessing URL endpoints '/budgets' | Displays Welcome message requesting user to sign in/up  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/' | Displays Welcome message requesting user to sign in/up  | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/:id' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/:id/edit/' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/expenses/:/create' | Redirected to Sign In page | ✅ |

## Frameworks, Libraries, and Dependencies
The TribeHub API is built using the following technologies and packages:

### Django
Django is a high-level Python web framework that facilitates rapid development and clean, pragmatic design.

### Django Rest Framework
Django Rest Framework (DRF) is used to create RESTful APIs with Django, enabling serialization, authentication, and other RESTful functionalities.

### django-cloudinary-storage
django-cloudinary-storage integrates Cloudinary for media storage, allowing user profile images to be stored in Cloudinary.

### dj-allauth
dj-allauth provides authentication and registration capabilities, including support for social media logins. Although not currently used, this package may be implemented in future updates.

### dj-rest-auth
dj-rest-auth offers REST API endpoints for user authentication operations such as login and logout. Custom user registration functionality is implemented separately in the TribeHub API.

### djangorestframework-simplejwt
djangorestframework-simplejwt enables JSON Web Token (JWT) authentication for securing API endpoints.

### dj-database-url
dj-database-url simplifies database configuration by allowing connection details to be set via environment variables.

### psycopg2
psycopg2 is a PostgreSQL adapter for Python, providing the necessary database connectivity for Django applications using PostgreSQL.

### django-filter
django-filter helps with filtering API results based on date ranges. Users can request events that fall within specific dates, and the API also checks for recurring events that might fall within the range.

### django-cors-headers
django-cors-headers adds headers to allow requests from other websites or apps. TribeHub is set up to accept requests from any origin, making it easier to develop mobile apps that use this API.


##### Deployment Guide for Expenses Tracking API
The TribeHub API is hosted on Heroku and uses an ElephantSQL Postgres database. To deploy it yourself, follow these steps:

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
- DATABASE_URL: Get this from ElephantSQL (details below).
- SECRET_KEY: Your secret key for the app.
- ALLOWED_HOST: Your Heroku app’s URL without https://.

- Log in to ElephantSQL.
- Click 'Create new instance' on the dashboard.
- Choose the 'Tiny Turtle (free)' plan.
- Select the nearest data center.
- Click 'Review' and copy the database URL starting with postgres://.
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
