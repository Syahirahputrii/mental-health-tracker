from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275216',
        'name': 'Syahirah Putri Aisyah',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

