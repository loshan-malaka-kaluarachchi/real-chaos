import pandas

data = {
        'Material': [
            'Mild Steel',
            'Stainless Steel',
            'Aluminium',
            'Copper',
            'Brass'
        ],
        'Quantity':[
            12,
            15,
            20,
            15,
            8
        ],
        'Unit Price(USD)':[
            80,
            110,
            180,
            120,
            100
        ]
    }

df = pandas.DataFrame(data)
price = list()
quantities = data.get('Quantity')
unit_prices = data.get('Price')

for unit_price in unit_prices:
    unit_price*quantities[0]

print(df)
