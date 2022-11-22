from django.shortcuts import render, redirect
from core_cnhs_2.forms import Registros_CNH_Form, Registros_JM_Form, Registros_CRT_Form, Registros_CEDV_Form, Inscricao_Candidatos_Form, Correcao_CNH_Form, Correcao_CRT_Form, Correcao_CEDV_Form, Correcao_JM_Form
from core_cnhs_2.models import Candidatos
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404



###################################################login|logout|submit#################################################

#Área de login do usuário para acessar as ferramentas administrativas administradtivos
def login_usuarios(request):
    return render(request, 'login.html')

#Redirecionamento ao efetuar logout
def logout_usuarios(request):
    logout(request)
    return redirect('/')

#Efetuação da autenticação do usuário
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/') 
    else:
        messages.error(request,'Usuário ou senha inválidos')
        return redirect('/')

#################################################Lista de exibição####################################################

#visualização da lista de candidatos com informações e opção de update #feito
@login_required(login_url='/login/')
def lista_candidatos_update(request):
    Lista = Candidatos.objects.all()
    paginator = Paginator(Lista, 25)
    page = request.GET.get('page')
    busca = request.GET.get('search')
    List = paginator.get_page(page) 

    if busca:
        List = Candidatos.objects.filter(cpf__icontains = busca)

    return render(request, 'lista_candidatos_update.html', {'List':List})

#visualização da lista de candidatos com informações e opção de alteração
@login_required(login_url='/login/')
def lista_candidatos_correcao(request):
    Lista = Candidatos.objects.all()
    paginator = Paginator(Lista, 25)
    page = request.GET.get('page')
    busca = request.GET.get('search')
    List = paginator.get_page(page)

    if busca:
        List = Candidatos.objects.filter(cpf__icontains = busca)

    return render(request, 'lista_candidatos_correcao.html', {'List':List})


@login_required(login_url='/login/')
def lista_candidatos(request): 
    Lista = Candidatos.objects.all().order_by('cpf')
    paginator = Paginator(Lista, 25)
    page = request.GET.get('page')
    List = paginator.get_page(page) 

    busca = request.GET.get('search')
    if busca:
        List = Candidatos.objects.filter(cpf__icontains = busca)

    return render(request, 'lista_candidatos.html', {'List':List})


