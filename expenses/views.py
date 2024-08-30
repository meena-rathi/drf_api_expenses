

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Expense, Budget
from .serializers import  ExpenseSerializer, BudgetSerializer
from drf_api.permissions import IsOwnerOrReadOnly



class ExpenseList(generics.ListCreateAPIView):
    """
    List expenses or create a new expense.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or delete an expense by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()




class BudgetList(generics.ListCreateAPIView):
    """
    List budgets or create a new budget.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned budgets to the current user.
        """
        user = self.request.user
        return Budget.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or delete a budget by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned budgets to the current user.
        """
        user = self.request.user
        return Budget.objects.filter(user=user)