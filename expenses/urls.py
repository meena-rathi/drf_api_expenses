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
from .views import CategoryList, ExpenseList, BudgetList  # Update the import to match your view names

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('budgets/', BudgetList.as_view(), name='budget-list'),  # Update to BudgetList
]