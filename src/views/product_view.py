from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste des produits\n2. Ajouter un produit\n3. Supprimer un produit\n4. Supprimer tous les produits\n5. Quitter le menu produits")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.get_all_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                controller.add_product(name, brand, price)                
            elif choice == '3':
                product_id = input("Entrez l'ID du produit à supprimer : ").strip()
                controller.delete_product(int(product_id))
                print(f"Produit {product_id} supprimé.")
            elif choice == '4':
                confirm = input("Voulez-vous vraiment supprimer tous les produits ? (o/N) : ").strip().lower()
                if confirm == 'o':
                    controller.delete_all_products()
                    print("Tous les produits ont été supprimés.")
                else:
                    print("Suppression annulée.")
            elif choice == '5':
                print("Fermeture du menu produits.")
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        print("\n".join(f"{p.id}: {p.name} ({p.brand}) - {p.price}€" for p in products))

    @staticmethod
    def get_inputs():
        name = input("Nom du produit : ").strip()
        brand = input("Marque : ").strip()
        price = float(input("Prix : ").strip())
        return name, brand, price
