## Planejamento de Rota em viagem
Um grupo de amigos pretendem visitar dez cidades da América do Sul e este projeto visa encontrar a melhor rota possível por meio do algoritmo genético.

As distâncias diretas entre as cidades estão descritas abaixo, em centenas de kilômetros. Por ser uma matriz simétrica, somente a parte superior foi descrita.

|        | SP | SSA | RJ | Lima | Bog. | Sant. | Carac. | BH | PoA. | BSB |
|--------|----|-----|----|------|------|-------|--------|----|------|-----|
| SP     | -  | 17  | 3  | 35   | 43   | 26    | 44     | 5  | 8    | 9   |
| SSA    |    | -   | 20 | 31   | 47   | 11    | 51     | 22 | 8    | 23  |
| RJ     |    |     | -  | 38   | 45   | 29    | 45     | 3  | 11   | 9   |
| Lima   |    |     |    | -    | 19   | 25    | 27     | 36 | 33   | 32  |
| Bog.   |    |     |    |      | -    | 43    | 10     | 43 | 46   | 37  |
| Sant.  |    |     |    |      |      | -     | 49     | 30 | 19   | 30  |
| Carac. |    |     |    |      |      |       | -      | 42 | 48   | 35  |
| BH.    |    |     |    |      |      |       |        | -  | 13   | 6   |
| PoA.   |    |     |    |      |      |       |        |    | -    | 16  |
| BSB    |    |     |    |      |      |       |        |    |      | -   |

[Ver explicação completa](Ref/proj1-iia-1-2020.pdf).

### Problema
A rota deve iniciar e terminar em Brasília (BSB), só devendo passar uma vez por cidade, e deve ser a rota com menor distância total a ser percorrida.

### Solução
Desenvolvida em [Python 3.7.6](https://www.python.org/downloads/release/python-376/), executada através dos comandos:

```
# Ativar ambiente virtual
python src/main.py
```
