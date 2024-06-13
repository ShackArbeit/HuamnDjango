from django.shortcuts import render,redirect
from UserBack import models

def UserBack(request):
      return render(request,'UserBack.html',locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'Listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    message = '如要張貼訊息，則每一個欄位都要填...'
    if request.method=='POST':
        user_id = request.POST.get('user_id')
        user_pass = request.POST.get('user_pass')
        user_post = request.POST.get('user_post')
        user_mood = request.POST.get('mood')
        if user_id != None:
            mood = models.Mood.objects.get(status=user_mood)
            post = models.Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            return redirect("/list/")
    return render(request, "Posting.html", locals())
