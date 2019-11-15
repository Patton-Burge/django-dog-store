from django.shortcuts import render,redirect
from app.models import DogProduct, DogTag, Purchase
from datetime import datetime
from django.contrib import messages


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
        dog_product.save()
        new_purchase = dog_product.purchase_set.create(
            dog_product=dog_product.name, purchased_at=datetime.now()
        )
        messages.success(request, f"Purchased {new_purchase.dog_product}")
        new_purchase.save()
        return render(request, "purchase_detail.html", {"purchase": new_purchase})
    else:
        dog_product.quantity == 0
        messages.success(request, f"{dog_product.name} is out of stock")
        return redirect('dog_product_detail', dog_product.id)


def purchase_detail(request, id):
    pass


def new_dog_tag(request):
    if request.method == "POST":
        new_tag = DogTag.objects.create(
            owner_name="Dixie", dog_name="REEEEE",dog_birthday="2019/11/15"
        )
        new_tag.save()
        return redirect(request, "dog_tag_list.html")
    else:
        return render(request, "new_dog_tag.html")

def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})

