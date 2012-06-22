from votes.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def list_options(request,contest):
	contest = get_object_or_404(Contests,title=contest)
	options = Options.objects.filter(contest=contest)
	return render_to_response('list.html',{'contest':contest,'options':options})

def ballot(request, contest):
	contest = get_object_or_404(Contests,title=contest)
	options = Options.objects.filter(contest=contest)
	rules   = get_object_or_404(Rules, pk=contest.rules)
	return render_to_response('ballot.html',{'contest':contest,'options':options}, context_instance=RequestContext(request))

def vote(request, contest_id):
	contest =get_object_or_404(Contests,pk=contest_id)
	for vote in request.POST:
		if vote !='csrfmiddlewaretoken' and request.POST[vote] != 0: 
			add_vote = Votes(contest=contest, option=Options.objects.get(pk=vote),vote_value=request.POST[vote])
			add_vote.save()
	return HttpResponseRedirect(reverse('votes.views.results', args=(contest.id,)))

def results(request, contest_id):
	contest = get_object_or_404(Contests,pk=contest_id)
	options = Options.objects.filter(contest=contest)
	votes   = dict([(option.title,Votes.objects.filter(contest=contest,option=option)) for option in options])
	votes_added = {}
	for vote in votes:
		votes_added[vote] = 0
		for v in votes[vote]:
			votes_added[vote] += v.vote_value
	return render_to_response('results.html',{'votes_added':votes_added})

def option(request,contest_id,option_id):
	contest = get_object_or_404(Contests,pk=contest_id)
	option  = get_object_or_404(Options,pk=option_id)
	return render_to_response('option.html',{'option':option})

def add_option(request,contest_id):
	if request.method == 'GET':
		#create the form for submission
		contest = get_object_or_404(Contests,pk=contest_id)
		return render_to_response('add_option.html',{'contest':contest}, context_instance=RequestContext(request))
	elif request.method == 'POST':
		#submit the data
		rp = request.POST
		contest    = get_object_or_404(Contests,pk=contest_id)
		new_option = Options(contest=contest,proposer=rp['proposer'],description=rp['description'],title=rp['title'])
		new_option.save()
		return HttpResponseRedirect(reverse('votes.views.list_options', args=(contest.title,)))
