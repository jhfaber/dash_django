from django.db import models

# Create your models here.



class TypeInfluencer(models.Model):
    name = models.CharField(max_length=255)     

    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)

class Medium(models.Model):
    name = models.CharField(max_length=255)
    id_view = models.IntegerField()

class Campaign(models.Model):
    name = models.CharField(max_length=255)    
    amount = models.FloatField()
    ini_date = models.DateField()
    end_date = models.DateField()
    
    #created the thought table automatically
    country = models.ManyToManyField(Country)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)


class Influencer(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    name_ga= models.CharField(max_length=255)  
    
    
    type_element = models.ForeignKey(TypeInfluencer, on_delete=models.CASCADE)
    # created a third table, overriding default behaviour
    campaign = models.ManyToManyField(Campaign, through='InfluencerCampaign')


    def __str__(self):
        return self.name

# through table
class InfluencerCampaign(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount_spend = models.FloatField()
    date = models.DateField()


# class Element(models.Model):
#     title = models.CharField(max_length=255)
#     rl_clean = models.CharField(max_length=255)
#     description= models.TextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     type_element = models.ForeignKey(TypeElement, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    