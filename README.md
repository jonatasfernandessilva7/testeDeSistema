# testes-De-Sistema

### Ferramenta de teste

A ferramenta utilizada para realizar os testes no sistema é o selenium. O selenium é um framework de testes automatizado, utilizado para testes em sistemas feitos em várias linguagens, como, java, javaScript, python etc. Nesse caso em específico estamos utilizando o selenium para a linguagem python.

### O sistema

O sistema proposto para testes tem duas funções básicas, um login e um cadastro. O sistema foi desenvolvido com o framework Django, utilizando a arquitetura MVT (Model, View, Template), onde a Model é a camada de dados, a View é responsável pela lógica do sistema e a camada de Templates é responsável pelas telas da aplicação.


### Criando um ambiente virtual (venv)

Para criar o ambiente virtual e executar os testes siga os passos a seguir:

```bash
  python3 -m venv venv
```

Após o ambiente estar criado deve-se ativá-lo, para isso faça:

```bash
  source venv/bin/activate
```

Agora que já está com o venv ativado veja os requisitos para rodar os testes...

### Pré-requisitos para rodar os testes

Já com o venv ativo verifique se tem as bibliotecas abaixo:

- Ter o ***djando*** instalado
  - ```bash 
      pip install django
    ```
- Instalar a biblioteca ***selenium***
  - ```bash 
      pip install selenium
    ```
- Instalar a biblioteca ***pytest***
    - ```bash
         pip install pytest
      ```

### Executando os testes

Para executar os testes corretamente siga os passos.:

Rodando o servidor -> ```bash 
                          python3 manage.py runserver
                      ``` 

Executanto os testes -> ```bash
                             pytest
                        ```

### Autor

_Jônatas Fernandes Silva_

### Professor Orientador

_Ítalo Linhares_
