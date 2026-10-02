# -*- coding: utf-8 -*-
"""Calcula metricas basicas de um arquivo de codigo fonte."""

import sys


def analisar(caminho):
    """Devolve um dicionario com as metricas do arquivo informado."""
    with open(caminho, encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    total = len(linhas)
    comentarios = 0
    codigo = 0
    em_branco = 0

    for linha in linhas:
        texto = linha.strip()
        if not texto:
            em_branco += 1
        elif texto.startswith("#"):
            comentarios += 1
        else:
            codigo += 1

    # A densidade compara comentarios com o conteudo util do arquivo,
    # entao as linhas em branco ficam de fora do denominador.
    uteis = codigo + comentarios
    densidade = (comentarios / uteis * 100) if uteis else 0.0

    return {
        "total": total,
        "codigo": codigo,
        "comentarios": comentarios,
        "em_branco": em_branco,
        "densidade": densidade,
    }


def main():
    if len(sys.argv) < 2:
        print("uso: python metricas.py <arquivo>")
        sys.exit(1)

    resultado = analisar(sys.argv[1])

    print(f"Arquivo analisado: {sys.argv[1]}")
    print(f"Total de linhas:        {resultado['total']}")
    print(f"Linhas de codigo:       {resultado['codigo']}")
    print(f"Linhas de comentario:   {resultado['comentarios']}")
    print(f"Linhas em branco:       {resultado['em_branco']}")
    print(f"Densidade de comentario: {resultado['densidade']:.1f}%")


if __name__ == "__main__":
    main()
