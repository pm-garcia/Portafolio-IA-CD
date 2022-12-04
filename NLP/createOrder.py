import json

def get_price(product1, product2):
    
    product_price = {'Alambre': 115,
                     'Costra': 30,
                     'Volcan': 22,
                     'Torta': 50,
                     'Postre': 30,
                     'Cerveza': 33, 
                     'Agua': 20 ,
                     'Refresco': 23,
                     'Sin bebida': 0}
                     
    total = product_price[product1] + product_price[product2] 
    message = str(total)
    return "El total a pagar es: $" + message
    
def lambda_handler(event, context):

    intent_name = event['interpretations'][0]['intent']['name']
    slots = event['interpretations'][0]['intent']['slots']
    product1 = slots['OrdenCliente']['value']['interpretedValue']
    product2 = slots['Bebida']['value']['interpretedValue']
    message = get_price(product1, product2)
    
    response = {
        'sessionState' : {
            'dialogAction' : {
                'type' : 'Close'
            },
            'intent' : {
                'name' : intent_name,
                'state' : 'Fulfilled'
            }
        },
          'messages': [
            {
                'contentType' : 'PlainText',
                'content' : message
            }
        ]
    }
    return response