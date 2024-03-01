from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db.models import Q
from django.views import View
from django.views.generic import CreateView,UpdateView
from .models import  Habarlar, Hodimlar,Lavozimlar,Shablonlar
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import send_message


# Create your views here.
class HodimlarView(View):
    def get(self, request):
        hodim = Hodimlar.objects.all()
        return render(request, 'hodimlar.html', {'hodim':hodim})

class ShablonlarView(View):
    def get(self, request):
        shablon = Shablonlar.objects.all()
        return render(request, 'shablonlar.html', {'shablon':shablon})


class LavozimlarView(View):
    def get(self, request):
        lavozim = Lavozimlar.objects.all()
        return render(request, 'lavozimlar.html', {'lavozim':lavozim})


class HomeView( View):
    def get(self, request):
        hodimlar = Hodimlar.objects.all()
        shablonlar = Shablonlar.objects.all()
        lavozimlar = Lavozimlar.objects.all()
        context = {
            'hodimlar': hodimlar,
            'shablonlar': shablonlar,
            'lavozimlar':lavozimlar,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        lavozim_id = request.POST.get('lavozim')
        lavozim = None
        if lavozim_id:
            lavozim = Lavozimlar.objects.get(id=lavozim_id)
        hodimlar_id = request.POST.getlist('hodimlar')
        message = request.POST.get('input_message')
        shablon = request.POST.get('shablon')
        vaqt = request.POST.get('vaqt')
        result_hodimlar = Hodimlar.objects.filter(
                    Q(id__in=hodimlar_id) |
                    (Q(lavozimi=lavozim) & ~Q(id__in=hodimlar_id)))
        result_message = message + '\n' +shablon
        if vaqt:
            result_vaqt = datetime.fromisoformat(vaqt)
        else:
            result_vaqt = datetime.now()
        message_saved = Habarlar.objects.create(text=result_message,vaqt=result_vaqt)
        message_saved.hodim.set(result_hodimlar)
        message_saved.save()
        if not vaqt:
            for hodim in message_saved.hodim.all():
                send_message(hodim.telegram_id, message_saved.text)
        return redirect('/')
    

class AddHodimView(CreateView):
    template_name = "add_page.html"
    model = Hodimlar
    fields = "__all__"
    success_url = "/hodimlar"

    def form_valid(self, form):
        hodim = form.save()
        hodim.save()
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Qo'shish"
        return context


class AddLavozimView(CreateView):
    template_name = "add_page.html"
    model = Lavozimlar
    fields = "__all__"
    success_url = "/lavozimlar"

    def form_valid(self, form):
        lavozim = form.save()
        lavozim.save()
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Qo'shish"
        return context


class AddShablonView(CreateView):
    template_name = "add_page.html"
    model = Shablonlar
    fields = "__all__"
    success_url = "/shablonlar"

    def form_valid(self, form):
        shablon = form.save()
        shablon.save()
        return redirect(self.success_url)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Qo'shish"
        return context



class UpdateHodimView(UpdateView):
    template_name = "add_page.html"
    model = Hodimlar
    fields = "__all__"
    success_url = "/hodimlar"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Saqlash"
        return context


class UpdateLavozimView(UpdateView):
    template_name = "add_page.html"
    model = Lavozimlar
    fields = "__all__"
    success_url = "/lavozimlar"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Saqlash"
        return context


class UpdateShablonView(UpdateView):
    template_name = "add_page.html"
    model = Shablonlar
    fields = "__all__"
    success_url = "/shablonlar"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context["button_title"] = "Saqlash"
        return context

def delete_hodim(request, pk):
    try:
        hodimm = Hodimlar.objects.filter(pk=pk)
    except Hodimlar.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Hodim topilmadi"})
    else:
        hodimm.delete()
        return redirect('/hodimlar')


def delete_lavozim(request,pk):
    try:
        lavozim = Lavozimlar.objects.filter(pk=pk)
    except Lavozimlar.DoesNotExist:
        return JsonResponse({"status":"error"})
    else:
        lavozim.delete()   
        return redirect('/lavozimlar')


def delete_shablon(request,pk):
    try:
        shablon = Shablonlar.objects.filter(pk=pk)
    except Shablonlar.DoesNotExist:
        return JsonResponse({"status":"error"})
    else:
        shablon.delete()   
        return redirect('/shablonlar')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))  # Foydalanuvchi tizimga kirgan bo'lsa, asosiy sahifaga yo'naltirish
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))  # Kirish muvaffaqiyatli bo'lsa, asosiy sahifaga yo'naltirish
        else:
            error_message = 'Login xato'
            return render(request, 'login.html', {'error': error_message})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))