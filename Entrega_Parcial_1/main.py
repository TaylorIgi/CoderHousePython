import utils
import alarme_aula_04 as alarme

teste = utils.api_get_data()
teste2 = utils.listar_tabelas()
teste3 = alarme.alerta()

table_qty = input("Quantas tabelas serão extraídas? ")
for contador in range(1, table_qty):
    utils.api_get_data