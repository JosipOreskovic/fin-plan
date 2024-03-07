from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	name = models.CharField(max_length=200)
	TYPE_CHOICE = (
		('0', 'J.D.O.O.'),
		('1', 'D.O.O.'),
		('3', 'D.D.'),
		('4', 'OBRT'),
		('5', 'NEPROFITNA ORGANIZACIJA'),
	)
	type = models.CharField(max_length=1, choices=TYPE_CHOICE)
	SIZE_CHOICE = (
		('0', 'MIKRO'),
		('1', 'MALI'),
		('3', 'SREDNJI'),
		('4', 'VELIKI'),
	)
	size = models.CharField(max_length=1, choices=SIZE_CHOICE, blank=True)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	post_number = models.CharField(max_length=10, blank=True)
	country = models.CharField(max_length=100, blank=True)
	tel = models.CharField(max_length=20, blank=True)
	mob = models.CharField(max_length=20, blank=True)
	email = models.CharField(max_length=100, blank=True)
	fax = models.CharField(max_length=20, blank=True)
	director_name = models.CharField(max_length=200, blank=True)
	director_address = models.CharField(max_length=200, blank=True)
	director_oib = models.CharField(max_length=200, blank=True)
	oib = models.CharField(max_length=11)
	vat_id = models.CharField(max_length=13, blank=True)
	reg_number = models.CharField(max_length=20, blank=True)
	stat_number = models.CharField(max_length=20, blank=True)
	hzmo_number = models.CharField(max_length=20, blank=True)
	hzzo_number = models.CharField(max_length=20, blank=True)
	PDV_CHOICE = (
		('0', 'NIJE OBVEZNIK'),
		('1', 'MJESEČNI'),
		('3', 'KVARTALNI'),
		)
	pdv = models.CharField(max_length=1, choices=PDV_CHOICE)
	number_worker = models.IntegerField(null=True, blank=True)
	price = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Task(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	due_date = models.DateField()
	RECURRING_CHOICE = (
		('0', 'NE'),
		('1', 'DA'),
	)
	RECURRING_PERIOD = (
		('0', 'GODIŠNJE'),
		('1', 'MJESEČNO'),
		('2', 'TJEDNO'),
		('3', 'DNEVNO'),
	)
	recurring = models.CharField(max_length=1, choices=RECURRING_CHOICE, blank=True)
	recurring_period = models.CharField(max_length=1, choices=RECURRING_PERIOD, blank=True)
	end_date = models.DateField(null=True, blank=True)
	description = models.TextField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Note(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		if len(self.text) > 50:
			return f"{self.text[:50]}..."
		else:
			return self.text