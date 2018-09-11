from django.shortcuts import render
from .models import DoctorAnalytics
from django.shortcuts import get_object_or_404, HttpResponse
import datetime
# Create your views here.


def doctor_analytics(request, doctor_id):

    doctor = get_object_or_404('doctors.Doctor', pk=doctor_id)

    if not DoctorAnalytics.object.filter(
                            doctor=doctor,
                            session=request.session.session_key):
        view = DoctorAnalytics(doctor=doctor,
                               ip=request.META['RMOTE_ADDR'],
                               created=datetime.datetime.now(),
                               session=request.session.session_key)
        view.save()

    return HttpResponse(u"%s" % DoctorAnalytics.objects.filter(doctor=doctor).count())






# # gets the ip address
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
#
# # records the amount of hits based on the url
#
# def hit_count(request):
#     if not request.session.session_key:
#         request.session.save()
#     s_key = request.session.session_key
#     ip = get_client_ip(request)
#     url, url_created = UrlHit.objects.get_or_create(url=request.path)
#
#     if url_created:
#         track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
#         if created:
#             url.increase()
#             request.session[ip] = ip
#             request.session[request.path] = request.path
#     else:
#         if ip and request.path not in request.session:
#             track, created = HitCount.objects.get_or_create(url_hit=url, ip=ip, session=s_key)
#             if created:
#                 url.increase()
#                 request.session[ip] = ip
#                 request.session[request.path] = request.path
#     return url.hits
#
# def list_analytics(request):
#     views = HitCount.objects.all
#     return views
#     # render(request, 'list_analytics.html', {'views': views})