import sys
from datetime import datetime
from pathlib import Path

import analyse
import extractor_image
from extractor_html_x11 import main as extractor_html_main

PAGE_URL = '''

https://www.xiaohongshu.com/explore/69e197510000000021038519?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYPtGd_qAcFf4cop_CZR-Kwg=&xsec_source=pc_search&source=web_search_result_notes
https://www.xiaohongshu.com/explore/69e1966e000000001d01b74b?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYHVv5yID7pQ2hEespsKv1Tw=&xsec_source=pc_search&source=web_search_result_notes
https://www.xiaohongshu.com/explore/69e1949f000000001a035824?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYJLU3mYdxAu4ziE2n96I81g=&xsec_source=pc_search&source=web_search_result_notes
https://www.xiaohongshu.com/explore/69e192e30000000021011e78?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYB6gQ5fmWI_ixPRlkb_Kypw=&xsec_source=pc_search&source=web_search_result_notes
https://www.xiaohongshu.com/explore/69e19664000000002301fba5?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYFO_AEcH6NydkpjHZ0ozMoI=&xsec_source=pc_search&source=web_search_result_notes
https://www.xiaohongshu.com/explore/69e1949f000000001a035824?xsec_token=ABmtBcvOlQCpZCR-WEMP1WYJLU3mYdxAu4ziE2n96I81g=&xsec_source=pc_search&source=web_note_detail_r10
https://www.xiaohongshu.com/discovery/item/69e195a2000000001a0260bd?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBLKVb5iYXspTciocNfXFmcSzoJkjB_2Jte42QwJAPaVw%3D&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777369967&share_id=c4b61025a01d4313a1e04ee35b93b6bb&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink
https://www.xiaohongshu.com/discovery/item/69e195a2000000001a0260bd?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBLKVb5iYXspTciocNfXFmcSzoJkjB_2Jte42QwJAPaVw%3D&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777369967&share_id=c4b61025a01d4313a1e04ee35b93b6bb&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink
https://www.xiaohongshu.com/discovery/item/69aa71f4000000001a034144?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBqsboO7wcm5MrZEApJa2brrIvMDnSjqJH7Efzl9u-CoA%3D&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777368960&share_id=a0f55a82dbc0439f96d07fd1fe61c016&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink
https://www.xiaohongshu.com/explore/69df7895000000002202abf9?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBIPHv0DQXfub5C8CoG-_GHXNjkc51GdwSb19309NXB4A=&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777370188&share_id=ce9c0baefb664101ace725a313470e64&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink
https://www.xiaohongshu.com/discovery/item/69e198ad0000000023005627?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBLKVb5iYXspTciocNfXFmcTfcb3oni4gA7WeyWP83MvU%3D&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777369613&share_id=c0326fea275844e982acf14e27acccf2&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink
https://www.xiaohongshu.com/discovery/item/69e195a9000000001b020985?app_platform=android&ignoreEngage=true&app_version=9.27.0&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBLKVb5iYXspTciocNfXFmcZLQrClwUl9eKL5c3enaxJ0%3D&author_share=1&shareRedId=N0lDMDY7PE82NzUyOTgwNjczOTo4SEpM&apptime=1777369237&share_id=ec740a40f57441a099159d54355e8672&share_channel=copy_link&appuid=5ca0368f0000000010034cdc&xhsshare=CopyLink

'''

time_stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
OUTPUT_DIR = Path(__file__).resolve().parent / f"tmp/{time_stamp}"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_API_PATH = "/api/chat"
HTML_OLLAMA_MODEL = "gemma4:26b"
HTML_OLLAMA_TIMEOUT = "600"
IMAGE_OLLAMA_MODEL = "qwen3-vl:8b"
IMAGE_OLLAMA_TIMEOUT = "180"
ANALYSE_OLLAMA_MODEL = "qwen3.6:27b"
ANALYSE_OLLAMA_TIMEOUT = "2400"
ANALYSE_CHUNK_SIZE = "32000"
ANALYSE_MAX_PREDICT = "9000"


def run_main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True)
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(line_buffering=True)
    original_argv = sys.argv[:]
    try:
        sys.argv = [
            "extractor_html_x11.py",
            PAGE_URL,
            "--out-dir",
            str(OUTPUT_DIR),
            "--ollama-base-url",
            OLLAMA_BASE_URL,
            "--ollama-api-path",
            OLLAMA_API_PATH,
            "--ollama-model",
            HTML_OLLAMA_MODEL,
            "--ollama-timeout",
            HTML_OLLAMA_TIMEOUT,
        ]
        print("start extractor_html_x11.main()", flush=True)
        print(f"page_url={PAGE_URL}", flush=True)
        print(f"out_dir={OUTPUT_DIR}", flush=True)
        print(f"argv={sys.argv}", flush=True)
        extractor_exit_code = extractor_html_main()
        print(f"extractor_html_x11.main() finished, exit_code={extractor_exit_code}", flush=True)
        if extractor_exit_code != 0:
            return extractor_exit_code
        if not OUTPUT_DIR.exists() or not any(OUTPUT_DIR.glob("item_*/manifest.json")):
            print("no manifest found, stop before image analysis", flush=True)
            print("if a fresh Xephyr login window was opened, finish login and rerun this script", flush=True)
            return extractor_exit_code

        sys.argv = [
            "extractor_image.py",
            "--out-dir",
            str(OUTPUT_DIR),
            "--ollama-base-url",
            OLLAMA_BASE_URL,
            "--ollama-api-path",
            OLLAMA_API_PATH,
            "--ollama-model",
            IMAGE_OLLAMA_MODEL,
            "--ollama-timeout",
            IMAGE_OLLAMA_TIMEOUT,
        ]
        print("start extractor_image.main()", flush=True)
        print(f"out_dir={OUTPUT_DIR}", flush=True)
        print(f"argv={sys.argv}", flush=True)
        image_exit_code = extractor_image.main()
        print(f"extractor_image.main() finished, exit_code={image_exit_code}", flush=True)
        if image_exit_code != 0:
            return image_exit_code

        sys.argv = [
            "analyse.py",
            "--out-dir",
            str(OUTPUT_DIR),
            "--ollama-base-url",
            OLLAMA_BASE_URL,
            "--ollama-api-path",
            OLLAMA_API_PATH,
            "--ollama-model",
            ANALYSE_OLLAMA_MODEL,
            "--ollama-timeout",
            ANALYSE_OLLAMA_TIMEOUT,
            "--chunk-size",
            ANALYSE_CHUNK_SIZE,
            "--max-predict",
            ANALYSE_MAX_PREDICT,
        ]
        print("start analyse.main()", flush=True)
        print(f"out_dir={OUTPUT_DIR}", flush=True)
        print(f"argv={sys.argv}", flush=True)
        analyse_exit_code = analyse.main()
        print(f"analyse.main() finished, exit_code={analyse_exit_code}", flush=True)
        return analyse_exit_code
    finally:
        sys.argv = original_argv


if __name__ == "__main__":
    raise SystemExit(run_main())
