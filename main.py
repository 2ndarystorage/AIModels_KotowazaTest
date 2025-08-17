"""
日本のことわざジェネレーター (CLI)

このスクリプトは、複数のLLM API (OpenAI / Anthropic Claude / Google Gemini / LMstudio) を
使用して日本のことわざを1つ取得し、CLI上に表示します。

事前準備 (.env に設定):
- OPENAI_API_KEY: OpenAI API キー
- CLAUDE_API_KEY: Anthropic Claude API キー
- GEMINI_API_KEY: Google Gemini API キー
- (任意) LMSTUDIO_BASE_URL: LMstudio のベースURL (例: http://localhost:1234/v1)
- (任意) LMSTUDIO_API_KEY: LMstudio 用のAPIキー (デフォルト: "lmstudio")
- (任意) LMSTUDIO_MODEL: 使用するローカルモデル名 (例: "llama3")

実行方法:
- `python main.py` を実行し、メニューから使用するAPIを選択します。
"""
import os
import openai
from openai import OpenAI
import google.generativeai as genai
import anthropic
from dotenv import load_dotenv

load_dotenv()

def get_proverb_openai() -> str:
    """
    OpenAI の Chat Completions API を使用して日本のことわざを取得します。

    環境変数:
        - OPENAI_API_KEY: OpenAI の API キー。

    戻り値:
        str: 取得したことわざとその簡潔な説明。
             エラー時は、原因を含むエラーメッセージの文字列を返します。

    備考:
        - 利用モデル: "gpt-3.5-turbo" (環境や契約に応じて変更可能)
        - 最大トークン数は簡潔な応答を想定して 150 に設定しています。
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return "エラー: OPENAI_API_KEYが設定されていません。.envファイルにAPIキーを設定してください。"
    
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは日本のことわざの専門家です。"},
                {"role": "user", "content": "日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"}
            ],
            max_tokens=150
        )
        
        proverb = response.choices[0].message.content
        return proverb
    
    except Exception as e:
        return f"エラー: OpenAI APIリクエスト中に問題が発生しました: {str(e)}"

def get_proverb_claude() -> str:
    """
    Anthropic Claude API を使用して日本のことわざを取得します。

    環境変数:
        - CLAUDE_API_KEY: Anthropic Claude の API キー。

    戻り値:
        str: 取得したことわざとその簡潔な説明。
             エラー時は、原因を含むエラーメッセージの文字列を返します。

    備考:
        - 利用モデル: "claude-3-haiku-20240307" (用途に応じて変更可能)
        - 最大トークン数は簡潔な応答を想定して 150 に設定しています。
    """
    api_key = os.environ.get("CLAUDE_API_KEY")
    
    if not api_key:
        return "エラー: CLAUDE_API_KEYが設定されていません。.envファイルにAPIキーを設定してください。"
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=150,
            system="あなたは日本のことわざの専門家です。",
            messages=[
                {"role": "user", "content": "日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"}
            ]
        )
        
        proverb = response.content[0].text
        return proverb
    
    except Exception as e:
        return f"エラー: Claude APIリクエスト中に問題が発生しました: {str(e)}"

def get_proverb_gemini() -> str:
    """
    Google Gemini API を使用して日本のことわざを取得します。

    環境変数:
        - GEMINI_API_KEY: Google Gemini の API キー。

    戻り値:
        str: 取得したことわざとその簡潔な説明。
             エラー時は、原因を含むエラーメッセージの文字列を返します。

    備考:
        - 利用モデル: 'gemini-2.0-flash' (コメント行の 'gemini-pro' などへ変更可能)
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        return "エラー: GEMINI_API_KEYが設定されていません。.envファイルにAPIキーを設定してください。"
    
    try:
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel('gemini-2.0-flash')
        # model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            "あなたは日本のことわざの専門家です。日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"
        )
        
        proverb = response.text
        return proverb
    
    except Exception as e:
        return f"エラー: Gemini APIリクエスト中に問題が発生しました: {str(e)}"

