from django.shortcuts import render
import requests, json


def login(request):
    uname = request.POST['name']
    password = request.POST['password']
    res = requests.get('http://192.168.43.103:8000/checkuser/'+uname+'/'+password+'/')
    if res.status_code == 200:
        return render(request, 'welcomemerchant.html')
    else:
        return render(request, 'login.html', {"message": 'Invalid Username and Password'})


def reset(request):
    return render(request, 'reset.html')


def resetcheck(request):
    uname = request.POST['name']
    new_pass = request.POST['new_password']
    conf_pass = request.POST['conf_password']
    data = {'password': new_pass}
    new_changepass = json.dumps(data)
    res = requests.put('http://192.168.43.103:8000/resetpassword/'+uname+'/', data=new_changepass)
    if new_pass == conf_pass:
        if res.status_code == 200:
            return render(request, 'login.html', {'me': "Password Updated Successfully"})
        else:
            return render(request, 'reset.html', {'message1': 'Invalid Email Id'})
    else:
        return render(request, 'reset.html', {"message1": 'Password Not Matched'})


def changepass(request):
    return render(request, 'change.html')


def changecheck(request):
    uname = request.POST['name']
    old_pass = request.POST['old_password']
    new_pass = request.POST['new_password']
    conf_pass = request.POST['conf_password']
    data = {'password': new_pass}
    new_changepass = json.dumps(data)
    res = requests.put('http://192.168.43.103:8000/changepassword/' + uname + '/' + old_pass + '/', data=new_changepass)
    if new_pass == conf_pass:
        if res.status_code == 200:
            return render(request, 'login.html', {'me': "Password Updated Successfully"})
        else:
            return render(request, 'change.html', {'message1': 'Invalid Email Id and Password'})
    else:
        return render(request, 'change.html', {"message1": 'Password Not Matched'})


def logout(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'welcomemerchant.html')
