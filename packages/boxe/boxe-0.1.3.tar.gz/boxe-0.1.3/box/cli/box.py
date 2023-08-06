
# def main():
#     sys.argv = ['box', '--root', box.__path__[0]] + sys.argv[1:]
#     poethepoet.main()

def main():
    import os
    import sys
    import poethepoet
    from pathlib import Path
    from poethepoet.app import PoeThePoet

    if len(sys.argv) == 2 and sys.argv[1].startswith("_"):
        first_arg = sys.argv[1]
        if first_arg in {"_list_tasks", "_describe_tasks", "_zsh_completion", "_bash_completion", "_fish_completion"}:
            return poethepoet.main()

    import box.poe as box_poe

    sys.argv[0] = "box"
    sys.argv.insert(1, "-q")

    os.environ["ROOT"] = str(Path.cwd().resolve())
    path = Path(box_poe.__path__[0]).resolve()
    os.chdir(path)

    app = PoeThePoet(cwd=path, output=sys.stderr)
    result = app(cli_args=sys.argv[1:])

    if result:
        raise SystemExit(result)
