import os
import re
import unittest

import shorten

INFILE = "urls_long.txt"
OUTFILE = "urls_short.txt"
TEST_INFILE = "test_" + INFILE
TEST_OUTFILE = "test_" + OUTFILE

# Max number of lines to test to ensure reasonable runtime
MAX_HEAD_LEN = 10

# To stay within stdlib, let's use Django's URLValidator regex
# https://github.com/django/django/blob/stable/1.6.x/django/core/validators.py#L43-L50
VALID_URL_REGEX = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ...or ipv4
    r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ...or ipv6
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


class TestShorten(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test infile, truncate at MAX_HEAD_LEN"""
        with open(INFILE) as f:
            lines = [line.strip() for line in f]
            head = lines[: min(len(lines), MAX_HEAD_LEN)]

        with open(TEST_INFILE, "w") as f:
            [f.write(url + "\n") for url in head]

        shorten.shorten_urls(TEST_INFILE, TEST_OUTFILE)

    def test_infile_and_outfile_lengths_are_equal(self):
        with open(TEST_INFILE, "r") as f:
            long = f.readlines()
        with open(TEST_OUTFILE, "r") as f:
            short = f.readlines()
        self.assertEqual(len(short), len(long))

    def test_long_urls_are_not_malformed(self):
        with open(TEST_INFILE, "r") as f:
            urls = [line.strip() for line in f]
            [self.assertTrue(VALID_URL_REGEX.match(url)) for url in urls]

    def test_short_urls_are_not_malformed(self):
        with open(TEST_OUTFILE, "r") as f:
            urls = [line.strip() for line in f]
            [self.assertTrue(VALID_URL_REGEX.match(url)) for url in urls]

    def test_shortened_url_is_shorter(self):
        with open(TEST_INFILE, "r") as f:
            long_urls = [line.strip() for line in f]
        with open(TEST_OUTFILE, "r") as f:
            short_urls = [line.strip() for line in f]

        for long, short in zip(long_urls, short_urls):
            self.assertTrue(len(long) > len(short))

    @classmethod
    def tearDownClass(cls):
        os.remove(TEST_INFILE)
        os.remove(TEST_OUTFILE)


if __name__ == "__main__":
    unittest.main()
