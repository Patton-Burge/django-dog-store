from django.shortcuts import render,redirect
from app.models import DogProduct, DogTag, Purchase
from datetime import datetime
from django.contrib import messages
from app.forms import NewDogTagForm
def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


def dog_product_detail(request, id):
    dog_product = DogProduct.objects.get(id=id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})

def purchase_dog_product(request, id):
    dog_product = DogProduct.objects.get(id=id)
    if dog_product.quantity > 0:
        dog_product.quantity -= 1
        purchased = dog_product.purchase_set.create(purchased_at=datetime.now())
        messages.success(request, f"Purchased {dog_product.name}")
        dog_product.save()
        return redirect("purchase_detail", purchased.id)
    else:
        messages.error(request, f"{dog_product.name} is out of stock")
        return redirect("dog_product_detail", dog_product.id)


def purchase_detail(request, id):
    purchase = Purchase.objects.get(id=id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def new_dog_tag(request):
    form = NewDogTagForm(request.POST)
    if form.is_valid():
        owner_name = request.POST["owner_name"]
        dog_name = request.POST["dog_name"]
        dog_birthday = request.POST["dog_birthday"]
        tag = DogTag.objects.create(
            owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday
        )
        tag.save()
        return redirect("dog_tag_list")
    else:
        return render(request, "new_dog_tag.html")

def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})

