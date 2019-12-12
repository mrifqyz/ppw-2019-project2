from django.shortcuts import redirect, render
from .models import Bantuan

# Create your views here.
def index(request):
    return render(request, 'home.html')

def bantuan(request):
    list_bantuan = Bantuan.objects.order_by('-waktu')
    context = {'list_bantuan' : list_bantuan}
    return render(request, 'bantuan.html', context)

def submit(request):
    if request.method == "POST" :
        pertanyaan = request.POST['pertanyaan']
        jawaban = request.POST['jawaban']
        nama = request.POST['nama']

        bantuan_baru = Bantuan(pertanyaan = pertanyaan,
                               jawaban = jawaban,
                               nama = nama)

        bantuan_baru.save()

        return redirect('bantuan')