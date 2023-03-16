# README.md

Nesta aula vamos aprender sobre o conceito de VOLUMES dentro da imagem.
Para isso criamos um script simples com as seguintes caracteristicas:
- O script tem como objetivo gerar logs aleatorios de acordo com a quantidade de contagem definidas
  - A variável **COUNT_END** define a quantidade de linhas do log, por padrão é **10**
  - A variável **LOGFILE** define o nome do arquivo, por padrão no código é example.log no diretório de trabalho.
- No Dockerfile temos as seguintes definições:
  - VOLUME apontando para /data/logs
    - Será criado um data volume toda vez que o container for iniciado
  - ENV LOGFILE=/data/logs/example.log
    - Define a variável **LOGFILE** que será utilizada pelo script para definir o caminho do arquivo de log que será gerado.

Sobre os parâmetros:  
- VOLUMES
  - https://docs.docker.com/engine/reference/builder/#volume
  - Define um ponto de montagem que será criado automaticamente no container quando for iniciado
  - Sintaxe:
    - VOLUME ["/var/log/"] - JSON Array
    - VOLUME /var/log - Texto puro

Aqui o [Dockerfile](Dockerfile) utilizado.  

Faça um build da imagem
```
docker image build -t volume .
```

Cria o container
```
docker container run -d --name volume -e COUNT_END=2 volume sleep 3600
```

Valida o ponto de montagem
```
docker container exec -it volume mount |grep data/logs
```

Valida o diretório de trabalho definido pelo workdir
```
docker container exec -it volume pwd
```

Define uma variável de ambiente e executa o script
```
docker container exec -it volume python3 logging-example.py
```

Validando o log gerado
```
docker container exec -it volume tail /data/logs/example.log
```