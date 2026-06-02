from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm
from .emails import send_admin_notification, send_thankyou_email

def contact_view(request):
    form = EnquiryForm()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()
            try:
                send_admin_notification(enquiry)
                send_thankyou_email(enquiry)
                messages.success(request, "✅ Thank you! We've received your enquiry and will contact you soon.")
            except Exception as e:
                print(f"Email error: {e}")
                messages.success(request, "✅ Your message was saved! We'll contact you soon.")
            return redirect('contact')
        else:
            messages.error(request, "❌ Please fix the errors below.")

    return render(request, 'contact/contact.html', {'form': form})