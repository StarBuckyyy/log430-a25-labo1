# LOG430 - LAB01  
Auteur : Goran VALIDZIC  

## 🚀 Lancement du projet avec Docker

1. **Construire l’image Docker**  
   
   docker-compose build

2. **Lancer les conteneurs (app + bases de données)**

docker-compose up -d

3. **Lancer les tests**

Exécuter tous les tests avec pytest :

docker exec -it log430-a25-labo1-store_manager_app-1 pytest src/tests

4. **Lancer l’application (menu utilisateurs ou produits)**

   Pour démarrer avec les utilisateurs :
   dans src/store_manager.py, assurez-vous que :

main_menu = UserView()  n'est pas commenté

Pour démarrer avec les produits :
(commenter la ligne main_menu = UserView() et décommenter la ligne main_menu = ProductView())

Puis lancer :

   docker exec -it log430-a25-labo1-store_manager_app-1 python src/store_manager.py

🗄️ Bases de données

    MySQL : utilisé pour Users et Products.

    MongoDB : utilisé uniquement pour Users (via UserDAOMongo).

👉 Pour tester Users avec MongoDB, modifier l’import dans src/tests/test_user.py :

# Pour MySQL
from daos.user_dao import UserDAO doit être décommenté

# Pour MongoDB
from daos.user_dao_mongo import UserDAOMongo as UserDAO doit être décommenté (et from daos.user_dao import UserDAO doit être commenté)


## ** CI/CD avec GitHub Actions**

Le projet utilise un runner auto-hébergé sur la VM pour l’intégration continue et le déploiement :  

- À chaque push sur `main`, le workflow `build-and-test` se déclenche automatiquement.
- Le runner construit les conteneurs Docker (app + MySQL + MongoDB) et exécute tous les tests.
- Les logs du workflow permettent de vérifier que MySQL et MongoDB sont bien initialisés et que les tests passent.

Ainsi, le CI/CD est entièrement fonctionnel et testé.
