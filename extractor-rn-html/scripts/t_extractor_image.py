import sys
from pathlib import Path

import extractor_image


OUTPUT_DIR = Path(__file__).resolve().parent / "tmp/20260417_181233"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_API_PATH = "/api/chat"
OLLAMA_MODEL = "qwen3-vl:8b"
OLLAMA_TIMEOUT = "180"


def run_main():
	if not OUTPUT_DIR.exists():
		raise FileNotFoundError(f"output dir not found: {OUTPUT_DIR}")
	if hasattr(sys.stdout, "reconfigure"):
		sys.stdout.reconfigure(line_buffering=True)
	if hasattr(sys.stderr, "reconfigure"):
		sys.stderr.reconfigure(line_buffering=True)
	original_argv = sys.argv[:]
	try:
		sys.argv = [
			"extractor_image.py",
			"--out-dir",
			str(OUTPUT_DIR),
			"--ollama-base-url",
			OLLAMA_BASE_URL,
			"--ollama-api-path",
			OLLAMA_API_PATH,
			"--ollama-model",
			OLLAMA_MODEL,
			"--ollama-timeout",
			OLLAMA_TIMEOUT,
		]
		print("start analyse_x11.main()", flush=True)
		print(f"out_dir={OUTPUT_DIR}", flush=True)
		print(f"argv={sys.argv}", flush=True)
		exit_code = extractor_image.main()
		print(f"analyse_x11.main() finished, exit_code={exit_code}", flush=True)
		return exit_code
	finally:
		sys.argv = original_argv


if __name__ == "__main__":
	raise SystemExit(run_main())