##############################################Formulários de inserção/atualização de dados########################################
#Formulário de ATUALIZAÇÃO do setor jm
@login_required(login_url='/login/')
def form_atualizacao_jm(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Registros_JM_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Registros_JM_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Atualização realizada com sucesso! ✔✍😉')
            candidatos = form.save(commit=False)
            candidatos.exame_medico = form.cleaned_data['exame_medico']
            candidatos.save()
            return redirect('lista_candidatos_update')
        else:
            return render(request, 'formupdate_jm.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'formupdate_jm.html', {'form': form, 'candidatos' : candidatos})

#Formulário de ATUALIZAÇÃO do setor crt
@login_required(login_url='/login/')
def form_atualizacao_crt(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Registros_CRT_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Registros_CRT_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Atualização realizada com sucesso! ✔✍😉')
            candidatos = form.save(commit=False)
            candidatos.formacao_teorica = form.cleaned_data['formacao_teorica']
            candidatos.exame_teorico = form.cleaned_data['exame_teorico']
            candidatos.curso_direcao = form.cleaned_data['curso_direcao']
            candidatos.save()
            return redirect('lista_candidatos_update')
        else:
            return render(request, 'formupdate_crt.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'formupdate_crt.html', {'form': form, 'candidatos' : candidatos})

#Formulário de ATUALIZAÇÃO do setor cedv
@login_required(login_url='/login/')
def form_atualizacao_cedv(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Registros_CEDV_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Registros_CEDV_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Atualização realizada com sucesso! ✔✍😉')
            candidatos.exame_direcao = form.cleaned_data['exame_direcao']
            candidatos.save()
            return redirect('lista_candidatos_update')
        else:
            return render(request, 'formupdate_cedv.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'formupdate_cedv.html', {'form': form, 'candidatos' : candidatos})

#Formulário de ATUALIZAÇÃO do setor cnh
@login_required(login_url='/login/')
def form_atualizacao_cnh(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Registros_CNH_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Registros_CNH_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Atualização realizada com sucesso! ✔✍😉')
            candidatos = form.save(commit=False)
            candidatos.nome = form.cleaned_data['nome']
            candidatos.telefone = form.cleaned_data['telefone']
            candidatos.municipio = form.cleaned_data['municipio']
            candidatos.categoria_cnh = form.cleaned_data['categoria_cnh']
            candidatos.servico = form.cleaned_data['servico']
            candidatos.emissao_cnh = form.cleaned_data['emissao_cnh']

            candidatos.save()

            return redirect('lista_candidatos_update')
        else:
            return render(request, 'formupdate_cnh.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'formupdate_cnh.html', {'form': form, 'candidatos' : candidatos})


@login_required(login_url='/login/')  
def form_inscrição(request):
        form = Inscricao_Candidatos_Form(request.POST or None)
            
        if(form.is_valid()):
            messages.success(request, 'Candidato inscrito com sucesso! ✔✍😁')
            form.save()
            return redirect('lista_candidatos') 
            
        return render(request, 'formularioregistro.html', {'form': form})

##############################################Formulários de Correção de dados########################################
@login_required(login_url='/login/')
def form_correcao_jm(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Correcao_JM_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Correcao_JM_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Correção realizada com sucesso! ✔🔧😁')
            candidatos = form.save(commit=False)
            candidatos.exame_medico = form.cleaned_data['exame_medico']
            candidatos.justificativas_auditoria = form.cleaned_data ['justificativas_auditoria_jm']

            candidatos.save()

            return redirect('lista_candidatos_correcao')
            
        else:
            return render(request, 'correcao_jm.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'correcao_jm.html', {'form': form, 'candidatos' : candidatos})


@login_required(login_url='/login/')
def form_correcao_crt(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Correcao_CRT_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Correcao_CRT_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Correção realizada com sucesso! ✔🔧😁')
            candidatos = form.save(commit=False)
            candidatos.formacao_teorica = form.cleaned_data['formacao_teorica']
            candidatos.exame_teorico = form.cleaned_data['exame_teorico']
            candidatos.curso_direcao = form.cleaned_data['curso_direcao']
            candidatos.justificativas_auditoria = form.cleaned_data['justificativas_auditoria_crt']
            candidatos.save()
            return redirect('lista_candidatos_correcao')
        else:
            return render(request, 'correcao_crt.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'correcao_crt.html', {'form': form, 'candidatos' : candidatos})


@login_required(login_url='/login/')
def form_correcao_cedv(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Correcao_CEDV_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Correcao_CEDV_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Correção realizada com sucesso! ✔🔧😁')
            candidatos.exame_direcao = form.cleaned_data['exame_direcao']
            candidatos.justificativas_auditoria = form.cleaned_data['justificativas_auditoria_cedv']
            candidatos.save()
            return redirect('lista_candidatos_correcao')
        else:
            return render(request, 'correcao_cedv.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'correcao_cedv.html', {'form': form, 'candidatos' : candidatos})


@login_required(login_url='/login/')
def form_correcao_cnh(request, id):
    candidatos = get_object_or_404(Candidatos, cpf=id)
    form = Correcao_CNH_Form(instance=candidatos) 

    if(request.method == 'POST'):
        form = Correcao_CNH_Form(request.POST, instance=candidatos)
        
        if(form.is_valid()):
            messages.success(request, 'Correção realizada com sucesso! ✔🔧😁')
            candidatos = form.save(commit=False)
            candidatos.nome = form.cleaned_data['nome']
            candidatos.telefone = form.cleaned_data['telefone']
            candidatos.municipio = form.cleaned_data['municipio']
            candidatos.categoria_cnh = form.cleaned_data['categoria_cnh']
            candidatos.servico = form.cleaned_data['servico']
            candidatos.emissao_cnh = form.cleaned_data['emissao_cnh']
            candidatos.justificativas_auditoria = form.cleaned_data['justificativas_auditoria_']
            candidatos.save()
            return redirect('lista_candidatos_correcao')
        else:
            return render(request, 'correcao_cnh.html', {'form': form, 'candidatos' : candidatos})
    elif(request.method == 'GET'):
        return render(request, 'correcao_cnh.html', {'form': form, 'candidatos' : candidatos})

#################################################################################################################################
@login_required(login_url='/login/')
def home (request):
    List = Candidatos.objects.all()
    busca = request.GET.get('search')
    if busca:
        List = Candidatos.objects.filter(cpf__icontains = busca)
    return render(request, 'base.html', {'List':List})

@login_required(login_url='/login/')
def instrucoes (request):
    return render(request, 'instrucoes.html')
