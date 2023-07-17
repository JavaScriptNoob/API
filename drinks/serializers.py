from rest_framework import serializers
from .models import Drinks
from .models import Article
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','name','description']
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'brand', 'model','description','price','url']