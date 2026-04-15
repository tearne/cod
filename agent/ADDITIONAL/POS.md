# Python Orchestrated Script (POS)
The POS style helps Python take the place of native shell scripts for administration or or small applications. It strategically breaks some Python idioms to combine the different strengths of Python and shell scripts, such as favouring subprocess calls for shell commands while using Python control flow.

POS guidance:
- Prefer `subprocess` for shell commands; use Python for control flow. This makes commands easy to read and copy-paste elsewhere.
    - Always use `shell=True` with a plain string — this keeps commands terminal-ready and avoids the need for `FileNotFoundError` handling (the shell handles command resolution; use `returncode` or `check=True` for error detection instead).
    - Use a helper function similar to `run()` (below) instead of `subprocess.run()` directly — it prints the command before executing. Use `subprocess.run()` directly only when there is a specific reason not to echo (e.g. a command that produces high-frequency output where the prefix would be noise):
        ```python
        def run(cmd: str, **kwargs) -> subprocess.CompletedProcess:
            _console.print(f"$ {cmd}", style="cyan")
            return subprocess.run(f"set -o pipefail && {cmd}", shell=True, executable="/bin/bash", **kwargs)
        ```
    - Examples:
        - To download the latest version of the `helix` `deb` for `amd64`:
        ```py
        run(r"""curl -s https://api.github.com/repos/helix-editor/helix/releases/latest | grep -oP '"browser_download_url": "\K[^"]*amd64.deb' | xargs wget""")
        ```
        - To apt install `curl`:
        ```py
        run("""DEBIAN_FRONTEND=noninteractive apt-get install -y curl""")
        ```
    - But don't take this to an extreme and force trivial actions like loops into the shell.
- Prefer a single Python source file, unless it compromises readability.
- Make the python file executable and use a `uv` shebang:
    ```sh
    #!/usr/bin/env -S uv run --script --
    # /// script
    # requires-python = "==3.12.*"
    # ///
    ```
- Scripts should carry a version constant and expose it via `--version` using `argparse`:
    ```py
    VERSION = "1.0.0"
    ```
    ```py
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    ```
- Key functions go at the top of the file; utility functions at the bottom.
- Use a "main guard" at the bottom of the file. Include a venv check here before calling `main()`:
    ```py
    if __name__ == "__main__":
        if not os.environ.get("VIRTUAL_ENV"):
            print("Error: no virtual environment detected. Run this script via './<script-name>' (requires uv), or activate a virtual environment first.")
            sys.exit(100)
        main()
    ```
- Prefer built-in libraries to maximise future compatibility. Suggested (when relevant): `argparse`, `atexit`, `getpass`, `os`, `pathlib`, `shutil`, `subprocess`, `sys`, `time`. Pre-approved external: `rich`. Other third-party libraries may be proposed if they are mainstream or would significantly enhance readability.
- When a `Path` object is already in hand, prefer `path.open(mode)` over `open(path, mode)`.
- Use `atexit` for cleanup of resources that must be released on normal exit and on `sys.exit()` (e.g. a log file opened at startup). Note: `atexit` handlers do not run on `os._exit()` or unhandled signals such as `SIGKILL`.
    ```py
    log = log_path.open("w")
    atexit.register(log.close)
    ```

## Config File Modifications

Scripts that modify user config files must be:

1. **Non-destructive** — never overwrite or delete existing content except where explicitly required; prefer targeted edits
2. **Idempotent** — repeated runs produce the same result; check whether the intended state already exists before making changes
3. **Non-conflicting** — before modifying, check whether a conflicting entry already exists (e.g. another assignment to the same variable); if so, leave the file untouched and surface the conflict to the user

Recommended helpers for common cases:

```python
def append_if_absent(path: Path, block: str) -> None:
    """Append block to path if not already present."""
    content = path.read_text() if path.exists() else ""
    if block in content:
        return
    with path.open("a") as f:
        f.write(("\n" if content and not content.endswith("\n") else "") + block + "\n")


def append_or_conflict(path: Path, block: str, conflict_pattern: str) -> None:
    """Append block to path, unless a conflicting entry already exists.

    conflict_pattern is a regex that matches entries incompatible with block,
    e.g. r'^export VAR=' for a variable that must only be set once.
    Raises RuntimeError on conflict.
    """
    import re
    content = path.read_text() if path.exists() else ""
    if block in content:
        return  # already present
    if re.search(conflict_pattern, content, re.MULTILINE):
        raise RuntimeError(
            f"Conflicting entry found in {path}. Please resolve manually before re-running."
        )
    append_if_absent(path, block)
```


## Sudo

Scripts that require elevated privileges for specific commands should ask for the password once upfront, before the work begins — rather than running the whole script as root or prompting mid-execution.

Below, `init_sudo()` skips the prompt if already root or if passwordless sudo is available. Otherwise it prompts once, retries up to 3 times on failure, and caches the result. All privileged `subprocess` calls then use the `sudo()` helper.

```python
import getpass
import os
import subprocess
import sys

_PASSWORDLESS = object()  # sentinel: sudo works without a password
_sudo_password = None     # None = uninitialised; _PASSWORDLESS or str = ready


def init_sudo():
    global _sudo_password
    if os.geteuid() == 0:
        _sudo_password = _PASSWORDLESS
        return
    if subprocess.run("sudo -n true", shell=True, capture_output=True).returncode == 0:
        _sudo_password = _PASSWORDLESS
        return
    for attempt in range(3):
        password = getpass.getpass("sudo password: ")
        result = subprocess.run(
            "sudo -S true", shell=True, text=True,
            input=password + "\n",
            capture_output=True,
        )
        if result.returncode == 0:
            _sudo_password = password
            return
        print("Incorrect password, try again." if attempt < 2 else "")
    print("Error: too many incorrect attempts.")
    sys.exit(1)


def sudo(cmd):
    if _sudo_password is None:
        raise RuntimeError("init_sudo() must be called before sudo()")
    if os.geteuid() == 0 or _sudo_password is _PASSWORDLESS:
        run(cmd)
    else:
        _console.print(f"$ {cmd}", style="bold cyan")
        proc = subprocess.Popen(
            ["sudo", "-S", "bash", "-c", f"set -o pipefail && {cmd}"], text=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        proc.stdin.write(_sudo_password + "\n")
        proc.stdin.close()
        output, _ = proc.communicate()
        if output:
            print(output, end="")
        if proc.returncode != 0:
            print(f"FAILED (exit {proc.returncode}): {cmd}")
            sys.exit(1)
```

Use `sudo()` exactly as you would use `subprocess.run()` for shell commands. The `init_sudo()` call belongs in `main()`, alongside other startup concerns like argument parsing — not in a helper buried in the business logic.

## Testing

Tests can be included in the same file using pytest with an inline dependency and self-executing main guard:

```py
#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["pytest"]
# ///

import pathlib
import sys
from unittest.mock import patch

import pytest

@pytest.fixture
def temp_home(tmp_path):
    with patch("pathlib.Path.home", return_value=tmp_path):
        yield tmp_path

def test_example(temp_home):
    assert temp_home.exists()

if __name__ == "__main__":
    if "pytest" not in sys.modules or "pytest.pytest_source" not in dir():
        sys.exit(pytest.main([__file__, "-v"]))
```

Key points:
- The `dependencies` in the script header ensures pytest is available when run via `./test_file.py`
- The main guard uses a simple check to avoid nesting pytest when collected by an external pytest run
- Tests can be run via `./test_file.py` (uses uv to run) or `uv run --with pytest pytest test_file.py`
