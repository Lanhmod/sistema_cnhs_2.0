from django.forms import ModelForm
from core_cnhs_2.models import Candidatos


municipio_Choices = (
    ('Alvarães', 'Alvarães'),
    ('Amaturá', 'Amaturá'),
    ('Anamã', 'Anamã'),
    ('Anori', 'Anori'),
    ('Apuí', 'Apuí'),
    ('Atalaia do Norte', 'Atalaia do Norte'),
    ('Autazes','Autazes'),
    ('Barcelos', 'Barcelos'),
    ('Barreirinha', 'Barreirinha'),
    ('Benjamin Constant', 'Benjamin Constant'),
    ('Beruri', 'Beruri'),
    ('Boa Vista do Ramos', 'Boa Vista do Ramos'),
    ('Boca do Acre', 'Boca do Acre'),
    ('Borba', 'Borba'),
    ('Caapiranga', 'Caapiranga'),
    ('Canutama', 'Canutama'),
    ('Carauari', 'Carauari'),
    ('Careiro', 'Careiro'),
    ('Careiro da Várzea', 'Careiro da Várzea'),
    ('Coari', 'Coari'),
    ('Codajás', 'Codajás'),
    ('Eirunepé', 'Eirunepé'),
    ('Envira', 'Envira'),
    ('Fonte Boa', 'Fonte Boa'),
    ('Guajará', 'Guajará'),
    ('Humaitá', 'Humaitá'),
    ('Ipixuna', 'Ipixuna'),
    ('Iranduba', 'Iranduba'),
    ('Itacoatiara', 'Itacoatiara'),
    ('Itamarati', 'Itamarati'),
    ('Itapiranga', 'Itapiranga'),
    ('Japurá', 'Japurá'),
    ('Juruá', 'Juruá'),
    ('Jutaí', 'Jutaí'),
    ('Lábrea', 'Lábrea'),
    ('Manacapuru', 'Manacapuru'),
    ('Manaquiri', 'Manaquiri'),
    ('Manaus', 'Manaus'),
    ('Manicoré', 'Manicoré'),
    ('Maraã', 'Maraã'),
    ('Maués', 'Maués'),
    ('Nhamundá', 'Nhamundá'),
    ('Nova Olinda do Norte', 'Nova Olinda do Norte'),
    ('Novo Airão', 'Novo Airão'),
    ('Novo Aripuanã', 'Novo Aripuanã'),
    ('Parintins', 'Parintins'),
    ('Pauini', 'Pauini'),
    ('Presidente Figueiredo', 'Presidente Figueiredo'),
    ('Rio Preto da Eva', 'Rio Preto da Eva'),
    ('Santa Isabel do Rio Negro', 'Santa Isabel do Rio Negro'),
    ('Santo Antônio do Içá', 'Santo Antônio do Içá'),
    ('São Gabriel da Cachoeira', 'São Gabriel da Cachoeira'),
    ('São Paulo de Olivença', 'São Paulo de Olivença'),
    ('São Sebastião do Uatumã', 'São Sebastião do Uatumã'),
    ('Silves', 'Silves'),
    ('Tabatinga', 'Tabatinga'),
    ('Tapauá', 'Tapauá'),
    ('Tefé', 'Tefé'),
    ('Tonantins', 'Tonantins'),
    ('Uarini', 'Uarini'),
    ('Urucará', 'Urucará'),
    ('Urucurituba', 'Urucurituba'),
)    

categoria_choices = (
    ('A', 'A'),
    ('B', 'B'),
    ('C','C'),
    ('D', 'D'),
    ('E', 'E'),
)

servico_choice = (
    ('1A.CNH', '1A.CNH'),
    ('TROCA/ADIC', 'TROCA/ADIC'),
)

ex_medico_choice = (
    ('Apto', 'Apto'),
    ('Inapto', 'Inapto'),
    ('Apto com restrição', 'Apto com restrição'), 
    ('Reavaliação', 'Reavaliação'),
)

formacao_teorica_choice = (
    ('Não realizada', 'Não realizada'),
    ('Realizada', 'Realizada'),
    ('Em andamento', 'Em andamento'), 
)

ex_teorico_choice = (
    ('Apto', 'Apto'),
    ('Inapto', 'Inapto'),
    ('Faltoso', 'Faltoso'),
)

curso_direcao_choice = (
    ('Realizado', 'Realizado'),
    ('Em andamento', 'Em andamento'),
    ('Não realizado', 'Não realizado'),
)

ex_direcao_choice = (
    ('Apto', 'Apto'),
    ('Inapto', 'Inapto'),
    ('Faltoso', 'Faltoso'),
)

emissao_cnh_choices = (
    ('Sim', 'Sim'),
    ('Não', 'Não'), 
)
##############################################Formulários de inserção/atualização de dados########################################
#formulario de inscrição de candidatos por responsabilidade do setor cnh
class Inscricao_Candidatos_Form(ModelForm):
    class Meta:
       model = Candidatos
       exclude = ('exame_medico', 'formacao_teorica', 'exame_teorico', 'curso_direcao', 'exame_direcao', 'justificativas_auditoria_jm','justificativas_auditoria_cedv','justificativas_auditoria_crt', 'justificativas_auditoria_cnh')

#formulário de registro e atualização do cnh
class Registros_CNH_Form(ModelForm):
    class Meta:
        model = Candidatos
        exclude = ('cpf', 'exame_medico', 'formacao_teorica', 'exame_teorico', 'curso_direcao', 'exame_direcao', 'justificativas_auditoria_jm','justificativas_auditoria_cedv','justificativas_auditoria_crt', 'justificativas_auditoria_cnh')

#formulário de registro e atualização do JM
class Registros_JM_Form(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['exame_medico',]

#formulário de  registro e atualização do CRT
class Registros_CRT_Form(ModelForm):
    class Meta:
        model = Candidatos
        exclude = ('cpf', 'nome', 'telefone', 'municipio', 'categoria_cnh', 'servico', 'exame_medico', 'exame_direcao', 'emissao_cnh', 'justificativas_auditoria_jm','justificativas_auditoria_cedv','justificativas_auditoria_crt', 'justificativas_auditoria_cnh')

#formulário de registro e  atualização do CEDV
class Registros_CEDV_Form(ModelForm):
   class Meta:
        model = Candidatos
        fields = ['exame_direcao',]




##############################################Formulários de Correção de dados########################################
#formulário de correção dos dados do CNH
class Correcao_CNH_Form(ModelForm):
    class Meta:
        model = Candidatos
        exclude = ('exame_medico', 'formacao_teorica', 'exame_teorico', 'curso_direcao', 'exame_direcao', 'justificativas_auditoria_jm','justificativas_auditoria_cedv','justificativas_auditoria_crt')    

#formulário de correção dos dados do JM
class Correcao_JM_Form(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['exame_medico', 'justificativas_auditoria_jm',]

#formulário de correção dos dados do CRT
class Correcao_CRT_Form(ModelForm):
    class Meta:
        model = Candidatos
        exclude = ('cpf', 'nome', 'telefone', 'municipio', 'categoria_cnh', 'servico', 'exame_medico', 'exame_direcao', 'emissao_cnh', 'justificativas_auditoria_jm','justificativas_auditoria_cedv','justificativas_auditoria_cnh')

#formulário de correção dos dados do CEDV
class Correcao_CEDV_Form(ModelForm):
    class Meta:
        model = Candidatos
        fields = ['exame_direcao','justificativas_auditoria_cedv',]

        
        
