from django.db import models
from auditlog.registry import auditlog
from django.utils.timezone import now


class Candidatos (models.Model):

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

    emissao_cnh_choices = (
        ('Sim', 'Sim'),
        ('Não', 'Não'), 
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

    
    cpf = models.CharField(max_length=11, primary_key=True, blank=False, null=False, verbose_name = 'CPF do(a) Candidato(a)', help_text='Somente números*') #cnh 
    nome =  models.CharField(max_length=100,  blank=False, null=True, verbose_name = 'Nome do(a) Candidato(a)', help_text='Completo e em caixa alta, sem abreviações*') #cnh
    telefone = models.CharField(max_length=13,  blank=False, null=True, verbose_name = 'Telefone',  help_text='ex:(ddd)940028922' ) #cnh
    municipio = models.CharField(max_length=30,  blank=False, null=True, default='Campo não alterado', choices=municipio_Choices, verbose_name = 'Município') #cnh
    categoria_cnh = models.CharField(max_length=1,  blank=False, null=True, choices=categoria_choices, verbose_name = 'Categoria CNH Solici.') #cnh
    servico = models.CharField(max_length=10,  blank=False, null=True, choices=servico_choice, verbose_name ='Tipo de serviço solicitado') #cnh
    exame_medico = models.CharField(max_length=18, blank=True, choices=ex_medico_choice, verbose_name ='Situação do exame médico') #junta médica
    formacao_teorica = models.CharField(max_length=13,  blank=True, choices= formacao_teorica_choice, verbose_name ='Status da formação teórica') #crt
    exame_teorico = models.CharField(max_length=7,  blank=True, choices=ex_teorico_choice, verbose_name ='Situação exame teórico') #crt
    curso_direcao = models.CharField(max_length=13,  blank=True, choices=curso_direcao_choice, verbose_name ='Status do curso de direção') #crt
    exame_direcao = models.CharField(max_length=7,  blank=True, choices=ex_direcao_choice, verbose_name = 'Situação do exame de direção') #cedv
    emissao_cnh = models.CharField(max_length=3,  blank=True, choices=emissao_cnh_choices, verbose_name = 'CNH emitida?')
    justificativas_auditoria_jm= models.TextField(max_length=240,  default='Correção não realizada.', help_text="obs*: Limpe a caixa de texto acima e justifique o motivo da correção!", verbose_name ='Justificativa para fins de auditoria')
    justificativas_auditoria_cedv = models.TextField(max_length=240,  default='Correção não realizada.', help_text="obs*: Limpe a caixa de texto acima e justifique o motivo da correção!", verbose_name ='Justificativa para fins de auditoria') 
    justificativas_auditoria_crt = models.TextField(max_length=240,  default='Correção não realizada.', help_text="obs*: Limpe a caixa de texto acima e justifique o motivo da correção!", verbose_name ='Justificativa para fins de auditoria')
    justificativas_auditoria_cnh = models.TextField(max_length=240, default='Correção não realizada.', help_text="obs*: Limpe a caixa de texto acima e justifique o motivo da correção!", verbose_name ='Justificativa para fins de auditoria')
    data_criacao = models.DateTimeField(default=now, blank=False, null=False, editable=False, verbose_name ='Data de criação do registro')

    class Meta: 
        db_table = 'Candidatos'
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos' 
        permissions = [
            ("pode_manipular_cnh", "pode manipular cnh"),
            ("pode_manipular_jm", "pode manipular jm"),
            ("pode_manipular_crt", "pode manipular crt"),
            ("pode_manipular_cedv", "pode manipular cedv"),
        ]
        ordering = ('data_criacao',)

    def __str__(self):
        return self.cpf 
auditlog.register(Candidatos, mapping_fields={'municipio': 'Município', 'categoria_cnh': 'Categoria da cnh', 'servico':'Serviço solicitado', 'exame_medico':'Exame médico', 'formacao_teorica':'Formação teórica', 'exame_teorico':'Exame teórico', 'curso_direcao':'Curso de direção', 'exame_direcao':'Exame de direção', 'emissao_cnh':'Emissão de CNH'})

