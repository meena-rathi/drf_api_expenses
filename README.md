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
| Non-authenticated user tries accessing URL endpoints '/projects/:id/tasks/create' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks/:id' | Redirected to Sign In page | ✅ |
| Non-authenticated user tries accessing URL endpoints '/tasks/:id/edit' | Redirected to Sign In page | ✅ |