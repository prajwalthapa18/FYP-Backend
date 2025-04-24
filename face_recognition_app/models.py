from django.db import models

class DetectedUser(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user_id = models.IntegerField(unique=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    image = models.ImageField(
        upload_to="detected_users/",
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  # Newest entries first by default

    def __str__(self):
        return f"User {self.user_id} – {self.gender}"


class GenderCount(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = models.CharField(
        max_length=10,
        unique=True,
        choices=GENDER_CHOICES
    )
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gender}: {self.count}"


class Counter(models.Model):
    id = models.AutoField(primary_key=True)
    last_user_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Last User ID: {self.last_user_id}"

class DetectedUser(models.Model):
    # primary key (id) is added automatically
    gender = models.CharField(max_length=10, choices=[("Male","Male"),("Female","Female")])
    image  = models.ImageField(upload_to="detected_users/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User ID: {self.id}, Gender: {self.gender}"  # Include primary key (id)