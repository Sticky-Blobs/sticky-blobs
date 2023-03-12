from six import text_type
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)
        )
    
account_activation_token = TokenGenerator()




def send_verification_mail(recipient_email: str, verification_link: str):
    message = render_to_string('mails/users/verification_mail.html', {
        "verification_link": verification_link})
    to_email = recipient_email
    raw_message = strip_tags(message)
    mail_subject = 'Email Verification for Sticky Blobs'
    from_email = '%s <noreply@%s>' % ('Sticky Blobs', 'stickyblobs.com')
    mail.send_mail(mail_subject, raw_message, from_email,
                   [to_email], html_message=message)