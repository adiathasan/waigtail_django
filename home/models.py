from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page


class HomePage(Page):
    templates = 'home/home_page.html'
    max_count = 1
    product_title = models.CharField(max_length=100, blank=False, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('product_title')
    ]

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'
