# Registros de Atividades

## Instalação

### Clonar o repositório

```bash
git clone https://github.com/KelsonF/registro-de-eventos-teste
cd registro-de-eventos-teste
```

### Inicialize o ambiente

Recomendamos usar o [venv](https://docs.python.org/3/library/venv.html) para criar um ambiente separado para o projeto.

```bash
python -m venv .venv
source .venv/bin/activate
```

### Instale as dependências

#### Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

#### Carregue os dados necessários para o projeto

```bash
python manage.py migrate
```

## Ambiente de Desenvolvimento

### Iniciar aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
python manage.py tailwind dev
```

A aplicação estará acessivel em http://127.0.0.1:8000/


## Credenciais do deploy
```bash
usuario: kelson
senha: Kmjp@2003
```
