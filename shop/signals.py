from email.message import EmailMessage
import smtplib
from django.dispatch import receiver
from .models import Order
from django.db.models.signals import post_save
from shopnify import settings
from email.message import EmailMessage



