import unittest

from CryptoWerk import CryptoWerk


class TestCryptoWerk(unittest.TestCase):

    def setUp(self):
        self.crypto_werk = CryptoWerk()
        self.retrieval_ids = []

    def test_register(self):
        data = "1111111111111111111111111111111111111111111111111111111111111111"
        response = self.crypto_werk.register(data)
        self.assertNotEqual(response, None)
        self.assertIn("documents", response)

        for obj in response["documents"]:
            self.assertIn("retrievalId", obj)
            self.retrieval_ids.append(obj["retrievalId"])

    def test_verify(self):
        for retrieval_id in self.retrieval_ids:
            response = self.crypto_werk.verify(retrieval_id)
            self.assertNotEqual(response, None)
            self.assertIn("documents", response)

            for obj in response["documents"]:
                self.assertIn("seal", obj)


if __name__ == "__main__":
    unittest.main()


