#!/usr/bin/env python3
from unittest import TestCase
from eia.db.odin_db import OdinDB
from eia.utils.credentials import load_credentials

class TestGETLiveGasprices(TestCase):

    def test_get_live_gasprices(self):
        load_credentials()
        odin_db: 'OdinDB' = OdinDB()
        results_df: 'DataFrame' = odin_db.get_live_gasprices(state="Alabama")
        self.assertGreater(results_df.shape[0], 0)