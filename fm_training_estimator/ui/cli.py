# Standard
import logging

# Third Party
import fire
import json
import os

# Local
from .core import run

def _run(config, output=None, lookup_data_path=None, model_path=None, use_model_features=True):
    res = run(config, lookup_data_path, model_path, use_model_features)

    out =  {
        "total_mem_estimate_og": float(res["total_mem_estimate_og"]),
        "activation_memory_og":  float(res["activation_memory_og"]),
        "gradient_memory_og":    float(res["gradient_memory_og"]),
        "model_memory_og": float(res["model_memory_og"]),
        "optimizer_memory_og": float(res["optimizer_memory_og"]),
        "total_mem_estimate": res["total_mem_estimate"],
        "activation_memory": res["activation_memory"],
        "gradient_memory": res["gradient_memory"],
        "model_memory": res["model_memory"],
        "optimizer_memory": res["optimizer_memory"],
        "tps": float(res["tps"])
    }

    outs = json.dumps(out)
    if output is None:
        results_file = "results.json"
    else:
        results_file = output
    with open(results_file, 'w') as f:
        f.write(outs)
    logging.info(f"estimator results: {outs}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(_run)