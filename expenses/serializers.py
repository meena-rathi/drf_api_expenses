from rest_framework import serializers
from .models import Expense, Budget

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name'] 

class ExpenseSerializer(serializers.ModelSerializer):
    #category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'description', 'date']
        
class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'balance']
        read_only_fields = ['user']



# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profiles
#         fields = ['user', 'bio', 'avatar']