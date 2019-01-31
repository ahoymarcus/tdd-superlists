from django.shortcuts import redirect, render
#from django.http import HttpResponse

from lists.models import Item


# Create your views here.
def home_page(request):
	#return HttpResponse('<html><title>To-Dolists</title></html>')
	
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})
	
def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
	
def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
	