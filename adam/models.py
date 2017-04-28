from django.db import models

# Create your models here.


class Questions(models.Model):

    prim_id = models.AutoField(primary_key=True)
    question = models.TextField(null=False)
    type = models.CharField(max_length=100, null=True)
    terms = models.TextField(null=True)
    query = models.TextField(null=True)
    answer = models.TextField(null=True)

    class Meta:
        db_table = 'Questions'
