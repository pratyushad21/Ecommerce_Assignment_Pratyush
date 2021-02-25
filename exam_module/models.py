from django.db import models

# Create your models here.
class LabExam(models.Model):
    
    ExamDate = models.DateField()
    ExamName = models.CharField(max_length = 200)
    ExamDescription = models.TextField()
    TotalMarks = models.FloatField()
    PassMarks = models.FloatField()
    ExamStatus = models.BooleanField()

    class Meta:
        verbose_name_plural = "LabExam"