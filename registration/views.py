from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import UserCreationFormsEmail
# Create your views here.


class Login(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('requests')

class SignUp(FormView):
    form_class = UserCreationFormsEmail
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    '''El redirect comprueba si está autenticado ya; 
       en este caso no aparece el form; 
       pasa directamente al success_url'''
    redirect_authenticated_user = True

    def form_valid(self, form):
        form.save()
        '''Cuando el form es valido lo guarda y 
           devuelve el mismo form rellenado para 
           seguir con la vista'''
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('signup')+'?ok'


