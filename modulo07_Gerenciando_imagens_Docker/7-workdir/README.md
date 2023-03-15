# README.md

Nesta aula vamos aprender sobre o parâmetro WORKDIR.  
Ao invés de usar RUN cd é recomendado usar o WORKDIR.
Desta forma durante o build o docker vai mudar de diretório, muito útil também para definir o diretório padrão da imagem.  


- WORKDIR
  - https://docs.docker.com/engine/reference/builder/#env
  - Define o diretório de trabalho para as instruções, como por exemplo:
    - RUN, CMD, ENTRYPOINT, COPY and ADD
  - Se o diretório não existir, ele será criado
  - Sintaxe:
    - WORKDIR /path/to/workdir

Aqui o [Dockerfile](Dockerfile) utilizado.  

Faça um build da imagem
```
docker image build -t workdir .
```

Valide os arquivos dentro da imagem
```
docker container run --rm -it workdir ls -l teste
docker container run --rm -it working-with-env ./example/example.sh
```