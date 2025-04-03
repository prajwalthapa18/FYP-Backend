from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    @classmethod
    def count_genders(cls):
        male_count = cls.objects.filter(gender='M').count()
        female_count = cls.objects.filter(gender='F').count()
        return {'Male': male_count, 'Female': female_count}

    def __str__(self):
        return self.get_gender_display()

class Count(models.Model):
    male_count = models.IntegerField(default=0)
    female_count = models.IntegerField(default=0)

    @classmethod
    def update_counts(cls):
        counts = Person.count_genders()
        count_obj, created = cls.objects.get_or_create(id=1)  # Ensure single instance
        count_obj.male_count = counts['Male']
        count_obj.female_count = counts['Female']
        count_obj.save()

    def __str__(self):
        return f"Male: {self.male_count}, Female: {self.female_count}"
