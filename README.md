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
