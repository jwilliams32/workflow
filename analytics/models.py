from django.db import models

# gets the url data and increases its count by one base on the url visited
class DoctorAnalytics(models.Model):
    doctor  = models.ForeignKey('doctors.Doctor', related_name='doctorsanalytics',on_delete=models.CASCADE)
    ip      = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    date    = models.DateTimeField(auto_now=True)




#
# class UrlHit(models.Model):
#     url     = models.URLField()
#     hits    = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return '{0}'.format(self.url)
#
#     def increase(self):
#         self.hits += 1
#         self.save()
#
#
# # Page view count model
# class HitCount(models.Model):
#     url_hit = models.ForeignKey(UrlHit, editable=False, on_delete=models.CASCADE)
#     ip      = models.CharField(max_length=40)
#     session = models.CharField(max_length=40)
#     date    = models.DateTimeField(auto_now=True)