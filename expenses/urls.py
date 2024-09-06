# from django.urls import path
# from .views import ExpenseListCreate, ExpenseDetail, CategoryListCreate, CategoryDetail, UserProfile, UserProfileDetail
# urlpatterns = [
#     path('expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
#     path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
#     path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
#     path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
#     path('profile/', UserProfileDetail.as_view(), name='user-profile-detail'),
# ]
# from django.urls import path
# from . import views


# urlpatterns = [
#     path('set_budget/', views.set_budget, name='set_budget'),
#     path('add_expense/', views.add_expense, name='add_expense'),
#     path('remaining_budget/', views.remaining_budget, name='remaining_budget'),
#     path('expenses/', views.get_expenses, name='get_expenses'),
# ]

from django.urls import path
from .views import  ExpenseList, BudgetList , ExpenseDetail, BudgetDetail # Update the import to match your view names

urlpatterns = [
    # path('categories/', CategoryList.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path('expenses/<int:pk>/edit/', ExpenseDetail.as_view(), name='expense-edit'),
    path('budgets/',BudgetList.as_view(), name='budget-list'),
    path('expenses/create/', ExpenseList.as_view(), name='expense-create'),
    path('budgets/<int:pk>/', BudgetDetail.as_view(), name='budget-detail'),
    # path('profiles/', ProfileList.as_view(), name='profile-list'),
    # path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]