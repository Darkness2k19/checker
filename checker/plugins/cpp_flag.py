from __future__ import annotations

from pathlib import Path

from checker.exceptions import PluginExecutionFailed

from .base import PluginABC, PluginOutput


class CppFlag(PluginABC):
    name = "cpp_flag"

    class Args(PluginABC.Args):
        task_path: Path
        flag: str | None

    def _run(self, args: Args, *, verbose: bool = False) -> PluginOutput:  # type: ignore[override]
        if args.flag is None:
            raise PluginExecutionFailed(output="Wrong true flag")

        with open(args.task_path / "flag.txt", "r") as f:
            lines = f.read().splitlines()
            flag = lines[0] if lines else ""

        if flag != args.flag:
            raise PluginExecutionFailed(output="Wrong flag")

        return PluginOutput(output="Correct flag")
