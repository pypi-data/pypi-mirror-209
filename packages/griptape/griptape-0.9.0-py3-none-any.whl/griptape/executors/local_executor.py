from __future__ import annotations
import logging
import os
import subprocess
from typing import TYPE_CHECKING, Union, Optional
from attr import define, field
from griptape.artifacts import BaseArtifact, ErrorArtifact, TextArtifact
from griptape.executors import BaseExecutor

if TYPE_CHECKING:
    from griptape.core import BaseTool


@define
class LocalExecutor(BaseExecutor):
    verbose: int = field(default=False, kw_only=True)

    def try_execute(self, tool_activity: callable, value: Optional[dict]) -> Union[BaseArtifact, str]:
        tool = tool_activity.__self__

        logging.warning(f"You are executing the {tool.name} tool in the local environment. Make sure to "
                        f"switch to a more secure ToolExecutor in production.")

        env = os.environ.copy()

        env.update(tool.env)

        self.install_dependencies(env, tool)

        output = self.run_subprocess(env, tool_activity, value)

        if output.stderr and not output.stdout:
            return ErrorArtifact(output.stderr.strip())
        else:
            return output.stdout.strip()

    def install_dependencies(self, env: dict[str, str], tool: BaseTool) -> None:
        command = [
            "pip",
            "install",
            "-r",
            "requirements.txt",
            "-U"
        ]

        subprocess.run(
            command,
            env=env,
            cwd=self.tool_dir(tool),
            stdout=None if self.verbose else subprocess.DEVNULL,
            stderr=None if self.verbose else subprocess.DEVNULL
        )

    def run_subprocess(self, env: dict[str, str], tool_activity: callable, value: Optional[dict]) -> subprocess.CompletedProcess:
        tool = tool_activity.__self__
        tool_name = tool.class_name
        input_value = value if value else ""
        command = [
            "python",
            "-c",
            f'from tool import {tool_name}; print({tool_name}().{tool_activity.__name__}({input_value}))'
        ]

        return subprocess.run(
            command,
            env=env,
            cwd=self.tool_dir(tool),
            capture_output=True,
            text=True
        )
