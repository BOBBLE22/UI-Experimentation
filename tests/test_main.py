"""
Test the site.
Author: Alexander Bieniek
Source/Inspiration: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest
from requests import get

from src.main import DATA_URL, DATA_FILE


class Test(TestCase):
    def test_normalcy(self):
        '''at = AppTest.from_file("https://attackmap.sonicwall.com/live-attack-map/rest/lam-summary/summary.json")
        at.run()'''

        assert DATA_URL == "https://attackmap.sonicwall.com/live-attack-map/rest/lam-summary/summary.json"

        '''assert at.title[0].value.startswith("World")
        assert not at.exception'''
