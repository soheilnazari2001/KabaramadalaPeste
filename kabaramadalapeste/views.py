from django.shortcuts import render
from django.http import Http404


def game(request):
    raise Http404
    '''
    return render(request, 'kabaramadalapeste/game.html', {
        'without_nav': True,
        'without_footer': True,
    })
    '''