from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from django.core.mail import EmailMultiAlternatives
import math
import random
from .models import UserOTP
from .forms import UserOTPForm
from .models import UserDetail
from .forms import UserDetailForm
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, "home.html")


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_mail(request):
    form = UserOTPForm()
    form = UserDetailForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        from_email = request.POST.get('from_email')
        file = request.POST.get('file')
        UserDetailData = UserDetail(
            name=name, email=email, message=message, from_email=from_email, subject=subject,file=file)
        o = generateOTP()
        print(o)
        genOtp = UserOTP()
        genOtp.otp = o
        genOtp.save()
        savingUserDetail = UserDetailData

        savingUserDetail.save()
        # user.token = token
        template = loader.get_template('contact_form.txt')
        context = {
            'email': email,
            'message': o,
            'subject': "OTP",
            'from_email': from_email,
            'file': file,
        }
        message = template.render(context)

        email = EmailMultiAlternatives(
            "Uthara Print", message,
            "Compny " + "Uthara Print",
            [from_email]
        )
       

        email.content_subtype = 'html'
        

        # userfile = UserDetail()
        # userfile.file=file
        # userfile.save()

        email.send()

        messages.success(
            request, 'Message sent successfully ! I will ansewr you as soon as possibile....')
        return HttpResponseRedirect('otp_verify')

    return render(request, 'home.html', {'form': form})


def otp_verify(request):
    if request.method == 'POST':
        form = UserOTP.objects.latest('id')
        latestOTP = form.otp
        print(latestOTP)
        otp = request.POST.get('otp')
        if latestOTP == int(otp):
            print("verified")
            userFormModel = UserDetail.objects.latest('id')
            print(userFormModel)
            template = loader.get_template('contact_form.txt')
            context = {
                'name': userFormModel.name,
                'email': userFormModel.email,
                'message': userFormModel.message,
                'subject': userFormModel.subject,
                'from_email': userFormModel.from_email,
                'file': userFormModel.file,
            }
             
            message = template.render(context)

            email = EmailMultiAlternatives(
                "Uthara Print", message,
                "Compny " + "Uthara Print",
                [userFormModel.email],
            )
            
            email.content_subtype = 'html'
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(
                request, 'Message sent successfully ! I will ansewr you as soon as possibile....')
            return HttpResponseRedirect('home')
        else:
            print("not verified")
    return render(request, 'otp.html')


# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.contrib import messages
# from django.template import loader
# from django.core.mail import EmailMultiAlternatives

# # Create your views here.
# def home(request):
#     return render(request, "home.html")

# def send_mail(request):
#     # form = emailssForm()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subject = request.POST.get('subject')
#         from_email = request.POST.get('from_email')
#         # file = request.POST.get('file')

#         template = loader.get_template('contact_form.txt')
#         context = {
#             'name': name,
#             'email': email,
#             'message': message,
#             'subject': subject,
#             'from_email':from_email,
#             # 'file' : file,

#         }

#         message = template.render(context)

#         email = EmailMultiAlternatives(
#             "Uthara Print", message,
#             "Compny " + "Uthara Print",
#             ['mailto:pandayharsh472@gmail.com',from_email]
#         )
#         # msg = EmailMultiAlternatives(
#         #     subject,message,name,[from_email],

#         # )

#         email.content_subtype = 'html'
#         file = request.FILES['file']
#         email.attach(file.name, file.read(), file.content_type)
#         email.send()

#         messages.success(request, 'Message sent successfully ! I will ansewr you as soon as possibile....')
#         return HttpResponseRedirect('/')
