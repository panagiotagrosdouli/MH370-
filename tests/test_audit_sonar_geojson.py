import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from audit_sonar_geojson import audit

def data():
    return {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},
      "geometry":{"type":"Polygon","coordinates":[[[92,-35],[93,-35],[93,-34],[92,-35]]]}}]}

class SonarAuditTests(unittest.TestCase):
    def run_audit(self, document=None, **options):
        args={"source_url":"https://example.org/official-dataset","dataset_id":"TEST-SYNTHETIC","stated_crs":"EPSG:4326"}
        args.update(options)
        return audit(data() if document is None else document, **args)

    def test_geometry_only_no_detection_claim(self):
        report=self.run_audit()
        self.assertIsNone(report["detection_probability"])
        self.assertIsNone(report["candidate_rank"])
        self.assertEqual(report["polygon_features"],1)

    def test_invalid_latitude_rejected(self):
        sample=data()
        sample["features"][0]["geometry"]["coordinates"][0][0]=[92,-95]
        with self.assertRaises(ValueError): self.run_audit(sample)

    def test_unclosed_polygon_rejected(self):
        sample=data()
        sample["features"][0]["geometry"]["coordinates"][0][-1]=[92,-34]
        with self.assertRaises(ValueError): self.run_audit(sample)

    def test_missing_provenance_rejected(self):
        with self.assertRaises(ValueError): self.run_audit(source_url="")

    def test_unknown_crs_rejected(self):
        with self.assertRaises(ValueError): self.run_audit(stated_crs="EPSG:3857")

    def test_line_layer_rejected(self):
        sample=data()
        sample["features"][0]["geometry"]={"type":"LineString","coordinates":[[92,-35],[93,-34]]}
        with self.assertRaises(ValueError): self.run_audit(sample)

if __name__=="__main__":
    unittest.main()
