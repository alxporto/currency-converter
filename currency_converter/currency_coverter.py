import re

class CurrencyConverter:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()
    
    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def validate_url(self):
        if not self.url:
            raise ValueError("The URL is empty")
        
        url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
        match = url_pattern.match(url)
        if not match:
            raise ValueError("The URL is not valid.")
        
    def get_url_base(self):
        question_index = self.url.find('?')
        url_base = self.url[:question_index]
        return url_base

    def get_url_params(self):
        question_index = self.url.find('?')
        url_params = self.url[question_index+1:]
        return url_params

    def get_value_param(self, search_param):
        index_param = self.get_url_params().find(search_param)
        index_value = index_param + len(search_param) + 1
        index_e_commercial = self.get_url_params().find('&', index_value)
        if index_e_commercial == -1:
            value = self.get_url_params()[index_value:]
        else:
            value = self.get_url_params()[index_value:index_e_commercial]
        return value
    
url = "bytebank.com/exchange?amount=10&curSource=real&curDestination=dolar"
currency_converter = CurrencyConverter(url)

DOLAR_VALUE = 4.89
source_currency = currency_converter.get_value_param("curSource") 
destination_currency = currency_converter.get_value_param("curDestination")
amount = currency_converter.get_value_param("amount") 

if source_currency == "dolar" and destination_currency == "real":
    converted_value = int(amount) * DOLAR_VALUE 
    print(f"The value of $ {amount} dollars is equivalent to R$ {str(converted_value)} reais.")
elif source_currency == "real" and destination_currency == "dolar":
    converted_value = int(amount) / DOLAR_VALUE 
    print(f"The value of R$ {amount} reais is equivalent to $ {str(converted_value)} dollars.")
else:
    print(f"Exchange from {source_currency} to {destination_currency} is not available.")