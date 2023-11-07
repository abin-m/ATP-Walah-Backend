from django.db import models
from django.contrib.auth.models import User

class ATPDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ATPDocumentDetails(models.Model):
    atp_document = models.ForeignKey(ATPDocument, on_delete=models.CASCADE)
    testcase_id = models.CharField(max_length=50)
    prerequisits = models.TextField()
    steps = models.TextField()
    results = models.TextField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.testcase_id
