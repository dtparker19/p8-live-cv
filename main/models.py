from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    middleinitial = models.CharField(max_length=5)
    lastname = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='images/', max_length=50)
    phone = models.CharField(max_length=14)
    website = models.URLField()
    summary = models.TextField()
    address = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    countrycode = models.CharField(max_length=2)
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        return ' '.join([self.firstname, self.middleinitial, self.lastname]).title()


class Profile(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE, related_name='profile_set', related_query_name='profile_set')

    FACEBOOK = 'FB'
    TWITTER = 'TW'
    LINKEDIN = 'LI'
    NETWORK_CHOICES = (
        (FACEBOOK, 'Facebook'),
        (TWITTER, 'Twitter'),
        (LINKEDIN, 'Linkedin'),
    )

    network = models.CharField(max_length=2, choices=NETWORK_CHOICES)
    username = models.CharField(max_length=150)
    url = models.URLField()

    class Meta:
        unique_together = ('resume', 'network')

    def __str__(self):
        return self.network + " " + self.resume.user.email

class Work(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    volunteer = models.BooleanField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    website = models.URLField()
    startDate = models.DateField()
    endDate = models.DateField()
    summary = models.TextField()

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.resume.user.email + " - " + self.company

class WorkHighlight(models.Model):
    work = models.ForeignKey(Work,on_delete=models.CASCADE)

    highlight = models.TextField()

    def __str__(self):
        return self.highlight[:30] + " - " + self.work.company + " - " + self.work.resume.user.email


class Education(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    institution = models.CharField(max_length=150)
    area = models.CharField(max_length=100)
    studyType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    gpa = models.CharField(max_length=3)

    class Meta:
        ordering = ['-startDate']

    def __str__(self):
        return self.area + " - " + self.institution + " - " + self.resume.user.email

class Course(models.Model):
    education = models.ForeignKey(Education,on_delete=models.CASCADE)

    coursecode = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.coursecode + " - " + self.education.institution

class Award(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    date = models.DateField()
    awarder = models.CharField(max_length=100)
    summary = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.resume.user.email + " - " + self.title + " - " + self.awarder


class Publication(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    releaseDate = models.DateField()
    website = models.URLField()
    summary = models.TextField()

    class Meta:
        ordering = ['-releaseDate']

    def __str__(self):
        return self.resume.user.email + " - " + self.name + " - " + self.publisher


class Skill(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.resume.user.email + " - " + self.name


class Keyword(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class SkillKeyword(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('skill', 'keyword')

    def __str__(self):
        return self.skill.resume.user.email + " - " + self.skill.name + " - " + self.keyword.word


class Language(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)

    def __str__(self):
        return self.resume.user.email + " - " + self.name

class Interest(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.resume.user.email + " - " + self.name

class InterestKeyword(models.Model):
    interest = models.ForeignKey(Interest,on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('interest', 'keyword')

    def __str__(self):
        return self.interest.resume.user.email + " - " + self.interest.name + " - " + self.keyword.word

class Reference(models.Model):
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.resume.user.email + " - " + self.name

class Image(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    alt_image = models.URLField(null=True, blank=True)
    attribution = models.TextField(blank=True)

    def __str__(self):
        return self.name
