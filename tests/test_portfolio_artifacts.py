"""Smoke tests for published coursework artifacts (not full notebook execution)."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestPortfolioArtifacts(unittest.TestCase):
    def test_population_outputs(self):
        base = ROOT / "data-analysis" / "population-2020"
        expected_figures = [
            "01_dispersion_mortalidad_esperanza.png",
            "02_mapa_calor_correlaciones.png",
            "03_ranking_correlaciones.png",
        ]
        for name in expected_figures:
            path = base / "figures" / name
            self.assertTrue(path.is_file(), path)
            self.assertGreater(path.stat().st_size, 1000)

        with (base / "results" / "matriz_correlaciones_2020.csv").open(
            encoding="utf-8-sig", newline=""
        ) as file:
            rows = list(csv.DictReader(file))
        self.assertEqual(len(rows), 7)
        mortality = next(row for row in rows if row["Series"] == "Mortalidad infantil")
        self.assertAlmostEqual(float(mortality["Esperanza de vida"]), -0.9154, places=4)

        with (base / "results" / "ranking_correlaciones_2020.csv").open(
            encoding="utf-8-sig", newline=""
        ) as file:
            pairs = list(csv.DictReader(file))
        self.assertEqual(len(pairs), 21)

    def test_video_game_saved_artifacts(self):
        base = ROOT / "data-analysis" / "video-game-eda"
        self.assertEqual(len(list((base / "figures").glob("*.png"))), 11)
        self.assertEqual(len(list((base / "derived-tables").glob("*.csv"))), 11)

        with (base / "derived-tables" / "vgsales_resumen_totales.csv").open(
            encoding="utf-8-sig", newline=""
        ) as file:
            totals = {row["Indicador"]: row["Total"] for row in csv.DictReader(file)}
        self.assertEqual(totals["Registros juego-plataforma"], "16598")
        self.assertEqual(totals["Plataformas"], "31")


if __name__ == "__main__":
    unittest.main()
