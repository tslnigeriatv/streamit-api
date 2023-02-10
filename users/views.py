from django.shortcuts import render
from django.core.mail import send_mail

def my_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            message,
            'talk2peteresezobor@gmail.com',
            ['petercodercoder@gmail.com', ],
            fail_silently=False
        )
    return render(request, 'email/user_reset_password.html', {})