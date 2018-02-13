from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser,BaseUserManager
 
 
class UserAccountManager(BaseUserManager):
	use_in_migrations = True
 
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Email address must be provided')
		if not password:
			raise ValueError('Password must be provided')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
 
	def create_user(self, email=None, password=None, **extra_fields):
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields['is_staff'] = True
		extra_fields['is_superuser'] = True

		return self._create_user(email, password, **extra_fields)
 
 
class MyUser(AbstractBaseUser, PermissionsMixin):
 
	REQUIRED_FIELDS = []
	USERNAME_FIELD = 'email'
 
	objects = UserAccountManager()
 
	email = models.EmailField('email', unique=True, blank=False, null=False)
	full_name = models.CharField('full name', blank=True, null=True, max_length=400)
	is_staff = models.BooleanField('staff status', default=False)
	is_active = models.BooleanField('active', default=True)
 
	def get_short_name(self):
		return self.email

	def get_full_name(self):
		return self.email

	def __unicode__(self):
		return self.email


class Meat(models.Model):
	TYPE = (
		('chicken', 'chiken meat'),
		('turkey', 'turkey meat'),

	)
	meat_type = models.CharField(max_length=7, choices=TYPE, blank=True, default='', help_text='Select meat type')
	CUT = (
		('Whole', 'WOG[Whole]'),
		('Tenderloin', 'Tenderloin'),
		('Thigh', 'Thigh'),
		('Drumstick', 'Drumstick'),
		('Whole Wing', 'Whole Wing'),
		('Breast Fillet', 'Breast Fillet'),
		('Tenders', 'Tenders'),
		('Legs', 'Legs')
	) 
	cut_type = models.CharField(max_length=50, choices=CUT, blank=True, default='', help_text='Select cut type')

	weight = models.IntegerField()

	def __str__(self):
		return '%s ,%s , (%s)' % (self.meat_type, self.cut_type, self.weight)

	def get_absolute_url(self):
		return reverse('meat', args=[str(self.id)])



class Wallet(models.Model):
	id = models.AutoField(primary_key=True,)
	user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
	balance  = models.IntegerField(default=0)


	@classmethod
	def order_deposit(cls, id, amount):
		with transaction.atomic():
			account = (
				cls.objects
				.select_for_update(nowait=True)
				.get(id=id)
			)
			Wallet.balance += amount
			account.save()


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for Order")
	meat = models.ForeignKey('Meat', on_delete=models.SET_NULL, null=True)
	date_time = models.DateTimeField(auto_now_add=True, editable=False)
	status = models.CharField(max_length=30, default="Order confirmed")

	class Meta:
		ordering = ["date_time"]

	def __str__(self):
		return '%s ,%s ,%s, (%s)' % (self.id, self.meat.meat_type, self.date_time, self.status)






