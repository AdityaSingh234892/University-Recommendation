from django.db import models

class University(models.Model):
    UniversityIndex = models.AutoField(primary_key=True, default=None)
    UniversityName = models.CharField(max_length=255)
    GREscore = models.IntegerField(default=0)
    GPA = models.FloatField(default=0.0)
    IELTSscore = models.FloatField(default=0.0)
    ResearchPaper = models.IntegerField(default=0)
    UniversityRanking = models.IntegerField(default=0)
    AdmitProbability = models.FloatField(default=0.0)
    country = models.CharField(max_length=50, default='US')
    course = models.CharField(max_length=255, default='CS/CE')

    def __str__(self):
        return self.UniversityName


class StudentsData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    board = models.CharField(max_length=100, default="CBSE")
    degree = models.CharField(max_length=10, choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')])
    course = models.CharField(max_length=100, blank=True, null=True)
    course_score = models.FloatField(blank=True, null=True, default=0.0)
    score12 = models.FloatField(default=0.0)
    score10 = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            self.course_score = float(self.course_score)
        except ValueError:
            self.course_score = None
        super(StudentsData, self).save(*args, **kwargs)