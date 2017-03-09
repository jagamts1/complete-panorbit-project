from .models import PanorbitUser

class PanorbitUserAuth(object):
	def authenticate(self,email=None,password=None):
		try:
			user=PanorbitUser.objects.get(email=email)
			return user
		except PanorbitUser.DoesNotExist:
			return None

	def get_user(self,user_id):
		try:
			user=PanorbitUser.objects.get(pk=user_id)
			return user
		except PanorbitUser.DoesNotExist:
			return None