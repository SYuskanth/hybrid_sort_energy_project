import os
import time
import subprocess
import pandas as pd
import numpy as np
import random

# ============================================================
#  Import Hybrid Sorting Algorithms
# ============================================================
from algorithms.timsort import timsort
from algorithms.introsort import introsort
from algorithms.hybrid_quick_insertion import hybrid_quick_insertion
from algorithms.dual_pivot_quicksort import dual_pivot_quicksort
from algorithms.recombinant_sort import recombinant_sort

# ============================================================
#  Intel Power Gadget Setup
# ============================================================
#  Update this path if your Power Gadget version folder is different (e.g. 3.7)
POWER_LOG_PATH = r"C:\Program Files\Intel\Power Gadget 3.6\PowerLog3.0.exe"

# ============================================================
#  Directory Setup
# ============================================================
RESULTS_DIR = "results"
ENERGY_LOG_DIR = os.path.join(RESULTS_DIR, "energy_logs")
RESULT_FILE = os.path.join(RESULTS_DIR, f"final_results_{time.strftime('%Y%m%d_%H%M%S')}.csv")

os.makedirs(ENERGY_LOG_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ============================================================
#  Algorithm Dictionary
# ============================================================
ALGORITHMS = {
    "Timsort": timsort,
    "IntroSort": introsort,
    "HybridQuickInsertion": hybrid_quick_insertion,
    "DualPivotQuickSort": dual_pivot_quicksort,
    "RecombinantSort": recombinant_sort
}

# ============================================================
#  Energy Measurement Function
# ============================================================
def measure_energy(algorithm_name, func, data, duration=15):
    """
    Runs a sorting algorithm while Intel Power Gadget logs energy usage.
    Returns runtime, average power, and total energy.
    """
    log_path = os.path.join(ENERGY_LOG_DIR, f"{algorithm_name}_log.csv")

    # Start Intel Power Gadget logging
    log_process = subprocess.Popen([
        POWER_LOG_PATH,
        "-resolution", "100",        # 100 ms sampling interval
        "-file", log_path,
        "-duration", str(duration)   # Logging duration in seconds
    ])
    time.sleep(1)  # Give Power Gadget time to start logging

    # Run sorting algorithm
    start = time.time()
    func(data.copy())
    end = time.time()
    runtime = end - start

    # Stop logging process
    log_process.wait()

    # Read Power Gadget CSV file
    try:
        df = pd.read_csv(log_path)
        # Some Power Gadget versions may use Processor Power_1(Watt)
        power_col = [col for col in df.columns if "Processor Power" in col][0]
        avg_power = df[power_col].mean()
        total_energy = np.sum(df[power_col] * 0.1)  # (W) * (0.1 s) = Joules
    except Exception as e:
        print(f"[WARN] Error reading log for {algorithm_name}: {e}")
        avg_power, total_energy = 0, 0

    return runtime, avg_power, total_energy

# ============================================================
#  Main Experiment Loop
# ============================================================
def main():
    sizes = [1000, 10000, 50000, 100000, 200000, 500000, 1000000]
    runs_per_algorithm = 10  # Repeat each run 10 times for accuracy
    results = []

    print("\n Starting Energy Measurement Experiment...\n")
    print(f"Intel Power Gadget Path: {POWER_LOG_PATH}")
    print(f"Results will be saved to: {RESULT_FILE}\n")

    for n in sizes:
        data = [random.randint(0, n) for _ in range(n)]
        for name, func in ALGORITHMS.items():
            for run in range(runs_per_algorithm):
                print(f" Running {name} | Size={n} | Run={run + 1}")
                runtime, avg_power, total_energy = measure_energy(name, func, data)
                
                results.append({
                    "Algorithm": name,
                    "InputSize": n,
                    "Run": run + 1,
                    "Runtime(s)": round(runtime, 4),
                    "AvgPower(W)": round(avg_power, 2),
                    "Energy(J)": round(total_energy, 2)
                })

                # Print summary for this run
                print(f" {name} | Size={n} | Run={run + 1} | "
                      f"Runtime={runtime:.3f}s | Power={avg_power:.2f}W | Energy={total_energy:.2f}J\n")

                # Save intermediate results (auto-backup)
                pd.DataFrame(results).to_csv(RESULT_FILE, index=False)

                # Cooldown between runs (for accurate energy readings)
                time.sleep(5)

    print("\n Experiment complete!")
    print(f"Results saved to: {RESULT_FILE}\n")

# ============================================================
#  Run the Experiment
# ============================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Experiment interrupted by user. Partial results saved.")
    except Exception as e:
        print(f"\n Error occurred: {e}")
