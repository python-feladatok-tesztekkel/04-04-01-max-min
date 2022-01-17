from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import maxmin

class TestOsszeg(TestCase):
    def test_feladat02(self):
        aktualis = maxmin.feladat02()
        elvart = -41
        self.assertEqual(elvart, aktualis, "A legkisebb számot nem jól határozta meg!")