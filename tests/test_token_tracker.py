import json
import shutil
import tempfile
import unittest
import sys
import os
from pathlib import Path

# Add project root to sys.path
sys.path.append(os.getcwd())

from src.interview_analysis.token_tracker import TokenTracker, TokenUsage


class TestTokenTracker(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.log_file = self.test_dir / "token_usage.jsonl"
        TokenTracker.initialize(self.log_file)

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        TokenTracker._instance = None
        TokenTracker._log_path = None

    def test_log_usage(self):
        usage = TokenUsage(input_tokens=100, output_tokens=50, total_tokens=150)
        TokenTracker.track(
            pipeline="test_pipeline",
            step="test_step",
            model="gemini-flash",
            usage=usage
        )

        self.assertTrue(self.log_file.exists())
        with open(self.log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 1)
            record = json.loads(lines[0])
            self.assertEqual(record["pipeline"], "test_pipeline")
            self.assertEqual(record["step"], "test_step")
            self.assertEqual(record["input_tokens"], 100)
            self.assertEqual(record["output_tokens"], 50)
            self.assertEqual(record["total_tokens"], 150)

if __name__ == "__main__":
    unittest.main()
