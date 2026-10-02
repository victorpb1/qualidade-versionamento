# -*- coding: utf-8 -*-
"""Verificacao automatica das metricas, sem framework externo."""

import os
import tempfile

from metricas import analisar


EXEMPLO = """# comentario inicial
valor = 10

# outro comentario
print(valor)
"""
# O arquivo acima tem 5 linhas, sendo 2 de comentario, 2 de codigo
# e 1 em branco.


def test_contagem():
    caminho = os.path.join(tempfile.mkdtemp(), "exemplo.py")
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(EXEMPLO)

    r = analisar(caminho)

    assert r["total"] == 5, f"total esperado 5, obtido {r['total']}"
    assert r["comentarios"] == 2, \
        f"comentarios esperado 2, obtido {r['comentarios']}"
    assert r["codigo"] == 2, f"codigo esperado 2, obtido {r['codigo']}"

    print("teste de contagem: OK")


if __name__ == "__main__":
    test_contagem()
    print("todos os testes passaram")
