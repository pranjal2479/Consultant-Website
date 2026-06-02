from django.core.mail import send_mail
from django.conf import settings

ADMIN_EMAIL = 'sales@crestservdigital.com'

def send_admin_notification(enquiry):
    subject = f"New Enquiry — {enquiry.company_name}"
    message = f"""
New enquiry received on Crestserv Digital website.

Company  : {enquiry.company_name}
Person   : {enquiry.person_name}
Email    : {enquiry.email}
Phone    : {enquiry.phone}

Enquiry Details:
{enquiry.enquiry_details}

Submitted at : {enquiry.submitted_at.strftime('%d %b %Y, %I:%M %p')}
    """.strip()
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [ADMIN_EMAIL], fail_silently=False)


def send_thankyou_email(enquiry):
    subject = "Thank you for contacting Crestserv Digital Learning!"
    message = f"""
Dear {enquiry.person_name},

Thank you for reaching out to Crestserv Digital Learning!

We have received your enquiry from {enquiry.company_name} and truly appreciate you connecting with us.

Our team will get back to you within 24 hours with all the information you need.

If you have any urgent queries, feel free to reach us at:
📧 sales@crestservdigital.com
📞 +91 98765 43210

Warm regards,
Team Crestserv Digital Learning
Mumbai, Maharashtra, India
    """.strip()
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [enquiry.email], fail_silently=False)