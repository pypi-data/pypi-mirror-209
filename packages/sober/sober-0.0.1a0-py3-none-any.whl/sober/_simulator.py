from pathlib import Path
from platform import system
from subprocess import PIPE, STDOUT, run


def _energyplus_default_root(major: str, minor: str, patch: str = "0") -> Path:
    version = "-".join((major, minor, patch))
    match system():
        case "Linux":
            return Path(f"/usr/local/EnergyPlus-{version}")
        case "Darwin":
            return Path(f"/Applications/EnergyPlus-{version}")
        case "Windows":
            return Path(rf"C:\EnergyPlusV{version}")
        case _ as system_name:
            raise NotImplementedError(f"unsupported system: '{system_name}'.")


def _run_energyplus(
    model_file: Path,
    weather_file: Path,
    output_directory: Path,
    has_macros: bool,
    has_templates: bool,
    energyplus_root: Path,
) -> None:
    commands = (
        (energyplus_root / "energyplus",)
        + (("-m",) if has_macros else ())
        + (("-x",) if has_templates else ())
        + ("-w", weather_file, model_file)
    )
    run(commands, stdout=PIPE, stderr=STDOUT, cwd=output_directory, text=True)


def _run_readvars(
    rvi_file: Path,
    output_directory: Path,
    frequency: str,
    energyplus_root: Path,
):
    commands = (
        energyplus_root / "PostProcess" / "ReadVarsESO",
        rvi_file,
        "Unlimited",
        "FixHeader",
        frequency,
    )
    run(commands, stdout=PIPE, stderr=STDOUT, cwd=output_directory, text=True)
