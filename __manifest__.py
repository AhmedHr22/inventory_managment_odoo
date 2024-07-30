{
    "name":"inventory_managment",
    "description":"a module to manage inventory",
    "category":"Inventory",
    "author":"Riad",
    "depends":['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/supplier.xml',
        'views/category.xml',
        'views/product_menu_item.xml',
        'data/product_data.xml',
        'data/inventory.product.csv',
        'data/supplier_data.xml',
        'data/inventory.category.csv'
    ],
    "license":"LGPL-3",
    "installable":True,
    "application":True,
    "version":'1'
}