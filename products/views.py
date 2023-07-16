from django.shortcuts import render
from .models import Produit
from django.shortcuts import render, get_object_or_404

def home(request):
    produits = Produit.objects.all()
    context = {'produits': produits}
    return render(request, 'produits/accueil.html',context)
def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    context = {'produit': produit}
    return render(request, 'produits/detail.html', context)
