from rest_framework import serializers 
from .models import Adventure 

class AdventureSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Adventure # tell django which model to use
        fields = ('id', 'health', 'attack', 'accuracy', 'weapons', 'items', 'villains') # tell django which fields to include
