from django.db import models

# Create your models here.
class Problems(models.Model):
    """
    Problem details
    """
    problem_name = models.CharField(max_length=300)
    next_state_generator = models.FilePathField(path="~/falcon/problems/nextStateGenerator/")
    starting_state = models.FilePathField(path="~/falcon/problems/startingStates/")
    problem_statement = models.FilePathField(path="~/falcon/problems/problemStatement/")

