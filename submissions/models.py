from django.db import models

CHOICES = (
    ('C', 'c'),
    ('C++', 'c++'),
)

class Submissions(models.Model):
    """
    Stores the submission details
    """
    pid = models.IntegerField()
    language = models.CharField(max_length='3', choices=CHOICES)
    filepath = models.FilePathField(path='~/falcon/allSubmissions/')
