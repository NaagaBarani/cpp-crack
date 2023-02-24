from django.db import models
# Create your models here.
class ProjIdea(models.Model):

    title = models.CharField(max_length=200)
    student_Id = models.CharField(max_length=30)
    mail_Id = models.CharField(max_length=30)
    submit_date = models.CharField('submit_date')
    genre = models.CharField(max_length=500)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.title + " - " + self.student_Id