from pathlib import Path

base_agent_file_end = [
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    from rlbot425.agents.standalone.standalone_bot import run_bot\n",
    "    run_bot(MyBot)\n",
]


class PyConv:
    key_replacements = {
        "import rlbot": "import rlbot425",
        "from rlbot": "from rlbot425",
    }

    def __init__(self, py_file: Path):
        self.base_dir = py_file.parent
        self.py_file = py_file
        self.files = list(self.base_dir.glob("**/*.py"))

    def convert(self, v5_base_dir: Path):
        self.write_requirements(v5_base_dir)

        for file in self.files:
            new_contents: list[str] = self._convert_file(file)

            new_file = v5_base_dir / file.relative_to(self.base_dir)
            new_file.parent.mkdir(parents=True, exist_ok=True)
            with open(new_file, "w") as f:
                f.writelines(new_contents)

    def write_requirements(self, v5_base_dir: Path):
        requirements = self.base_dir / "requirements.txt"
        new_requirements = v5_base_dir / "requirements.txt"

        lines = []
        if requirements.exists():
            with open(requirements, "r") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                if "rlbot" in line:
                    del lines[i]

        lines.append("rlbot>=2.0.0.beta")

        with open(new_requirements, "w") as f:
            for line in lines:
                f.write(line)

    def _convert_file(self, file: Path) -> list[str]:
        with open(file, "r") as f:
            lines = f.readlines()

        has_base_agent = False

        for i, line in enumerate(lines):
            if "(BaseAgent):" in line:
                has_base_agent = True
            lines[i] = self._convert_keywords(line)

        if has_base_agent:
            lines.extend(base_agent_file_end)

        return lines

    def _convert_keywords(self, line: str) -> str:
        for key, value in self.key_replacements.items():
            line = line.replace(key, value)

        return line
