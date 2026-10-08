"""Secret scanning gate (NFR-7; F-09..F-14). Test values are assembled at runtime so this file holds no literal secret."""

from pathlib import Path

from scripts.secret_scan import main, scan_text, scan_tree


def test_detects_the_delivered_secret_shapes() -> None:
    pw = "Wel" + "come123"
    assert scan_text("x.py", f'SHARED_DB_PASSWORD = "{pw}"')
    assert scan_text(".env", "DATABASE_URL=postgresql://app_shared:" + pw + "@localhost:5432/workshop")
    assert scan_text(".env", "AI_GATEWAY_KEY=sk-" + "workshop-hardcoded-example")
    assert scan_text(".env", "OT_VENDOR_TOKEN=replace-me-" + "but-currently-shared")
    assert scan_text("k.pem", "-----BEGIN RSA PRIVATE " + "KEY-----")


def test_allows_env_reads_placeholders_and_marked_lines() -> None:
    assert not scan_text("x.py", 'SHARED_DB_PASSWORD = os.environ.get("LEGACY_DB_PASSWORD", "")')
    assert not scan_text(".env.example", "AUTH_SECRET=")
    assert not scan_text("x.py", 'KEY = "abcdefgh1234"  # secret-scan: allow (test value)')
    assert not scan_text("x.py", "token_source = 'estimate'")


def test_working_tree_of_the_app_is_clean() -> None:
    root = Path(__file__).resolve().parents[1]
    assert scan_tree(root) == []


def test_cli_exit_codes(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("api_key = " + "abcdefghijk")
    assert main(["--root", str(tmp_path)]) == 1
    (tmp_path / "a.txt").write_text("hello")
    assert main(["--root", str(tmp_path)]) == 0
