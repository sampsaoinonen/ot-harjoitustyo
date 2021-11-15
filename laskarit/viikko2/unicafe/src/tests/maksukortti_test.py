import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.3")
    
    def test_vahentaa_saldoa_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(8)
        self.assertEqual(str(self.maksukortti), "saldo: 0.02")
    
    def test_ei_vahenna_saldoa_kun_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_True_kun_rahaa_tarpeeksi(self):        
        self.assertEqual(self.maksukortti.ota_rahaa(8), True)

    def test_ota_rahaa_True_kun_rahaa_ei_ole_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)
    
