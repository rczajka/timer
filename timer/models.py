from django.db import models


class Timer(models.Model):
	slug = models.SlugField(blank=True, unique=True, editable=False)
	change_stamp = models.IntegerField(editable=False)
	state = models.CharField(max_length=10)
	minutes = models.IntegerField()
	seconds = models.IntegerField()

	@classmethod
	def get(cls, slug):
		try:
			return cls.objects.get(slug=slug)
		except cls.DoesNotExist:
			return cls(slug=slug, change_stamp=0, state='reset', minutes=0, seconds=0)
