from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Expense, Budget
from .serializers import ExpenseSerializer, BudgetSerializer
from rest_framework.exceptions import PermissionDenied

class ExpenseList(generics.ListCreateAPIView):
    """
    List expenses or create a new expense.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an expense by id.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this expense.")
        return obj

    def delete(self, request, *args, **kwargs):
        try:
            expense = self.get_object()
            self.perform_destroy(expense)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Expense.DoesNotExist:
            return Response({'detail': 'Expense not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BudgetList(generics.ListCreateAPIView):
    """
    List budgets or create a new budget.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Optionally restrict the returned budgets to the current user.
        """
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a budget by id.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Optionally restrict the returned budgets to the current user.
        """
        return Budget.objects.filter(user=self.request.user)
