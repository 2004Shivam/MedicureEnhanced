from django.test import SimpleTestCase

class SmokeTest(SimpleTestCase):
    def test_smoke_always_passes(self):
        # very small smoke test that doesn't touch DB
        self.assertEqual(1, 1)
