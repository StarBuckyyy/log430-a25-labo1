"""
User controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from daos.user_dao import UserDAO

class UserController:
    def __init__(self):
        self.dao = UserDAO()

    def list_users(self):
        """ List all users """
        return self.dao.select_all()
        
    def create_user(self, user):
        """ Create a new user based on user inputs """
        self.dao.insert(user)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
    def delete_user(self, user_id):
        """Supprime un utilisateur spécifique"""
        self.dao.delete(user_id)

    def delete_all_users(self):
        """Supprime tous les utilisateurs"""
        self.dao.delete_all()