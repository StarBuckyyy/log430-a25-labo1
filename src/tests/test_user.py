import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from daos.user_dao import UserDAO
#from daos.user_dao_mongo import UserDAOMongo as UserDAO
from models.user import User

dao = UserDAO()
dao.delete_all() # pour s'assurer que la collection est vide avant les tests


def test_user_select():
    user_list = dao.select_all()
    assert len(user_list) >= 0

def test_user_insert():
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    assigned_id = dao.insert(user)
    user.id = assigned_id
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

def test_user_update():
    user = User(None, 'Charles Babbage', 'babage@example.com')
    assigned_id = dao.insert(user)
    user.id = assigned_id

    corrected_email = 'babbage@example.com'
    user.email = corrected_email

    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails

def test_user_delete():
    user = User(None, 'Douglas Engelbart', 'engelbart@example.com')
    assigned_id = dao.insert(user)
    user.id = assigned_id
    dao.delete(user.id)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails

def test_user_delete_all():
    """ Vérifie la suppression de tous les utilisateurs """
    # Ajouter plusieurs utilisateurs
    users = [
        User(None, 'User1', 'user1@example.com'),
        User(None, 'User2', 'user2@example.com'),
        User(None, 'User3', 'user3@example.com'),
    ]
    for user in users:
        user.id = dao.insert(user)

    # Vérifie qu’ils ont été insérés
    user_list = dao.select_all()
    assert len(user_list) >= 3

    # Supprime tous les utilisateurs
    dao.delete_all()
    user_list = dao.select_all()
    assert len(user_list) == 0