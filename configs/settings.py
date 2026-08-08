from pathlib import Path

# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
CHARTS_DIR = PROJECT_ROOT / "charts"

# Benchmark configuration
NUM_USERS = 10000
NUM_RELATIONSHIPS = 50000

# Number of times each benchmark is repeated
NUM_RUNS = 5

# Random seed for reproducibility
RANDOM_SEED = 42