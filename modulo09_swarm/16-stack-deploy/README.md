# README.md

- Quando trabalhamos com Docker swarm, podemos criar uma stack de serviços utilizando o compose file;
- A definição do arquivo é praticamente igual as definições que vimos no módulo sobre Docker Compose;
- Pequenas mudanças ocorrem com relação a alguns parâmetros

## Sintaxe
```
docker stack deploy [OPTIONS] STACK
```

- Criando uma stack de serviços
```
docker stack deploy -c docker-compose.yaml of_docker
```

NOTA: O nome da stack não aceita hífen (-)

- Listando stack
```
docker stack ls
```

- Listando serviços da stack
```
docker stack services of_docker
```

- Listando serviços
```
docker service ls
```

- Listando detalhes do serviço
```
docker service ps of_docker_color1
```