import utils

#utils.extract_and_print_tables()

response = utils.api_get_data("https://brasilapi.com.br/api/cvm/corretoras/v1")
print(response)