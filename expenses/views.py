

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

    def get_queryset(self):
        # Only return expenses for the current authenticated user
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Associate the expense with the current authenticated user
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an expense by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        # Only allow access to the specific expense if it belongs to the user
        return Expense.objects.filter(user=self.request.user)

    def get_object(self):
        # Override to ensure the user can only access their own expense
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this expense.")
        return obj



# class ExpenseList(generics.ListCreateAPIView):
#     """
#     List expenses or create a new expense.
#     """
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = ExpenseSerializer
#     queryset = Expense.objects.all()

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve or delete an expense by id.
#     """
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = ExpenseSerializer
#     queryset = Expense.objects.all()




# class BudgetList(generics.ListCreateAPIView):
#     """
#     List budgets or create a new budget.
#     """
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = BudgetSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned budgets to the current user.
#         """
#         user = self.request.user
#         return Budget.objects.filter(user=user)

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)

# class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve or delete a budget by id.
#     """
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = BudgetSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned budgets to the current user.
#         """
#         user = self.request.user
#         return Budget.objects.filter(user=user)
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
    Retrieve or delete a budget by id.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        """
        Optionally restrict the returned budgets to the current user.
        """
        return Budget.objects.filter(user=self.request.user)

# class ProfileList(generics.ListCreateAPIView):
#     queryset = Profiles.objects.all()
#     serializer_class = ProfileSerializer

# # Retrieve, update or delete a specific profile
# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profiles.objects.all()
#     serializer_class = ProfileSerializer