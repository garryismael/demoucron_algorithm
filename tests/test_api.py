import unittest
from fastapi.testclient import TestClient
from fastapi import status

from api import app
from constants import (
    MATRICE_LENGTH_NOT_EQUAL,
    MATRICE_MAX_INVALID, MATRICE_MIN, MATRICE_MIN_INVALID,
    PATH_MAX, PATH_MIN, MATRICE, DETAIL, RESULTAT,MAX_BIG_MATRIX
)
from api.constants import (
    INVALID_MATRIX_UNITY,
    INVALID_MATRIX_VALUE
)


class ApiTestCase(unittest.TestCase):
    """
        Test Demoucron API
    """

    def setUp(self):
        self.client = TestClient(app)

    def test_chemin_max_big_matrix(self):
        response = self.client.post(PATH_MAX, json={MATRICE: MAX_BIG_MATRIX})
        self.assertEqual(response.json()[RESULTAT], [0, 1, 3, 2, 10, 11, 14, 13, 16])
        
    def test_invalid_matrice_max(self):
        response = self.client.post(
            PATH_MAX, json={MATRICE: MATRICE_MAX_INVALID})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[DETAIL], INVALID_MATRIX_VALUE)

    def test_chemin_min(self):
        response = self.client.post(PATH_MIN, json={MATRICE: MATRICE_MIN})
        self.assertEqual(response.json()[RESULTAT], [1, 2, 4, 8, 9])

    def test_invalid_matrice_min(self):
        response = self.client.post(
            PATH_MIN, json={MATRICE: MATRICE_MIN_INVALID})
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.json()[DETAIL], INVALID_MATRIX_VALUE)

    def test_invalid_len_matrice(self):
        response = self.client.post(
            PATH_MIN, json={MATRICE: MATRICE_LENGTH_NOT_EQUAL})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()[DETAIL], INVALID_MATRIX_UNITY)
