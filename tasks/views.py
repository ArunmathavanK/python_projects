from django.shortcuts import render , redirect

from django.http import HttpResponse

from . models import Task

from .forms import Form

def index(request):

    form=Form()
     
    tasks=Task.objects.all()

    if request.method=="POST":

        form=Form(request.POST)

        if form.is_valid():

            form.save()

        return redirect('/')

    context={'tasks':tasks,'Form':form}

    return render(request, 'tasks.html',context)


def updateTask(request, pk):

    tasks=Task.objects.get(id=pk)

    form=Form(instance=tasks)

    if request.method=="POST":

        form=Form(request.POST,instance=tasks)

        if form.is_valid():

            form.save()

            return redirect('/')
        
    context={'Form':form}

    return render(request, 'update-task.html',context)    
 
def deleteTask(request,pk):

    tasks=Task.objects.get(id=pk)

    if request.method=='POST':

        tasks.delete()

        return redirect('/')
    
    context = {'task':tasks}

    return render(request, 'delete-task.html',context)