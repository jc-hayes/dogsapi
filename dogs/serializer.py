from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    size = serializers.ChoiceField(choices=Breed.SIZE_CHOICES)
    friendliness = serializers.ChoiceField(choices=Breed.Rating.choices)
    trainability = serializers.ChoiceField(choices=Breed.Rating.choices)
    shedding_amount = serializers.ChoiceField(choices=Breed.Rating.choices)
    exercise_needs = serializers.ChoiceField(choices=Breed.Rating.choices)
    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'shedding_amount',
            'exercise_needs')

# •	name (a character string)
# •	size (a character string) [should accept Tiny, Small, Medium, Large]
# •	friendliness (an integer field) [should accept values from 1-5]
# •	trainability (an integer field) [should accept values from 1-5]
# •	sheddingamount (an integer field) [should accept values from 1-5]
# •	exerciseneeds (an integer field) [should accept values from 1-5]

class DogSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.ChoiceField(choices=Dog.GENDER_CHOICES)
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'age',
            'breed',
            'gender',
            'color',
            'favorite_food',
            'favorite_toy')