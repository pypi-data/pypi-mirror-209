import os
from unittest import TestCase

from src.mt_auto_minhon_mlt import Translator
from src.mt_auto_minhon_mlt.tranlator import TranslateType


class TestTranslator(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.translator = Translator(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
            user_name=os.environ["USER_NAME"],
        )

    def test_translate_text(self):
        jp_text = "みんなの自動翻訳"
        en_expected = "Minna no Jido Hon'"
        en_actual = self.translator.translate_text(jp_text, source_lang="ja", target_lang="en")
        self.assertEqual(en_expected, en_actual)

        en_text = "Minna no Automatic translation"
        jp_expected = "みんなの自動翻訳"
        jp_actual = self.translator.translate_text(en_text, source_lang="en", target_lang="ja")
        self.assertEqual(jp_expected, jp_actual)

        jp_text = "みんなの自動翻訳"
        en_expected = "Minna no Jido Hon'"
        en_actual = self.translator.translate_text(
            jp_text,
            translate_type=TranslateType.GENERAL_NT,
            source_lang="ja",
            target_lang="en",
        )
        self.assertEqual(en_expected, en_actual)

    def test_translate_text_error(self):
        translator = Translator(
            client_id=os.environ["CLIENT_ID"],
            client_secret=os.environ["CLIENT_SECRET"],
            user_name="invalid user name",
        )
        jp_text = "みんなの自動翻訳"

        with self.assertRaises(ValueError) as cm:
            translator.translate_text(jp_text, source_lang="ja", target_lang="en")
        self.assertEqual('code: 501, message: ""', str(cm.exception))
