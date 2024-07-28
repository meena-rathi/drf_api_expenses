# from rest_framework import generics
# from .serializers import ExpenseSerializer, CategorySerializer
# from .models import Expense, Category
# from profiles.models import UserProfile

# class ExpenseListCreate(generics.ListCreateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer

# class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer

# class CategoryListCreate(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import Category, Expense, Budget
from .serializers import CategorySerializer, ExpenseSerializer, BudgetSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# class CategoryList(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategoryList(generics.ListCreateAPIView):
    """
    List all categories or create a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a category by id.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]
# class ExpenseList(APIView):
#     def post(self, request):
#         budget = Budget.objects.first()  # Assuming there's only one budget
#         if not budget:
#             return Response({"error": "No budget set"}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             expense = serializer.save()
#             budget.balance -= expense.amount
#             budget.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ExpenseList(APIView):
#     def get(self, request):
#         expenses = Expense.objects.all()
#         serializer = ExpenseSerializer(expenses, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseList(generics.ListCreateAPIView):
    """
    List expenses or create a new expense.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetail(generics.RetrieveDestroyAPIView):
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
    queryset = Budget.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a budget by id.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all()