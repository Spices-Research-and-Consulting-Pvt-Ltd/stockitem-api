from django.db import models

# Create your models here.
class StockItem(models.Model):
	# tenant_id = models.ForeignKey(Tenant, on_delete=models.PROTECT, blank=True, null=True, related_name='tenant_item')
	unique_id = models.CharField(max_length=255, default='', blank=True, null=True)
	item_code = models.CharField(max_length=255, default='', blank=True, null=True)
	item_name = models.CharField(max_length=255)
	product_type = models.CharField(max_length=255, default="goods")
	url = models.CharField(max_length=255, default='', blank=True, null=True)
	alias = models.CharField(max_length=255, default='', blank=True, null=True)
	stock_category = models.CharField(max_length=100, blank=True, null=True)
	stock_subcategory = models.CharField(max_length=100, blank=True, null=True)
	uom = models.CharField(max_length=20, blank=True, null=True)
	valuation_method = models.CharField(max_length=255, default="FIFO")
	opening = models.FloatField(default=0, blank=True, null=True)
	available_quantity = models.FloatField(default=0, blank=True, null=True)
	total_quantity = models.FloatField(default=0, blank=True, null=True)
	cost_price = models.FloatField(default=0, blank=True, null=True)
	amount = models.FloatField(default=0, blank=True, null=True)
	selling_price = models.FloatField(default=0, blank=True, null=True)
	vat = models.CharField(max_length=100, default='0', blank=True, null=True)
	# purchase_gl = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, blank=True, null=True, related_name="item_purchase_gl")
	# sales_gl = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, blank=True, null=True, related_name="item_sales_gl")
	# purchase_return_gl = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, blank=True, null=True, related_name="item_purchase_return_gl")
	# sales_return_gl = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, blank=True, null=True, related_name="item_sales_return_gl")
	# inventory_gl = models.ForeignKey(ChartOfAccount, on_delete=models.PROTECT, blank=True, null=True, related_name="item_inventory_gl")
	is_fixed_asset = models.BooleanField(default=False)
	# serial_number = models.CharField(max_length=255, default='', blank=True, null=True)
	# batch_number = models.CharField(max_length=255, default='', blank=True, null=True)
	# manufacture_date = models.CharField(max_length=255, default='', blank=True, null=True)
	expire_date = models.CharField(max_length=255, default='', blank=True, null=True)
	entry_by = models.CharField(max_length=255, default='admin', blank=True, null=True)
	active_status = models.CharField(max_length=255, default='active')
	# narration = models.CharField(max_length=5000, default='', blank=True, null=True)

	# class Meta:
	# 	db_table = u'StockItem'
	
	def save(self, *args, **kwargs):
		if self.unique_id == '' or self.unique_id is None:
			prefix = "STK"
			count = StockItem.objects.count() + 1
			self.unique_id = f"{prefix}{count:03d}"

		super().save(*args, **kwargs)
  
	def __str__(self):
		return self.item_name