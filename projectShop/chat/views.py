# Create your views here.
from django.shortcuts import render, redirect
 
 
def chatPage(request, *args, **kwargs):
    print("2qqq1322154563")
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)
