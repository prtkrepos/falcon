from django.shortcuts import render



def game_page(request):
    """
    Game Page View
    """
    template = 'game.html'
    ctx = {}
    return render(request, template, ctx)
