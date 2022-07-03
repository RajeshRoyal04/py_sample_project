from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
from .models import user
def index(request):
	users_list=user.objects.all()
	context = {"user_list":users_list}
	#return render(request, 'header.html','homepage.html')
	return render(request, 'homepage.html', context=context)
	#return render(request, 'footer.html')

def edit_user(request,user_id):
	users_list = user.objects.get(user_id=user_id)
	context = {"user_list":users_list}
	return render(request, 'edit_user.html',context=context)
	

def save_usr(request):
	if request.method == 'POST':
		name = request.POST["name"]
		mobile = request.POST["mobile"]
		email = request.POST["email"]
		createdon = request.POST["createdon"]
		user_info=user(name=name,mobile=mobile,email=email,createdon=createdon)
		user_info.save()
		messages.success(request, 'Contact request submitted successfully.')
	#messages.error(request, 'Invalid form submission.')
	#messages.error(request, form.errors)
	return render(request, 'save_user.html')

def edit_usr(request,user_id):
	name = request.POST["name"]
	mobile = request.POST["mobile"]
	email = request.POST["email"]
	createdon = request.POST["createdon"]
	record = user.objects.get(user_id=user_id)
	record.name = name
	record.mobile = mobile
	record.email = email
	record.createdon = createdon
	record.save(update_fields=['name','mobile','email','createdon'])
	messages.success(request, 'Contact request submitted successfully.')
	#messages.error(request, 'Invalid form submission.')
	#messages.error(request, form.errors)
	return render(request, 'edit_user.html')

def delete_usr(request,user_id):
	users = user.objects.get(user_id=user_id)
	users.delete()
	return redirect(index)

