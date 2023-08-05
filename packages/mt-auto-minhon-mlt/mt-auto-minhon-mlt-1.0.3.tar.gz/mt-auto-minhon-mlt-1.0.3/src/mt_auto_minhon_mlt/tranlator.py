from __future__ import annotations

import json
from enum import Enum
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class TranslateType(str, Enum):
    FSA_NT = "fsaNT"
    SHORT_SNT = "shortSnt"
    VOICETRA_NT = "voicetraNT"
    PAT_ETC = "patETC"
    LAWS_NT = "lawsNT"
    GENERAL_PT = "generalPT"
    PATENT_NT = "patentNT"
    SCIENCE = "science"
    FSA_GO_JP = "fsaGoJP"
    MINNA_PE = "minnaPE"
    GENERAL_NT = "generalNT"


def load_support_translate() -> list[tuple[str, str, str]]:
    path = Path(__file__).parent / "assets/support_translate.json"
    with open(path, encoding="utf-8") as f:
        support_languages = json.load(f)
    return [tuple(support_language) for support_language in support_languages]


def send_request(url: str, data: dict[str, str], timeout=10) -> dict:
    request_object = Request(url, urlencode(data).encode("ascii"), method="POST")

    with urlopen(request_object, timeout=timeout) as response:
        response_body = response.read().decode("utf-8")
    return json.loads(response_body)


class Translator:
    __DOMAIN = "https://mt-auto-minhon-mlt.ucri.jgn-x.jp"
    __SUPPORT_TRANSLATE = load_support_translate()

    def __init__(self, client_id: str, client_secret: str, user_name: str) -> None:
        self.__client_id = client_id
        self.__user_name = user_name
        self.__access_token = self.__get_access_token(client_id, client_secret)

    @classmethod
    def __get_access_token(cls, client_id: str, client_secret: str) -> str:
        url = f"{cls.__DOMAIN}/oauth2/token.php"
        request_data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        response_data = send_request(url, request_data)
        return response_data["access_token"]

    def translate_text(
        self,
        text: str,
        source_lang: str,
        target_lang: str,
        translate_type: TranslateType = TranslateType.GENERAL_NT,
        split: int = None,
        history: int = None,
        xml: int = None,
        term_id: str | list[str] | int = None,
        bilingual_id: str | list[str] | int = None,
        log_use: int = None,
        data: str | int = None,
    ) -> str:
        """
        Translate text.

        :param: text: text to translate.
        :param: source_lang: source language.
        :param: target_lang: target language.
        :param: translate_type: translate type.
        :param: split: split text.
        :param: history: history.
        :param: xml: xml.
        :param: term_id: term id.
        :param: bilingual_id: bilingual id.
        :param: log_use: log use.
        :param: data: data.

        :return: translated text.
        """
        self.__check(text, translate_type, source_lang, target_lang)

        url = f"{self.__DOMAIN}/api/mt/{translate_type.value}_{source_lang}_{target_lang}/"
        request_data = {
            "access_token": self.__access_token,
            "key": self.__client_id,
            "name": self.__user_name,
            "type": "json",
            "text": text,
            "split": split,
            "history": history,
            "xml": xml,
            "term_id": term_id,
            "bilingual_id": bilingual_id,
            "log_use": log_use,
            "data": data,
        }
        response_data = send_request(url, request_data)

        if response_data["resultset"]["code"] != 0:
            raise ValueError(
                f"code: {response_data['resultset']['code']}, message: \"{response_data['resultset']['message']}\""
            )
        return response_data["resultset"]["result"]["text"]

    def __check(self, text: str, translate_type: TranslateType, source_lang: str, target_lang: str) -> None:
        if not self.__is_support_translate(translate_type, source_lang, target_lang):
            raise ValueError(
                f"doesn't support. translate_type: {translate_type}, source_lang: {source_lang}, "
                "target_lang: {target_lang}"
            )
        if not text:
            raise ValueError("doesn't exist text")

    @classmethod
    def __is_support_translate(cls, translate_type: TranslateType, src_lang: str, target_lang: str) -> bool:
        return (translate_type.value, src_lang, target_lang) in cls.__SUPPORT_TRANSLATE
