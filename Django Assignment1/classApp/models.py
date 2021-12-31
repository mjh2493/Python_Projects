from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    CourseNumber = models.IntegerField(blank=True)
    InstructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Title
