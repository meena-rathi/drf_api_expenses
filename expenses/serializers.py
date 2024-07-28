# from rest_framework import serializers
# from .models import Category, Expense, UserProfile

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']

# class ExpenseSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Expense
#         fields = ['id', 'amount', 'description', 'category', 'date']

from rest_framework import serializers
from .models import Category, Expense, Budget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'category', 'date', 'user']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'balance']
        # read_only_fields = ['user']