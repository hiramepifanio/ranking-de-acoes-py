# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from lib.io import io
from lib.dados import rank
from lib.dados import order
from lib.dados import alter
from lib.dados import calc
from lib.dados import filtr


def acoes_dividendos():
    titulos, dados = io.import_from_fundamentus("empresas.csv")

    dados = filtr.distinct(titulos, dados)
    #dados = filtr.invalidos(titulos, dados)
    dados = filtr.dividendos_irregulares(titulos, dados)

    dados = filtr.greater_or_equal_to("Patrim. Líq", 50e6, titulos, dados)
    dados = filtr.greater_or_equal_to("Cresc. Rec.5a", -5, titulos, dados)
    dados = filtr.greater_or_equal_to("Liq.2meses", 100e3, titulos, dados)
    dados = filtr.greater_than("P/L", 0, titulos, dados)
    dados = filtr.greater_than("ROIC", 0, titulos, dados)

    rank_pl = rank.by_item("P/L", titulos, dados)
    alter.append_column("Rk PL", rank_pl, titulos, dados)

    rank_yeld = rank.by_item_desc("Div.Yield", titulos, dados)
    alter.append_column("Rk DY", rank_yeld, titulos, dados)

    soma = calc.add_columns(["Rk PL", "Rk DY", "Rk DY", "Rk DY"], titulos, dados)
    alter.append_column("Soma", soma, titulos, dados)
    rank_jgb = rank.by_item("Soma", titulos, dados)
    alter.append_column("Rk JGB", rank_jgb, titulos, dados)

    titulos_print = ["Rk JGB", "Papel", "Cotação", "P/L", "Div.Yield", "Liq.2meses", "Soma"]
    dados_print = order.by_item_desc("Rk JGB", titulos, dados)
    io.print_dados_filtrando_itens(titulos_print, titulos, dados_print)


def acoes_jgb():
    titulos, dados = io.import_from_fundamentus("empresas.csv")

    dados = filtr.distinct(titulos, dados)
    #dados = filtr.invalidos(titulos, dados)

    dados = filtr.greater_or_equal_to("Patrim. Líq", 500e6, titulos, dados)
    dados = filtr.greater_or_equal_to("Cresc. Rec.5a", -5, titulos, dados)
    dados = filtr.greater_or_equal_to("Liq.2meses", 100e3, titulos, dados)
    dados = filtr.greater_than("P/L", 0, titulos, dados)
    dados = filtr.greater_than("ROIC", 0, titulos, dados)

    rank_pl = rank.by_item("P/L", titulos, dados)
    alter.append_column("Rk PL", rank_pl, titulos, dados)

    rank_roic = rank.by_item_desc("ROIC", titulos, dados)
    alter.append_column("Rk ROIC", rank_roic, titulos, dados)

    rank_roe = rank.by_item_desc("ROE", titulos, dados)
    alter.append_column("Rk ROE", rank_roe, titulos, dados)

    soma = calc.add_columns(["Rk PL", "Rk PL", "Rk ROIC", "Rk ROE"], titulos, dados)
    alter.append_column("Soma", soma, titulos, dados)
    rank_jgb = rank.by_item("Soma", titulos, dados)
    alter.append_column("Rk JGB", rank_jgb, titulos, dados)

    titulos_print = ["Rk JGB", "Papel", "Cotação", "P/L", "ROE", "ROIC"]
    dados_print = order.by_item_desc("Rk JGB", titulos, dados)
    io.print_dados_filtrando_itens(titulos_print, titulos, dados_print)


def fiis():
    titulos, dados = io.import_from_csv("fiis.csv")
    dados = io.tratar_numeros(dados, 2)

    # dados = filtr.distinct(titulos, dados)
    dados = filtr.filtrar_papel(titulos, dados, "filtro_fiis_dividendos_irregulares.csv")
    dados = filtr.filtrar_papel(titulos, dados, "filtro_fiis_patrimonio_decrescente.csv")
    dados = filtr.filtrar_papel(titulos, dados, "filtro_fiis_novo.csv")
    dados = filtr.filtrar_papel(titulos, dados, "filtro_fiis_outros.csv")
    dados = filtr.less_than("Dividend Yield", 30, titulos, dados)
    dados = filtr.less_than("Cotação", 200, titulos, dados)

    new_rank = rank.by_item_desc("Dividend Yield", titulos, dados)
    alter.append_column("Rk DY", new_rank, titulos, dados)

    new_rank = rank.by_item("P/VP", titulos, dados)
    alter.append_column("Rk P/VP", new_rank, titulos, dados)

    roi_col = calc.mult_columns(["Dividend Yield", "P/VP"], titulos, dados)
    alter.append_column("ROI", roi_col, titulos, dados)
    new_rank = rank.by_item_desc("ROI", titulos, dados)
    alter.append_column("Rk ROI", new_rank, titulos, dados)

    soma = calc.add_columns(["Rk DY"], titulos, dados)
    alter.append_column("Soma", soma, titulos, dados)
    rank_jgb = rank.by_item("Soma", titulos, dados)
    alter.append_column("Rk JGB", rank_jgb, titulos, dados)

    titulos_print = ["Papel", "Segmento", "Cotação", "Dividend Yield", "P/VP", "ROI", "Rk JGB"]
    dados_print = order.by_item_desc("Rk JGB", titulos, dados)
    io.print_dados_filtrando_itens(titulos_print, titulos, dados_print)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 233,336
    acoes_jgb()
