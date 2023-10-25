from django.shortcuts import render
from .models import Subscriber, Blog, Category
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Subscriber  # Import the Subscriber model

# Create your views here.
def home(request):
    post = Blog.objects.all()
    category = Category.objects.all()
    context = {
        "post":post,
        "category":category
    }
    return render(request, 'home.html', context)

def allPost(request):
    post = Blog.objects.all()
    category = Category.objects.all()
    context = {
        "post":post,
        "category":category
    }
    return render(request, 'all-post.html', context)

def details(request):
    post = Blog.objects.all()
    category = Category.objects.all()
    context = {
        "post":post,
        "category":category
    }
    return render(request, 'post.html', context)



def subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_subscriber = Subscriber(user=email)
        new_subscriber.save()

        # Send an email to the admin
        subject = 'New Subscriber'
        message = f'A new subscriber has signed up with the email: {email}'
        from_email = 'partnermarvel55@gmail.com'  # Use the same sender email as configured in settings.py
        recipient_list = ['partnermarvel55@gmail.com']  # Replace with the admin's email address
        send_mail(subject, message, from_email, recipient_list)

        return redirect('success_page')  # Redirect to a success page
    else:
        return HttpResponse('Invalid request')



def carrier(request):
    return render(request, 'carrier.html')

def contact(request):
    return render(request, 'contact.html')
