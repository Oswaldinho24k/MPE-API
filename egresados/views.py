from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Egresado
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.

class ListView(View):
	def get(self, request):
		egresados = Egresado.objects.all();
		profiles = Profile.objects.filter(tipo='EG');

		template_name = "lista.html"
		context = {
		
		'egresados':egresados,
		'profiles':profiles
		}

		return render(request, template_name, context)

class DetailView(View):
	def get(self, request, id):
		#egresado = get_object_or_404(Egresado, id=id)
		profile = get_object_or_404(Profile, id=id)
		

		template_name = "detalle.html"
		context = {
		#'egresado':egresado,
		
		'profile':profile
		}
		
		return render(request, template_name, context)

	def post(self,request):
		token = request.POST.get('token')
		print('el token: ',token)
		user = User.objects.get(id=request.POST.get('user'))
		print(user)

		try:
			result = envia_token(token,user)
			print('listo! ',result)
		except:
			print('nel')
			return redirect('home')

def envia_token(token,user):
	from pyfcm import FCMNotification
	push_service = FCMNotification(api_key="AIzaSyAfPe7Lw9DmUHlYbHibQ5tSXIGr7KkhMVU")
	registration_id = token
	message_title = "Hola "+user.username
	message_body = "¡Felicidades, Tienes una cita registrada para una vacante!"
	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
	return result

