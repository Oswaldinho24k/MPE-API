from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User


class Home(View):
    def get(self, request):
        template_name = "sedeco/home.html"
        context = {
            "usuarios":User.objects.all()
        }
        return render(request, template_name, context)

    def post(self,request):
        token = request.POST.get('token')
        print('el token: ',token)
        user = User.objects.get(id=request.POST.get('user'))
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
