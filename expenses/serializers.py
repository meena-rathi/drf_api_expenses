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
        fields = ['id', 'name'] 

class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'category', 'date']

    def validate_category(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Category must be a primary key (integer).")
        return value

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'balance']
        # read_only_fields = ['user']