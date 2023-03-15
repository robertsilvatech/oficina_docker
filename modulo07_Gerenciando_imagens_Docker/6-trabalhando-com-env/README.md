# README.md

Nesta aula vamos aprender sobre o parâmetro ENV e como utilizar em todo o processo de Build e execução dos containers

- ENV
  - https://docs.docker.com/engine/reference/builder/#env
  - Define uma variável de ambiente, será utilizada no build e também durante a execução do container.
  - Sintaxe:
    - ENV COLOR="BLUE"
    - ENV END_FOR=5

Aqui o [Dockerfile](Dockerfile) utilizado.  

Faça um build da imagem
```
docker image build -t working-with-env .
```

Valide os arquivos dentro da imagem
```
docker container run --rm -it working-with-env printenv |grep END_FOR
docker container run --rm -it working-with-env ./example/example.sh
```

Substituindo a variável
```
docker container run --rm -e END_FOR=10 -it working-with-env ./example/example.sh
```

> Preparamos o script para utilizar a variável END_FOR

```
#!/bin/bash

END=${END_FOR}
 
for i in $(seq $END); do echo $i; done
```