from django.db import models

class ContactInfo(models.Model):
    profile = models.OneToOneField('portfolio.Profile', on_delete=models.CASCADE, related_name='contact_info')
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Contacts for {self.profile.user.username}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
    
    def __str__(self):
        return f'{self.name} ({self.email}) - {self.created_at.strftime("%d.%m.%Y %H:%M")}'