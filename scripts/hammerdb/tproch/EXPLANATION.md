# TPROC-H Benchmark Scripts Overview

This folder contains scripts for running the **TPROC-H** benchmark (a variant of **TPC-H**) against PostgreSQL using HammerDB. TPROC-H focuses on **analytical/OLAP workloads** with complex queries, unlike TPROC-C's transactional focus. Below is a summary of each script's purpose:

---

## Scripts

### 1. `pg_tproch_buildschema.py`

- **Purpose**: Creates the TPROC-H database schema for analytical workloads.
- **Usage**: Run first to set up the database structure.
- **Actions**:
  - Creates TPC-H tables (`nation`, `region`, `part`, `supplier`, `partsupp`, `customer`, `orders`, `lineitem`).
  - Populates large-scale test data (configurable scale factor).

---

### 2. `pg_tproch_checkschema.py`

- **Purpose**: Validates the schema and data integrity for analytical queries.
- **Usage**: Run after `buildschema` to ensure data quality for complex joins.

---

### 3. `pg_tproch_deleteschema.py`

- **Purpose**: Drops the TPROC-H schema and cleans up large datasets.
- **Usage**: Run after benchmarking to free up storage.

---

### 4. `pg_tproch_run.py`

- **Purpose**: Executes TPROC-H's 22 analytical queries with timing.
- **Usage**: Run after schema setup to measure OLAP performance.
- **Actions**:
  - Executes complex joins, aggregations, and reporting queries.
  - Measures query execution time and throughput.

---

### 5. `pg_tproch_result.py`

- **Purpose**: Generates analytical performance metrics.
- **Actions**:
  - Calculates **Query-per-Hour (QpH)** and individual query times.
  - Produces comparative reports for scalability testing.

---

### 6. Wrapper Scripts

- **`pg_tproch_py.sh`**/**`pg_tproch_py.ps1`**
- **Purpose**: Automates the **multi-stage workflow**:
  1. Build schema with large datasets
  2. Validate data integrity
  3. Execute analytical queries
  4. Generate performance reports

---

## Key Differences from TPROC-C

1. **Schema**: Uses TPC-H's **8 normalized tables** instead of TPC-C's denormalized schema.
2. **Workload**: Focuses on **read-heavy analytical queries** rather than transactional updates.
3. **Data Scale**: Typically requires **larger datasets** (100GB+ for meaningful results).
4. **Metrics**: Tracks **query complexity/throughput** rather than transactions-per-second.

---

## Workflow Order

1. `buildschema` → 2. `checkschema` → 3. `run` → 4. `result` → 5. `deleteschema` (optional).

---

## Notes

- Configure **scale factor** in `buildschema` to control dataset size.
- Ensure PostgreSQL has adequate **work_mem** and **shared_buffers** for OLAP workloads.
- Run on hardware with **fast storage** due to large table scans.
