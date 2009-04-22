# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

#SJL http://www.djangobook.com/en/1.0/chapter16/ is amazing

from django.db import models
from django.forms import ModelForm
import datetime 


class Tag(models.Model):
    # automatic! id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=140, blank=True)
    time = models.DateTimeField(default=datetime.datetime.now) 
    
    def __unicode__(self):
        return self.tag

    class Meta:
        db_table = u'tags'

class Instruction(models.Model):
    # automatic! id = models.AutoField(primary_key=True)
    instruction_text = models.TextField()
    is_exclusive = models.BooleanField()
    task_reward = models.DecimalField(max_digits=6, decimal_places=2)
    messages_per_task= models.IntegerField()
    min_agreement_percentage = models.IntegerField()
    max_workers_per_message = models.IntegerField()
    available_tags = models.ManyToManyField(Tag, blank=True)
    creation_time = models.DateTimeField(default=datetime.datetime.now) 
    
    def __unicode__(self):
        return self.instruction_text
        
    class Meta:
        db_table = u'instructions'

class OrigMessage(models.Model):
    new_id = models.AutoField(primary_key=True)
    assigned_tags = models.ManyToManyField(Tag, blank=True)
    assigned_instructions = models.ManyToManyField(Instruction, blank=True)
 
    id = models.IntegerField()
    transaction_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=90, blank=True)
    monitor_id = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField()
    is_outgoing = models.IntegerField()
    message = models.TextField()
    is_virtual = models.IntegerField()
    
    def __unicode__(self):
        return self.message
    
    class Meta:
        db_table = u'orig_messages'


class InstructionForm(ModelForm):
    class Meta:
        model = Instruction
        exclude = ['creation_time']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ['time']

# gooood article http://www.pointy-stick.com/blog/2009/01/23/advanced-formset-usage-django/
