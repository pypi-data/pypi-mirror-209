![](https://raw.githubusercontent.com/MIDORIBIN/mt-auto-minhon-mlt/main/docs/assets/header.png)

# みんなの自動翻訳 Python Library

[![Python application](https://github.com/MIDORIBIN/mt-auto-minhon-mlt/actions/workflows/python-app.yml/badge.svg)](https://github.com/MIDORIBIN/mt-auto-minhon-mlt/actions/workflows/python-app.yml)
[![PyPI version](https://badge.fury.io/py/mt-auto-minhon-mlt.svg)](https://badge.fury.io/py/mt-auto-minhon-mlt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mt-auto-minhon-mlt)](https://pypi.org/project/mt-auto-minhon-mlt/)

「みんなの自動翻訳」をPythonから利用するためのライブラリです。  
「みんなの自動翻訳」は日本語から英語、英語から日本語、そして多数の他の言語の間で自動翻訳を提供しています。  
Pythonラッパーを使用することで、これらの翻訳機能をPythonプログラムから簡単に利用することができます。

## インストール

```shell
pip install mt-auto-minhon-mlt
```

## 必要条件

本ライブラリは、Python 3.7, 3.8, 3.9, 3.10でテストされています。

## 使用法

1. [みんなの自動翻訳の設定画面](https://mt-auto-minhon-mlt.ucri.jgn-x.jp/content/setting/user/edit/)から `ユーザーID` 、 `API key` 、 `API secret` を取得
2. `Translator` クラスのインスタンスを生成
3. `Translator.translate_text` に翻訳対象の文章、翻訳前の言語、翻訳後の言語を指定

`API key` 及び `API secret` は公開しないように注意してください。

```python
from mt_auto_minhon_mlt import Translator

translator = Translator(
    client_id='ab5718f...',
    client_secret='45791a9...',
    user_name='name',
)
en_actual = translator.translate_text('みんなの自動翻訳', source_lang='ja', target_lang='en')
```

## TODO

- [x] ~~CI~~
- [x] ~~linter, formatter~~
- [x] ~~PyPI~~
- [x] ~~PyPI GitHub Actions~~
- [x] ~~support other parameter~~
- [x] ~~badge~~
- [x] ~~docs~~
- [x] ~~docs header~~
- [ ] support file
- [ ] CD
- [ ] CLI

