# README.md

Nesta aula vamos entender os dois parâmetros utilizados para copiar arquivos e diretórios para uma imagem

- COPY
  - https://docs.docker.com/engine/reference/builder/#copy
  - Copia arquivos ou diretórios do diretório local para a imagem
  - Sintaxe:
    ```
    COPY [--chown=<user>:<group>] <src>... <dest>
    COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
    ```
- ADD
  - https://docs.docker.com/engine/reference/builder/#add
  - Copia arquivos ou diretórios do diretório local e também arquivos remotos através de uma URL para a imagem
  - Sintaxe:
    ```
    ADD [--chown=<user>:<group>] [--checksum=<checksum>] <src>... <dest>
    ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
    ```

Aqui o [Dockerfile](Dockerfile) utilizado.  

Faça um build da imagem
```
docker image build -t copy-vs-add .
```
NOTA:
- Você pode utilizar o parâmetro `--no-cache` para não utilizar o cache da imagem

Valide os arquivos dentro da imagem
```
docker container run --rm -it copy-vs-add ls -lh /example
```