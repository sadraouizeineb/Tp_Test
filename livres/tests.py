from django.test import TestCase
from .models import Livre

class LivreTestCase(TestCase):
    def setUp(self):
        Livre.objects.create(titre="Django ", auteur="act2", date_publication="2012-01-01")

    def test_liste_livres(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ajouter_livre(self):
        response = self.client.post('/ajouter/', {'titre': 'Nouveau Livre', 'auteur': 'Auteur', 
                                                  'date_publication': '2024-11-01', 'disponible': True})
        self.assertEqual(Livre.objects.count(), 2)




