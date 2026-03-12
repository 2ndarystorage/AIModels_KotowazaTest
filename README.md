# ことわざジェネレーター

OpenAI、Anthropic Claude、Google Gemini、またはLMstudio（ローカルモデル）を使用して日本のことわざをランダムに生成するPythonプログラムです。

## 機能

- OpenAI、Anthropic Claude、Google Gemini、またはLMstudio（ローカルモデル）を使用して日本のことわざをランダムに生成
- 使用するAPIをユーザーが選択可能
- ことわざとその意味を表示
- 環境変数からAPIキーを読み込み（OpenAI、Claude、Gemini用）

## セットアップ

1. 必要なライブラリをインストール:
   ```
   pip install openai google-generativeai anthropic python-dotenv
   ```

2. `.env`ファイルにAPIキーを設定:
   ```
   # OpenAI API Key
   OPENAI_API_KEY=your_openai_api_key_here
   # Anthropic Claude API Key
   CLAUDE_API_KEY=your_claude_api_key_here
   # Google Gemini API Key
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. LMstudioを使用する場合:
   - LMstudioをインストールして起動
   - LMstudioの「Server」タブで「Start Server」をクリックしてAPIサーバーを起動
   - ローカルサーバーが`http://localhost:1234/v1`で実行されていることを確認
   - モデル（例：llama3）をLMstudioにロードしておく
   - `.env`ファイルにLMstudio設定を追加（オプション）:
     ```
     # LMstudio Configuration
     LMSTUDIO_BASE_URL=http://localhost:1234/v1
     LMSTUDIO_API_KEY=lmstudio
     LMSTUDIO_MODEL=llama3
     ```
   - モデル名はLMstudioにロードされているモデルの名前と一致させる必要があります

## 使用方法

```
python main.py
```

プログラム実行後、使用するAPIを選択します:
1. OpenAI
2. Anthropic Claude
3. Google Gemini
4. LMstudio（ローカルモデル）
q. 終了

## 注意事項

- `.env`ファイルはGitで追跡されないため、APIキーが公開されることはありません
- APIキーが設定されていない場合はエラーメッセージが表示されます
- 各APIの利用には、それぞれのサービスでのアカウント登録とAPIキーの取得が必要です
- LMstudioオプションを使用するには、LMstudioがローカルで実行されている必要があります

## Program Summary

- OpenAI / Anthropic Claude / Google Gemini / LMstudio のいずれかを選び、日本のことわざを1件取得して意味と共に表示するCLIツール
- APIキーは環境変数（`.env`）から読み込み、対話メニューで実行APIを選択

## How to Use

- 依存関係のインストール（READMEの「セットアップ」を参照）
- `.env` に各APIキーを設定
- 実行: `python main.py`
- 対話メニューでAPIを選択
- Not verified

## Completion Status

- Usable: 単一スクリプトで完結し、基本的なエラーハンドリングと対話メニューがある一方、テストや配布設定は未整備

## Program Summary

- CLIで実行し、OpenAI / Anthropic Claude / Google Gemini / LMstudio のいずれかから日本のことわざ1件と意味を生成・表示する
- APIキーは環境変数（`.env`）から読み込む

## How to Use

- 依存関係をインストール: `pip install openai google-generativeai anthropic python-dotenv`
- `.env` に各APIキーを設定（LMstudioは任意で `LMSTUDIO_*` を設定）
- 実行: `python main.py`
- メニューでAPIを選択
- Not verified

## Completion Status

- Usable: 主要機能は実装済みで対話フローもあるが、テスト・配布・設定検証の自動化は未整備

## Program Summary

- CLIで実行し、OpenAI / Anthropic Claude / Google Gemini / LMstudio のいずれかを選んで日本のことわざ1件と意味を生成・表示する
- `.env` のAPIキーを読み込む（LMstudioはローカルサーバーとモデルの起動が前提）

## How to Use

- 依存関係をインストール: `pip install openai google-generativeai anthropic python-dotenv`
- `.env` に `OPENAI_API_KEY` / `CLAUDE_API_KEY` / `GEMINI_API_KEY` を設定（LMstudioは任意で `LMSTUDIO_*` を設定）
- 実行: `python main.py`
- メニューでAPIを選択
- Not verified

## Completion Status

- Usable: 単一スクリプトの対話型ツールとしては完成度が高いが、自動テストや配布手順は未整備
