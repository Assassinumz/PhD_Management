from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField

# Create your models here.
class User(AbstractUser):
    paper_status = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected')
    )

    genders = (
        ('not specified', 'not specified'),
        ('male', 'male'),
        ('female', 'female'),
    )

    profile_picture = pub_2 = models.TextField(null=True, blank=True, default="https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg")

    roll_number = models.CharField(blank=True, null=True, max_length=60)
    mobile_number = models.CharField(blank=True, null=True, max_length=60)

    gender = models.CharField(default="Not Specified", max_length=60)
    research_area = models.CharField(blank=True, null=True, max_length=60)

    father_name = models.CharField(blank=True, null=True, max_length=60)
    mother_name = models.CharField(blank=True, null=True, max_length=60)
    
    guardian_name = models.CharField(blank=True, null=True, max_length=60)
    address = models.TextField(blank=True, null=True,)
    time_table = models.TextField(null=True, blank=True, default=None)

    publications = JSONField(default={}, blank=True)
    patent = JSONField(default={}, blank=True)
    conference = JSONField(default={}, blank=True)

    pub_1 = models.TextField(null=True, blank=True, default=None, name='paper_1')
    pub_1_check = models.TextField(choices=paper_status, default='pending')

    pub_2 = models.TextField(null=True, blank=True, default=None, name='paper_2')    
    pub_2_check = models.TextField(choices=paper_status, default='pending')

    pub_3 = models.TextField(null=True, blank=True, default=None, name='paper_3')
    pub_3_check = models.TextField(choices=paper_status, default='pending')

    cv = models.TextField(null=True, blank=True, default=None, name='cv')
    cv_check = models.TextField(choices=paper_status, default='pending')
    
    pub_4 = models.TextField(null=True, blank=True, default=None, name='paper_4')
    pub_4_check = models.TextField(choices=paper_status, default='pending')

    pub_5 = models.TextField(null=True, blank=True, default=None, name='paper_5')
    pub_5_check = models.TextField(choices=paper_status, default='pending')

    aps = models.TextField(null=True, blank=True, default=None, name='aps')
    aps_check = models.TextField(choices=paper_status, default='pending')

    pub_6 = models.TextField(null=True, blank=True, default=None, name='paper_6')
    pub_6_check = models.TextField(choices=paper_status, default='pending')

    pre_synopsis = models.TextField(null=True, blank=True, default=None, name='pre_synopsis')
    pre_synopsis_check = models.TextField(choices=paper_status, default='pending')

    pub_7 = models.TextField(null=True, blank=True, default=None, name='paper_7')
    pub_7_check = models.TextField(choices=paper_status, default='pending')

    thesis = models.TextField(null=True, blank=True, default=None)
    thesis_check = models.TextField(choices=paper_status, default='pending')

    pdc = models.TextField(null=True, blank=True, default=None,)
    pdc_check = models.TextField(choices=paper_status, default='pending')

    def save(self, *args, **kwargs):
        if not self.paper_1:
            self.paper_1 = None
        if not self.paper_2:
            self.paper_2 = None
        if not self.paper_3:
            self.paper_3 = None
        if not self.cv:
            self.cv = None
        if not self.paper_4:
            self.paper_4 = None
        if not self.paper_5:
            self.paper_5 = None
        if not self.aps:
            self.aps = None
        if not self.paper_6:
            self.paper_6 = None
        if not self.pre_synopsis:
            self.pre_synopsis = None
        if not self.paper_7:
            self.paper_7 = None
        if not self.thesis:
            self.thesis = None
        if not self.pdc:
            self.pdc = None
        super(User, self).save(*args, **kwargs)