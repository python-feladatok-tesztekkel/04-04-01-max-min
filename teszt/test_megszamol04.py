from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import maxmin

class TestOsszeg(TestCase):
    def test_feladat04(self):
        aktualis = maxmin.feladat04()
        elvart = -2
        self.assertEqual(elvart, aktualis, "A negatív számok közül a legnagybbat nem jól határozta meg!")
