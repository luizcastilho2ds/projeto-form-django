from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ClienteForm


def inserir_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente inserido com sucesso!')
            return redirect('inserir_cliente')
    else:
        form = ClienteForm()

    return render(request, 'inserir_cliente.html', {'form': form})
