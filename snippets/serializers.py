from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICE

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50, allow_blank=True, required=False)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    boolean = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='Node',)
    style = serializers.ChoiceField(choices=STYLE_CHOICE, default='STYLE',)

    def create(self, validated_data):
        """
        create snippet instance
        :param validated_data:
        :return: snippet instance, given the validated data
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update and return an existing 'Snippet' instance, given the validated data
        :param instance:
        :param validated_data:
        :return:
        """

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.boolean = validated_data.get('boolean', instance.boolean)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
