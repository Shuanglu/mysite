from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Issue, Option
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
#def index(request):
#    latest_issue_list = Issue.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_issue_list': latest_issue_list,
#    }
#    return HttpResponse(template.render(context, request))


#def index(request):
#    latest_issue_list =Issue.objects.order_by('-pub_date')[:5]
#    context = {'latest_issue_list': latest_issue_list}
#    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
     template_name = 'polls/index.html'
     context_object_name = 'latest_issue_list'

     def get_queryset(self):
         """Return the last five published issues."""
         return Issue.objects.filter(
	     pub_date__lte=timezone.now()    
	  ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
     model = Issue
     template_name = 'polls/detail.html'
     def get_queryset(self):
	 """
	 Excludes any issues that aren't published yet.
	 """
	 return Issue.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
     model = Issue
     template_name = 'polls/results.html'


#def detail(request,issue_id):
    #try:
    #	issue = Issue.objects.get(pk=issue_id)
    #except Issue.DoesNotExist:
    #    raise Http404("Issue does not exit")
    #return render(request, 'polls/detail.html', {'issue': issue})
    #return HttpResponse("You're looking at issue %s." %issue_id)
#    issue = get_object_or_404(Issue, pk=issue_id)
#    return render(request, 'polls/detail.html', {'issue': issue})	
#def results(request, issue_id):
#    response = "You're looking at the results of issue %s."
#    return HttpResponse(response %issue_id)

def vote(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    try:
        selected_option = issue.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
    # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
        'issue': issue,
        'error_message': "You didn't select a option.",
    })
    else:
        selected_option.votes += 1
        selected_option.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.	
        return HttpResponseRedirect(reverse('polls:results', args=(issue.id,)))

#def results(request, issue_id):
#    issue = get_object_or_404(Issue, pk=issue_id)
#    return render(request, 'polls/results.html', {'issue': issue})
