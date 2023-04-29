# README.md

Nesta aula vamos aprender sobre os parâmetros `ENTRYPOINT` e `CMD`.

Sobre os parâmetros:  
- ENTRYPOINT
  - https://docs.docker.com/engine/reference/builder/#entrypoint
  - Executa um comando na inicialização do container, este é o principal processo do container, se o processo falhar o container vai morrer.
  - Além disso o ENTRYPOINT pode executar um script que será executado quando o container iniciar
    - Muitas aplicações precisam de algumas parametrizações antes de iniciar e é muito útil ter um script que faça essas parametrizações
    - O script de ENTRYPOINT será utilizado **durante a inicialização do container**
    - Exemplo de entrypoint para uma aplicaçao utilizando Python e DJANGO
    ```
    #!/usr/bin/env bash
    if [ ! -z ${DEPLOY_DB} ] && $DEPLOY_DB; then
        echo "Create database and loaddata"
        python manage.py makemigrations && \
        python manage.py migrate && \
        export DJANGO_SUPERUSER_PASSWORD=${DJANGO_PASS};python manage.py createsuperuser --noinput --username admin --email django@teste.com && \
        python manage.py runserver 0.0.0.0:8000        
    else
        echo "Environment not defined at $DEPLOY_DB or is False";
        echo "Do makemigrations and migrate"
        python manage.py makemigrations && \
        python manage.py migrate && \
        python manage.py runserver 0.0.0.0:8000    
    fi
    ```
    Os comandos do ENTRYPOINT não podem ser substituidos ou ignorados mesmo que você execute o container com argumento de linha de comando.
  - Sintaxe:
    ```
    ENTRYPOINT ["executable", "param1", "param2"]
    ENTRYPOINT command param1 param2
    ```
- CMD
  - https://docs.docker.com/engine/reference/builder/#cmd
  - Executa um comando na inicialização do container, se não existir o `ENTRYPOINT`
  - Quando tem o `ENTRYPOINT` o `CMD` não pode mais chamar qualquer comando e ele só passa parâmetros para o `ENTRYPOINT`.
  - Sintaxe:
    ```
    CMD ["executable","param1","param2"] - (exec form, this is the preferred form)
    CMD ["param1","param2"] - (as default parameters to ENTRYPOINT)
    CMD command param1 param2 - (shell form)
    ```

# Trabalhando com ENTRYPOINT

Um exemplo simples do ENTRYPOINT: [1_Dockerfile_entrypoint](1_Dockerfile_entrypoint).

Faça o build da imagem

```
docker image build -t simple-entrypoint -f 1_Dockerfile_entrypoint .
```

Crie o container

```
docker container run -P -d simple-entrypoint
```

Liste os containers
```
docker container ls -a
```

Acesso o navegador com a porta definida.

# Trabalhando com CMD

Um exemplo simples do CMD: [2_Dockerfile_cmd](2_Dockerfile_cmd).

Faça o build da imagem

```
docker image build -t simple-cmd -f 2_Dockerfile_cmd .
```

Crie o container

```
docker container run -P -d -e COLOR=red simple-cmd
```

Liste os containers
```
docker container ls -a
```

Acesso o navegador com a porta definida.

# Trabalhando com ENTRYPOINT e CMD juntos

Um exemplo simples do ENTRYPOINT e CMD: [3_Dockerfile_entrypoint_and_cmd](3_Dockerfile_entrypoint_and_cmd).

Faça o build da imagem

```
docker image build -t entrypoint-and-cmd -f 3_Dockerfile_entrypoint_and_cmd .
```

Crie o container

```
docker container run -P -d -e COLOR=blue entrypoint-and-cmd
```

Liste os containers
```
docker container ls -a
```

Acesso o navegador com a porta definida.

# Trabalhando com ENTRYPOINT em modo avançado

Um exemplo do ENTRYPOINT em modo avançado: [4_Dockerfile_entrypoint_advanced](4_Dockerfile_entrypoint_advanced).

Faça o build da imagem

```
docker image build -t entrypoint-advanced -f 4_Dockerfile_entrypoint_advanced .
```

Crie o container em modo dev (local)

```
docker container run -P -d -e COLOR=gray -e DEPLOY_PROD=false entrypoint-advanced
```

Liste os containers
```
docker container ls -a
```

Veja os logs

```
docker container logs -f ID
```

NOTA:
- Veja que executou o comando definido no entrypoint para o modo de desenvolvimento utilizando o `flask run`

Crie o container em modo prod

```
docker container run -P -d -e COLOR=yellow -e DEPLOY_PROD=true entrypoint-advanced
```

Liste os containers
```
docker container ls -a
```

Veja os logs

```
docker container logs -f ID
```

NOTA:
- Veja que executou o comando definido no entrypoint para o modo de produção utilizando o `gunicorn`

Acesso o navegador com a porta definida.