from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'core/home.html')

def how_it_works(request):
    return render(request, 'core/how_it_works.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def faq(request):
    return render(request, 'core/faq.html')

def testimonials(request):
    return render(request, 'core/testimonials.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Compose email message
        email_body = f"""
        New Contact Form Submission
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        try:
            # Send email
            send_mail(
                f'Contact Form: {subject}',
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                ['support@truedna.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent. We\'ll get back to you soon!')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again.')
            
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def terms(request):
    return render(request, 'core/terms.html')

# Order forms
def order_peace_of_mind(request):
    # Implement order form processing here
    return render(request, 'core/order_peace_of_mind.html')

def order_legal_dna(request):
    # Implement order form processing here
    return render(request, 'core/order_legal_dna.html')
def order(request, kit_type):
    # Validate kit type
    if kit_type not in ['peace-of-mind', 'legal-dna']:
        return redirect('pricing')
        
    context = {
        'kit_type': kit_type,
        'kit_type_display': 'Peace of Mind Kit' if kit_type == 'peace-of-mind' else 'Legal DNA Kit'
    }
    
    return render(request, 'core/order.html', context)

def submit_order(request):
    if request.method != 'POST':
        return redirect('pricing')
    
    # Here you would process the order form data
    # For now, we'll just redirect with a success message
    
    # Example:
    # form_data = request.POST
    # new_order = Order(
    #     kit_type=form_data.get('kit_type'),
    #     full_name=form_data.get('full_name'),
    #     # ... and so on
    # )
    # new_order.save()
    
    messages.success(request, 'Your order has been received! We will contact you shortly to confirm.')
    return redirect('home')
