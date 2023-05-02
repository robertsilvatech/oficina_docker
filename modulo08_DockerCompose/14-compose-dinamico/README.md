# README.md

# Comandos

Vou ensinar a tornar o compose dinâmico de duas formas:  
- Usando variavel de ambiente do shell.
- Usando um arquivo de variável de ambiente.

## Usando variavel de ambiente do shell.	

Adicionar variável no compose
Exemplo:
```
    environment:
      - COLOR=${COLOR}
```      


A sintaxe $VARIABLE e ${VARIABLE} são suportadas. Os valores padrão podem ser definidos da seguinte forma:
- ${VARIABLE:-default}: Define um valor padrão para variável se ela não estiver definida no ambiente ou estiver vazia
- ${VARIABLE-default}: Define um valor padrão para variável se ela não estiver definida no ambiente


Exportar a variável de ambiente
```
export COLOR=RED
```


Para remover a variável de ambiente
```
unset COLOR
```

Exibe as configurações
```
docker compose convert
```

Iniciar o serviço
```
docker compose up -d
```

## Usando um arquivo de variável de ambiente.

Arquivo(s):
- modulo08_DockerCompose/14-compose-dinamico/.env.dev
- modulo08_DockerCompose/14-compose-dinamico/.env.prod

Variável dev  
```
docker compose --env-file .env.dev up -d
docker compose down
```

Variável prod
```
docker compose --env-file .env.prod up -d
docker compose down
```

