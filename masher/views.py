from django.shortcuts import render


def index(request):
    """Home page of site"""

    # render html
    return render(
        request,
        'masher/index.html',
        {},
    )
