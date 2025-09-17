import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()
dao.delete_all()  # pour s'assurer que la collection/table est vide avant les tests

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 0

def test_product_insert():
    product = Product(None, 'Laptop', 'Dell', 1200.00)
    assigned_id = dao.insert(product)
    product.id = assigned_id
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Smartphone', 'Samsung', 800.00)
    assigned_id = dao.insert(product)
    product.id = assigned_id

    corrected_price = 750.00
    product.price = corrected_price

    dao.update(product)

    product_list = dao.select_all()
    prices = [p.price for p in product_list]
    assert corrected_price in prices

def test_product_delete():
    product = Product(None, 'Tablet', 'Apple', 500.00)
    assigned_id = dao.insert(product)
    product.id = assigned_id
    dao.delete(product.id)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names

def test_product_delete_all():
    """ Vérifie la suppression de tous les produits """
    # Ajouter plusieurs produits
    products = [
        Product(None, 'Product1', 'BrandA', 100.00),
        Product(None, 'Product2', 'BrandB', 200.00),
        Product(None, 'Product3', 'BrandC', 300.00),
    ]
    for product in products:
        product.id = dao.insert(product)

    # Vérifie qu’ils ont été insérés
    product_list = dao.select_all()
    assert len(product_list) >= 3

    # Supprime tous les produits
    dao.delete_all()

    # Vérifie que la table est vide
    product_list = dao.select_all()
    assert len(product_list) == 0
