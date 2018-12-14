from django.db import models


class List(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List: {}".format(self.name)


class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Card: {}".format(self.title)
