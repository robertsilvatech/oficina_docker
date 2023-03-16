# README.md

Nesta aula vamos aprender sobre o parâmetro EXPOSE

Sobre os parâmetros:  
- EXPOSE
  - https://docs.docker.com/engine/reference/builder/#expose
  - Informa o Docker que o container está escutando em uma porta de rede durante a execução.
  - Podemos define se o protocolo utilizado será TCP ou UDP, por padrão é TCP
  - O Expose não publica a porta no container, é um parâmetro que apenas documenta qual as portas estão sendo utilizadas pelo container.
  - Ao criar o container temos duas opções de publicar a porta
    - -p -> definimos manualmente qual porta queremos publicar
    - -P -> publica todas as portas que estão "expostas" no container, é nesse caso que entra o parâmetro EXPOSE
  - Sintaxe:
    - EXPOSE <port> [<port>/<protocol>...]

Aqui o [Dockerfile](Dockerfile) utilizado.  

Faça um build da imagem
```
docker image build -t expose .
```

Cria o container
```
docker container run -d -P expose flask
```

Liste os containers
```
docker container ls -a
```

> Observe que não temos container em execução, porque na imagem não temos um comando para inicializar o container.  
> Veremos sobre ENTRPOINT e CMD na próxima aula.  

Crie o container passando um comando
```
docker container run -d --name oficinadocker -P expose flask --app oficinadocker run --host 0.0.0.0 --debug
```

Liste os containers
```
docker container ls -a
```

Acesse via browser com a porta informada