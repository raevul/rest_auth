from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_confirmation_email(user):

    context = {
        "small_text_detail": """
        Thank you for creating an account. 
        Please verify your email
        """,
        "email": user.email,
        "activation_code": user.activation_code
    }
    msg_html = render_to_string("email.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Account activation"
    to_email = user.email
    mail.send_mail(
        subject,
        plain_message,
        "dastan.alymbekov@data-ox.com",
        [to_email],
        html_message=msg_html
    )
