from django.shortcuts import HttpResponse
import subprocess
import os
# Create your views here.


# def CallPage(request):
#     return HttpResponse(request, 'index.html')


def users(request):
    script_path = r'Scripts\main.py'
    if not os.path.exists(script_path):
        return HttpResponse(f"Error: File not found at {script_path}")

    try:
        subprocess.Popen(['python', script_path],shell=False)
        return HttpResponse("Tkinter application started.")
    except Exception as e:
        return HttpResponse(f"Error: {e}")