from django.db import models

class Enquiry(models.Model):
    company_name    = models.CharField(max_length=200)
    person_name     = models.CharField(max_length=100)
    email           = models.EmailField()
    phone           = models.CharField(max_length=20)
    enquiry_details = models.TextField()
    submitted_at    = models.DateTimeField(auto_now_add=True)
    is_read         = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.company_name} — {self.person_name}"