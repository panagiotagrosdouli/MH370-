import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rank_residual_cells import rank, score

def cell(**changes):
    row = {"cell_id": "synthetic-1", "lat": "-35", "lon": "93",
           "physics": "1", "drift": "1", "eof": "1",
           "pd_atsb_ga": "0.2", "pd_oi2018": "",
           "pd_oi2025_26": "", "cell_area_km2": "2",
           "evidence_gate": "AUTHORITATIVE_GIS_VALIDATED"}
    row.update(changes)
    return row

class RankingSafetyTests(unittest.TestCase):
    def test_area_weighting(self):
        result = rank([cell(cell_id="one", cell_area_km2="1"),
                       cell(cell_id="three", cell_area_km2="3")])
        self.assertEqual(result[0]["cell_id"], "three")
        self.assertAlmostEqual(result[0]["posterior_residual"], .75)
        self.assertAlmostEqual(sum(r["posterior_residual"] for r in result), 1)

    def test_missing_sonar_probability_rejected(self):
        with self.assertRaises(ValueError):
            rank([cell(pd_atsb_ga="")])

    def test_proxy_grid_rejected(self):
        with self.assertRaises(ValueError):
            rank([cell(evidence_gate="PROXY_ONLY_NO_GIS_PD")])

    def test_unknown_ocean_infinity_neutral(self):
        self.assertAlmostEqual(score(cell(pd_oi2025_26="")),
                               score(cell()))

    def test_known_nondetection_reduces_score(self):
        self.assertAlmostEqual(score(cell(pd_oi2018="0.5")),
                               score(cell()) / 2)

    def test_invalid_probabilities_rejected(self):
        for invalid in ("1.1", "-0.1", "nan", "inf", "hello"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    score(cell(pd_atsb_ga=invalid))

    def test_invalid_area_rejected(self):
        with self.assertRaises(ValueError):
            score(cell(cell_area_km2="0"))

    def test_zero_total_rejected(self):
        with self.assertRaises(ValueError):
            rank([cell(physics="0")])

if __name__ == "__main__":
    unittest.main()
