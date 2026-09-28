"""Verify the paper's mAP correction using only Python's standard library."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
M = 300
R = 2


def correction(logged: float, m: int = M, r: int = R) -> float:
    return ((r + 1) * logged - (r + 1) / m) / r


def intended_ap(first_rank: int, second_rank: int) -> float:
    return (1.0 / first_rank + 2.0 / second_rank) / 2.0


def archived_ap(first_rank: int, second_rank: int, m: int = M) -> float:
    return (1.0 / first_rank + 2.0 / second_rank + 3.0 / m) / 3.0


def load(name: str):
    with (RAW / name).open(encoding="utf-8") as handle:
        return json.load(handle)


def close(a: float, b: float, tol: float = 1e-12) -> None:
    if not math.isclose(a, b, rel_tol=0.0, abs_tol=tol):
        raise AssertionError(f"{a!r} != {b!r}")


def verify_rank_identity() -> int:
    checked = 0
    for first, second in itertools.combinations(range(1, M), 2):
        close(correction(archived_ap(first, second)), intended_ap(first, second))
        checked += 1
    return checked


def verify_aggregates() -> None:
    receipt = load("derived_corrected_map.json")
    salvage = load("salvage_results.json")
    dino = load("dino_results.json")
    labels = {"I-JEPA": "jepa", "C-JEPA": "cjepa", "MAE": "mae", "VICReg": "vicreg"}
    for label, key in labels.items():
        mean, sd = salvage["methods"][key]["map"]
        close(correction(mean), receipt["controlled_binarised"][label]["corrected_mean"])
        close(1.5 * sd, receipt["controlled_binarised"][label]["corrected_sd"])
    mean, sd = dino["map"]
    close(correction(mean), receipt["controlled_binarised"]["DINO"]["corrected_mean"])
    close(1.5 * sd, receipt["controlled_binarised"]["DINO"]["corrected_sd"])

    history = load("sota_color_4exec.json")["executions"]
    key_to_label = {"jepa": "I-JEPA", "cjepa": "C-JEPA", "mae": "MAE", "vicreg": "VICReg", "dino": "DINO"}
    for receipt_key, execution in zip(receipt["historical_colour"], history.values()):
        for key, value in execution["map"].items():
            close(correction(value), receipt["historical_colour"][receipt_key][key_to_label[key]])

    precision = load("fullconfig_determinism.json")
    for row in precision:
        method = {"vicreg": "VICReg", "dino": "DINO", "mae": "MAE"}[row["method"]]
        mode = "AMP" if row["amp"] else "fp32"
        close(correction(row["map"]), receipt["precision_diagnostic"][method][mode])

    pretrained = load("pretrained_calibration.json")["pretrained_vit_s16_imagenet_retrieval_mAP"]
    close(correction(pretrained), receipt["frozen_pretrained"]["corrected"])


def main() -> None:
    checked = verify_rank_identity()
    if checked != 44_551:
        raise AssertionError(checked)
    verify_aggregates()
    print(f"PASS: {checked} rank-pair identities and all retained aggregate corrections verified")


if __name__ == "__main__":
    main()
