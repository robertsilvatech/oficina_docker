# README.md

Nesta aula vamos criar um Dockerfile simples para que você possa entender o conceito de camadas e cache em uma imagem.

> Somente a última camada é read-write, ou seja pode escrever e remover dados.
> As demais camadas são somente read-only, ou seja outras camadas não conseguem fazer alterações.

Vamos então:
- Criar o arquivo [Dockerfile](Dockerfile)

> O parâmetro ENV não cria uma nova camada.

**Cenário 1**

Executar a copia do arquivo e depois fazer as instalações  
- Desta forma quebra o cache, porque o arquivo é copiado sempre a tem que reinstalar.
- Mudar o conteúdo do arquivo e fazer o build de novo.

No Dockerfile
```
FROM ubuntu:22.04

ENV TESTE="Primeiro Teste"
ENV TESTE2="Teste2"

COPY arquivo1.txt /arquivo1.txt

RUN apt update 
RUN apt install net-tools -y 
```

Fazer o build 2 vezes
```
docker image build .
```

> Observe que no primeiro build não foi feito nenhum cache.  
> Repita o builda novamente e veja que agora temos cache de toda a imagem.  

Agora faça qualquer alteração no arquivo1.txt e repita o build

> Observe que perdemos todo o cache

**Cenário 2**

Executar as instalações e depois copiar os arquivos  
- Desta forma aproveitamos o cache
- Desta forma qualquer alteração nos arquivos serão copiadas sem quebrar o cache.

No Dockerfile
```
FROM ubuntu:22.04

ENV TESTE="Primeiro Teste"
ENV TESTE2="Teste2"

RUN apt update 
RUN apt install net-tools -y 

COPY arquivo1.txt /arquivo1.txt
```

Fazer o build 2 vezes
```
docker image build .
```

> Observe que no primeiro build não foi feito nenhum cache.  
> Repita o builda novamente e veja que agora temos cache de toda a imagem.  

Agora faça qualquer alteração no arquivo1.txt e repita o build

> Observe que mantemos o cache da instalação e copiamos somente os arquivos

Conclusão:
- Nesta aula temos alguns insigths sobre como organizar os parâmetros dentro do Dockerfile para fazer o build das imagens aproveitando ao máximo o cache.
- Entenda bem os parâmetros e organize seu Dockerfile.
- Este processo de organização trará muitos beneficios quando você for trabalhar com CI/CD