def get_proverb_lmstudio() -> str:
    """
    LMstudio のローカルモデルを使用して日本のことわざを取得します。

    環境変数 (任意):
        - LMSTUDIO_BASE_URL: LMstudio のベースURL。デフォルト: "http://localhost:1234/v1"
        - LMSTUDIO_API_KEY: LMstudio 用のAPIキー。デフォルト: "lmstudio"
        - LMSTUDIO_MODEL: 使用するローカルモデル名。デフォルト: "llama3"

    戻り値:
        str: 取得したことわざとその簡潔な説明。
             エラー時は、原因と対処ヒントを含むエラーメッセージの文字列を返します。

    処理概要:
        1) /models エンドポイントでサーバーの起動可否を確認
        2) 利用可能なモデル一覧を取得して、指定モデルの存在を検証
        3) Chat Completions 形式で応答を生成
    """
    base_url = os.environ.get("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
    api_key = os.environ.get("LMSTUDIO_API_KEY", "lmstudio")
    model_name = os.environ.get("LMSTUDIO_MODEL", "llama3")
    
    try:
        import requests
        try:
            response = requests.get(f"{base_url}/models", timeout=5)
            if response.status_code != 200:
                return f"エラー: LMstudioサーバーが応答していません。ステータスコード: {response.status_code}\n\nLMstudioが起動していることを確認してください。"
        except requests.exceptions.ConnectionError:
            return "エラー: LMstudioサーバーに接続できません。\n\nLMstudioが起動していることと、以下の設定を確認してください：\n- LMstudioが起動している\n- サーバーアドレスが正しい（デフォルト: http://localhost:1234/v1）\n- モデルがロードされている"
        except requests.exceptions.Timeout:
            return "エラー: LMstudioサーバーへの接続がタイムアウトしました。\n\nLMstudioが正常に動作していることを確認してください。"
        
        client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        
        models = client.models.list()
        available_models = [model.id for model in models.data]
        
        if model_name not in available_models:
            return f"エラー: 指定されたモデル '{model_name}' が見つかりません。\n\n利用可能なモデル: {', '.join(available_models)}\n\n.envファイルでLMSTUDIO_MODEL環境変数を設定するか、LMstudioで正しいモデルをロードしてください。"
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "あなたは日本のことわざの専門家です。"},
                {"role": "user", "content": "日本のことわざをランダムに1つ教えてください。ことわざとその意味を簡潔に説明してください。"}
            ],
            temperature=0.7
        )
        
        proverb = response.choices[0].message.content
        return proverb
    
    except Exception as e:
        return f"エラー: LMstudio APIリクエスト中に問題が発生しました: {str(e)}\n\nLMstudioの設定を確認してください。"

def main() -> None:
    """
    メイン関数: 対話型メニューから利用する API を選択し、ことわざを取得して表示します。

    - '1'〜'4' または 'q' を入力して操作します。
    - 各 API 呼び出しの結果は、成功時はことわざ文、失敗時はエラーメッセージとして表示されます。
    """
    print("日本のことわざジェネレーター")
    print("-" * 30)
    
    while True:
        print("使用するAPIを選択してください:")
        print("1: OpenAI")
        print("2: Anthropic Claude")
        print("3: Google Gemini")
        print("4: LMstudio (ローカルモデル)")
        print("q: 終了")
        
        choice = input("選択 (1/2/3/4/q): ")
        
        if choice == "q":
            print("プログラムを終了します。")
            break
        
        if choice == "1":
            print("\nOpenAI APIを使用します...\n")
            proverb = get_proverb_openai()
            print(proverb)
        elif choice == "2":
            print("\nAnthropic Claude APIを使用します...\n")
            proverb = get_proverb_claude()
            print(proverb)
        elif choice == "3":
            print("\nGoogle Gemini APIを使用します...\n")
            proverb = get_proverb_gemini()
            print(proverb)
        elif choice == "4":
            print("\nLMstudio (ローカルモデル) を使用します...\n")
            proverb = get_proverb_lmstudio()
            print(proverb)
        else:
            print("\n無効な選択です。1、2、3、4、またはqを入力してください。\n")
            continue
        
        print("-" * 30)
        print("別のAPIを試しますか？ (qで終了)")
        print("-" * 30)

if __name__ == "__main__":
    main()
