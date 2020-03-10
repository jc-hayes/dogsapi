from django.db import models

# Breed Model
# •	name (a character string)
# •	size (a character string) [should accept Tiny, Small, Medium, Large]
# •	friendliness (an integer field) [should accept values from 1-5]
# •	trainability (an integer field) [should accept values from 1-5]
# •	sheddingamount (an integer field) [should accept values from 1-5]
# •	exerciseneeds (an integer field) [should accept values from 1-5]
class Breed(models.Model):
    name = models.CharField(max_length=100)
    TINY='T'
    SMALL='S'
    MEDIUM='M'
    LARGE='L'
    SIZE_CHOICES = (
        (TINY,'Tiny'),
        (SMALL,'Small'),
        (MEDIUM,'Medium'),
        (LARGE,'Large'),
    )
    size = models.CharField(
        max_length=6,
        choices=SIZE_CHOICES,
        default=MEDIUM
    )
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    friendliness = models.IntegerField(choices=Rating.choices)
    trainability = models.IntegerField(choices=Rating.choices)
    shedding_amount = models.IntegerField(choices=Rating.choices)
    exercise_needs = models.IntegerField(choices=Rating.choices)


# Dog model
# •	name (a character string)
# •	age (an integer)
# •	breed (a foreign key to the Breed Model)
# •	gender (a character string)
# •	color (a character string)
# •	favoritefood (a character string)
# •	favoritetoy (a character string)
class Dog(models.Model):
    MALE='M'
    FEMALE='F'
    GENDER_CHOICES=(
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    breed = models.ForeignKey(
        Breed,
        related_name='breeds',
        on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=FEMALE,
    )
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)
    class Meta:
        ordering = ('name',)