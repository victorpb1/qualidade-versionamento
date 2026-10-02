# Analisador de Métricas de Código

Ferramenta simples de linha de comando que calcula métricas básicas de um
arquivo de código fonte, criada como exercício da disciplina de Qualidade de
Software.

A ideia é apoiar a avaliação de qualidade do produto, medindo características
que costumam ser usadas como indicadores iniciais, como o tamanho do arquivo e
a proporção de comentários.

## Métricas calculadas

- Total de linhas do arquivo
- Linhas de código efetivas, descontando linhas em branco e comentários
- Linhas de comentário
- Densidade de comentários, em percentual

## Como usar

```
python metricas.py <caminho do arquivo>
```

Exemplo de saída:

```
Arquivo analisado: metricas.py
Total de linhas:        56
Linhas de codigo:       40
Linhas de comentario:   3
Linhas em branco:       13
Densidade de comentario: 7.0%
```

## Testes

```
python test_metricas.py
```

O teste monta um arquivo de exemplo com quantidades conhecidas e confere o
resultado devolvido pela função de análise.
