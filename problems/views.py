from problems.models import Problem
from problems.forms import ProblemForm


def problem_page(request):
    if request.method == 'POST':
    else:
        problem = Problem.objects.create()

