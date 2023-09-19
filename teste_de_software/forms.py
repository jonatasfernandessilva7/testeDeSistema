from django import forms

class CadastroForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Italo',
            }
        )
    )
    surname = forms.CharField(
        label="Sobrenome",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Silva',
            }
        )
    )
    username = forms.CharField(
        label="Nome de Usuário",
        max_length=20,
        required=True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva',
            }
        )
    )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: fulano@gmail.com',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        min_length=5,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )

    conf_password = forms.CharField(
        label='Confirmação da Senha',
        required=True,
        min_length=5,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        )
    )#fim do conf_password

    def clean_conf_password(self):
        password = self.cleaned_data.get('password')
        conf_password = self.cleaned_data.get('conf_password')

        if not password or not conf_password or password != conf_password:
            raise forms.ValidationError("Senhas não são iguais!")

        return conf_password
    
    def verificaSeNomeEhTexto(self):
        name = self.cleaned_data.get('name')

        if type(name) != str:
            raise forms.ValidationError("nome não é válido")
        
        return name




class LoginForms(forms.Form):
    username=forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva',
            }
        )
    )
    password=forms.CharField(
        label='Senha',
        required=True,
        min_length=5,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )