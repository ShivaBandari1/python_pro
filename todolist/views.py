from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todolist

def todo(request):
    all_items=todolist.objects.all()
    return render(request,'todo.html',{'all_items':all_items})
def addtodo(request):
    additem=request.POST['string']
    item=todolist(content=additem)
    item.save()
    return HttpResponseRedirect('todo')
def delete_todo(request,item_id):
    delete_item=todolist.objects.get(id=item_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo')



