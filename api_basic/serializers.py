from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # date = serializers.DateTimeField()
    
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author']
        fields = '__all__'
    