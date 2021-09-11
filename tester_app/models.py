from django.db import models

# Create your models here.
class Question(models.Model):
    #options = models.ArrayField(models.ArrayField( models.CharField(max_length=200), blank=True,null=True, default=dict))

   
    question = models.TextField()
    # question_type = models.CharField(max_length=60, choices=QUESTION_TYPES, default='Textbox')
    # question_type = models.CharField(max_length=60, default='Textbox')
    # helps = models.CharField(max_length=5000, blank=True)
    # mandatory = models.BooleanField(blank=False, default=True)
    def __str__(self):
        # return '%s in %s of %s' % (, , )
        return self.question


class Option(models.Model):
     question = models.ForeignKey(Question, on_delete=models.CASCADE)
     text = models.TextField()

     def __str__(self):
         return self.text


