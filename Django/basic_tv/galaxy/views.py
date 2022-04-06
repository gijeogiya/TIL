from django.shortcuts import render


def ping(request):
    return render(request, 'galaxy/ping.html')


def pong(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    elif request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']

    context = {
        'username': username,
        'password': password,
    }
    return render(request, 'galaxy/pong.html', context)


# browser 에서 POST 요청 보내는 방법 => <form method="POST">
def pingpong(request):
    if request.method == 'GET':
        return render(request, 'galaxy/form.html')

    elif request.method == 'POST':

        c = int(request.POST['temperature'])
        f = c * 1.8 + 32

        context = { 'f': f, }
        return render(request, 'galaxy/result.html', context)