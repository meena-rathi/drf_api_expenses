from django.urls import path
from .views import  ExpenseList, BudgetList , ExpenseDetail, BudgetDetail # Update the import to match your view names

urlpatterns = [
    path('', ExpenseList.as_view(), name='expense-list'),
    path('<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path('budgets/', BudgetList.as_view(), name='budget-list'),
    path('budgets/<int:pk>/', BudgetDetail.as_view(), name='budget-detail'),
]