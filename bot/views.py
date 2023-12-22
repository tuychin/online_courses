from django.shortcuts import redirect


def redirect_to_bot(request):
    return redirect('https://t.me/my_online_courses_bot')
