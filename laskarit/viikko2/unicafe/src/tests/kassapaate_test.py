import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_on_alussa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyja_edullisia_lounaita_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyja_maukkaita_lounaita_alussa_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_lounas_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 500-240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_maukas_lounas_kun_maksu_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 500-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edullinen_lounas_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_maukas_lounas_kun_maksu_ei_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_lounas_kun_maksu_riittava(self):
        onnistuiko_osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)                
        self.assertEqual(onnistuiko_osto, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_maukas_lounas_kun_maksu_riittava(self):
        onnistuiko_osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)                
        self.assertEqual(onnistuiko_osto, True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiosto_edullinen_lounas_kun_maksu_ei_riittava(self):
        self.maksukortti.saldo = 100
        onnistuiko_osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)                
        self.assertEqual(onnistuiko_osto, False)
        self.assertEqual(self.maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_maukas_lounas_kun_maksu_ei_riittava(self):
        self.maksukortti.saldo = 300
        onnistuiko_osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)                
        self.assertEqual(onnistuiko_osto, False)
        self.assertEqual(self.maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_ladataan_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti.saldo, 1100)
    
    def test_ladataan_negatiivista_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)