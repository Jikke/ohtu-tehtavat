import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "piimä", 7)
            if tuote_id == 3:
                return Tuote(3, "kerma", 10)

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa_mock = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)



    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_yhden_ostoksen_paatyttya_tilisiirtoa_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_kahden_eri_tuotteen_ostamisen_paatyttya_tilisiirtoa_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 12)

    def test_kahden_saman_tuotteen_ostamisen_paatyttya_tilisiirtoa_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)

    def test_toinen_ostettava_tuote_on_loppu_mutta_ostosten_paatyttya_tilisiirtoa_kutsutaan_oikealla_asiakkaalla_tilinumerolla_ja_summalla(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.lisaa_koriin(3)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 7)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.lisaa_koriin(3)
        self.kauppa_mock.tilimaksu("pekka", "12345")
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.tilimaksu("jussi", "54321")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("jussi", ANY, "54321", ANY, 5)

    def test_tilimaksu_vaatii_uuden_viitenumeron(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.lisaa_koriin(2)
        self.kauppa_mock.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia uusi on kutsuttu
        self.viitegeneraattori_mock.uusi.assert_called()


    def test_ostoskorista_poisto_toimii(self):
        
        # tehdään ostokset
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.poista_korista(1)
        saldo = self.varasto_mock.saldo(1)

        # varmistetaan, että saldo on taas 10
        self.assertEqual(saldo, 10)
