import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
    


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text

class Load(models.Model):
	"""docstring for Load"""
	ROWID = models.IntegerField('Row ID')
	OrderID = models.IntegerField('Order ID')
	OrderDate = models.CharField('Order Date', max_length=30)
	OrderPri = models.CharField('Order Priority', max_length=30)
	OrderQt = models.IntegerField('Order Quantity')
	Sales = models.CharField('Sales', max_length=30)
	Disc = models.CharField('Discount', max_length=30)
	ShipMode = models.CharField('Ship Mode', max_length = 40)
	Profit = models.CharField('Profit', max_length=30)
	UnitPrice = models.CharField('Unit Price', max_length=30)
	Cost = models.CharField('Ship Cost', max_length=30)
	Name = models.CharField('Cust Name', max_length = 100)
	Province = models.CharField('Province',max_length = 100)
	Region = models.CharField('Region',max_length = 50)
	CustSeg = models.CharField('Cust Seg', max_length = 50)
	Category = models.CharField('Category',max_length = 100)
	SubCat = models.CharField('SubCat',max_length = 200)
	ProdName = models.TextField('Product Name',max_length = 1500)
	ProdCont = models.CharField('Product Container', max_length = 100)
	Margin = models.CharField('Margin', max_length=30)
	ShipDate = models.CharField('Order Date', max_length=30)