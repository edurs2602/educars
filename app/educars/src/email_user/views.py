import os
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_welcome_email(user_email, first_name, last_name, date_joined):

    try:
        current_year = datetime.now().year  # Obter o ano atual

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "date_joined": date_joined,
            "year": current_year  # Passar o ano atual para o contexto
        }

        receiver_email = user_email
        template_name = os.path.join(settings.BASE_DIR, 'src', 'email_user', 'templates', 'welcome.html')
        try:
            convert_to_html_content = render_to_string(
                template_name=template_name,
                context=context
            )
        except TemplateDoesNotExist:
            logger.error(f"Template {template_name} does not exist.")
            return False

        plain_message = strip_tags(convert_to_html_content)

        sent = send_mail(
            subject="Welcome to Educars",
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[receiver_email],
            html_message=convert_to_html_content,
            fail_silently=False
        )

        return sent > 0

    except BadHeaderError:
        logger.error("Invalid header found.")
        return False
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return False
