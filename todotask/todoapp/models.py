from django.db import models
# Create your models here.
class userDetail(models.Model):
    username=models.CharField(max_length=264)
    location=models.CharField(max_length=264)
    date=models.DateField()
    
    def __str__(self):
        return self.username
        
class taskDetail(models.Model):
    username=models.OneToOneField(userDetail,on_delete=models.CASCADE)
    task=models.CharField(max_length=264)
    status=models.CharField(max_length=25)
    
    # def __str__(self):
    #     return self.username