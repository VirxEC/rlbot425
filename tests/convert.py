from pathlib import Path

from rlbot425.convert import Bot

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    v4_dir = base_dir / "v4-example"
    v5_dir = base_dir / "v425-example"

    bot = Bot(v4_dir / "bot.cfg")
    bot.write_to_toml(v5_dir / "bot.toml")
    bot.convert_python(v5_dir)

    print("Conversion complete.")
