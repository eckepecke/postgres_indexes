# TPROC-C Benchmark Scripts Overview

This folder contains scripts for running the **TPROC-C** benchmark (a variant of TPC-C) against PostgreSQL using HammerDB. Below is a summary of each script's purpose:

---

## Scripts

### 1. `pg_tprocc_buildschema.py`

- **Purpose**: Creates the TPROC-C database schema (tables, indexes, and initial data).
- **Usage**: Run first to set up the database structure.
- **Actions**:
  - Creates tables (`warehouse`, `district`, `customer`, `orders`, etc.).
  - Populates initial test data (e.g., 100,000 items, warehouses).

---

### 2. `pg_tprocc_checkschema.py`

- **Purpose**: Validates the schema and data integrity after creation.
- **Usage**: Run after `buildschema` to ensure tables and data are correctly initialized.
- **Actions**:
  - Checks table existence and row counts.
  - Verifies constraints and indexes.

---

### 3. `pg_tprocc_deleteschema.py`

- **Purpose**: Drops the TPROC-C schema and cleans up the database.
- **Usage**: Run after benchmarking to reset the database.
- **Actions**:
  - Drops tables, indexes, and other objects.

---

### 4. `pg_tprocc_run.py`

- **Purpose**: Executes the TPROC-C workload (simulates transactions).
- **Usage**: Run after `buildschema` and `checkschema` to start the benchmark.
- **Actions**:
  - Spawns virtual users for concurrent transactions.
  - Measures throughput (transactions per second) and latency.

---

### 5. `pg_tprocc_result.py`

- **Purpose**: Generates performance results and metrics.
- **Usage**: Run after `pg_tprocc_run.py` to analyze benchmark results.
- **Actions**:
  - Parses logs and calculates KPIs (e.g., TPS, latency).
  - Outputs results in human-readable format.

---

### 6. Wrapper Scripts

- **`pg_tprocc_py.sh` (Linux/macOS)**  
  **`pg_tprocc_py.ps1` (Windows)**
  - **Purpose**: Simplifies execution of the Python scripts.
  - **Usage**: Run these to automate the workflow (build → check → run → result).
  - **Actions**:
    - Sets environment variables.
    - Calls the relevant Python scripts in sequence.

---

## Workflow Order

1. `buildschema` → 2. `checkschema` → 3. `run` → 4. `result` → 5. `deleteschema` (optional).

---

## Notes

- Replace placeholders (e.g., database credentials, hostnames) in the scripts before execution.
- Use the wrapper scripts (`pg_tprocc_py.sh`/`.ps1`) for a streamlined process.
