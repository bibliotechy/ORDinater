from django.db import models

class Contests(models.Model):
	
	vote_choices = (
		('rated'      ,	'Rated Voting System'),
		('ranked'     ,	'Ranked Voting System'),
		('cumulative' ,	'Cumulative Voting System'),	
		('single'     ,	'Single Vote'))	

	title          = models.CharField(max_length=200)
	description    = models.CharField(max_length=1000)
	start_date     = models.DateTimeField('start date',blank=True,null=True)
	end_date       = models.DateTimeField('End Date', blank=True,null=True)
	vote_type      = models.CharField(max_length=10, choices=vote_choices)#selected from Choices above
	number_votes   = models.IntegerField(blank=True,null=True) #how many candidates can be voted for
	number_points  = models.IntegerField(blank=True,null=True) #how many points are available to distribute
	max_point_vote = models.IntegerField(blank=True,null=True) #max points per candidate

	def __unicode__(self):
		return self.title

class Options(models.Model): #the things which can be voted for
	title       = models.CharField(max_length=200)
	description = models.CharField(max_length=5000)
	proposer    = models.CharField(max_length=200)
	contest     = models.ForeignKey(Contests)
	
	def __unicode__(self):
		return self.title

class Votes(models.Model):
	contest     = models.ForeignKey(Contests)
	option      = models.ForeignKey(Options)
	vote_value  = models.IntegerField()
	#voter       = models. TODO record voter, decide on auth first

	def __unicode__(self):
        	return self.vote_value
