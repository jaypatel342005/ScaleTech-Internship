from rest_framework import serializers
from .models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
    def validate(self, attrs):
        if attrs['comment'] == '':
            raise serializers.ValidationError({'comment': 'Comment cannot be empty'})
        if attrs['author'] == '':
            raise serializers.ValidationError({'author': 'Author cannot be empty'})
        return attrs

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'



    