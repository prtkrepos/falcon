from problems.models import Problems
from submissions.models import Submissions
from django.shortcuts import render


def handle_uploaded_file(uploaded_file, language, sid):
    """
    Upload the file
    """
    filename = "~/falcon/allSubmissions/" + sid
    if language == 'C':
        filename += ".c"
    elif language == 'C++':
        filename += ".cpp"
    with open(filename, "w") as f:
        for line in uploaded_file:
            f.write(line)


def problem_page(request):
    """
    Problem Page View
    """
    if request.method == 'POST':
        submission = Submissions.objects.create()
        sid = submission.id
        language = request.POST['language']
        handle_uploaded_file(request.FILES['solution'], language, sid)
        submission.language = language
        pid = request.GET['pid']
        submission.pid = pid
        template = 'game.html'
        ctx = {}
        ctx['submission'] = submission
        return render(request, template, ctx)
    else:
        pid = request.GET['pid']
        problem = Problems.objects.get(id=pid)
        template = 'problems.html'
        ctx = {}
        ctx['problem_name'] = problem.problem_name
        ctx['problem_statement'] = problem.problem_statement
        ctx['starting_state'] = problem.starting_state
        return render(request, template, ctx)
