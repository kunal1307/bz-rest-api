from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default='Active')
    created = models.DateTimeField()
    last_modified_date = models.DateTimeField(null=True, blank=True)
    agency = models.CharField(max_length=100, null=True, blank=True)
    logo_url = models.CharField(max_length=1024, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_campaigns(self):
        return self.campaign_set.all()
