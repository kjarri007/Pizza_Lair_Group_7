from django.shortcuts import render


def hendler400(request, exception):
    return render(request, "400.html", status=400)


def hendler403(request, exception):
    return render(request, "403.html", status=403)


def hendler404(request, exception):
    return render(request, "404.html", status=404)


def hendler500(request):
    return render(request, "500.html", status=500)
