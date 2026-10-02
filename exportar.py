# -*- coding: utf-8 -*-
"""Exporta as metricas de varios arquivos para um arquivo CSV."""

import csv
import sys

from metricas import analisar


def exportar(caminhos, saida="metricas.csv"):
    """Analisa cada caminho informado e grava o resultado em CSV."""
    campos = ["arquivo", "total", "codigo", "comentarios",
              "em_branco", "densidade"]

    with open(saida, "w", newline="", encoding="utf-8") as destino:
        escritor = csv.DictWriter(destino, fieldnames=campos)
        escritor.writeheader()

        for caminho in caminhos:
            linha = analisar(caminho)
            linha["arquivo"] = caminho
            linha["densidade"] = round(linha["densidade"], 1)
            escritor.writerow(linha)

    return saida


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("uso: python exportar.py <arquivo> [arquivo ...]")
        sys.exit(1)

    destino = exportar(sys.argv[1:])
    print(f"metricas gravadas em {destino}")
