from django.db import models

# Create your models here.
class MyModel(models.Model):
    mr_num = models.IntegerField(primary_key=True)
    pr_num = models.IntegerField()
    po_num = models.CharField(max_length=50)

def __str__(self):
    return f'MR: {self.mr_num} MR: {self.pr_num} MR: {self.po_num}'