# README.md

Nesta aula vamos criar nossa primeira imagem.
- Usar o Ubuntu como imagem base
- Instalar o Python3 e o PIP

DICA:
- Suba um container com a imagem base que você quer utilizar e teste passo a passo.
- Depois insira no Dockerfile e teste o build da imagem

```
docker container run --rm -it ubuntu:22.04 bash
```

Step-by-Step via Shell

```
apt update -y
apt install -y python3.10 python3-pip
```

Cuidados:
- Somente a última camada é read-write
- As camadas anteriores são somente read-only
- Dependendo do comando, não use uma nova camada.

Vamos ao Dockerfile

[Dockerfile](Dockerfile)

Fazendo o build da imagem

Sintaxe:
```
docker image build [OPTIONS] PATH | URL | -
```

Primeiro build

```
docker image build .
```

Onde:  
. - Significa o contexto ou seja onde o Docker vai buscar o conteúdo para a imagem

Adicionando tag na imagem

```
docker image build -t ofdocker-python3 -t ofdocker-python3:1.0 .
```

Suba um container e valide se a imagem tem o python instalado.

```
docker container run -it --rm ofdocker-python3 python3 -V
```

