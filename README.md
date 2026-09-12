# 🛡️ ISO Quality & Environmental Data Automation Engine
> An automated Quality Assurance and Data Pipeline for Food Industry Compliance (ISO 9001 & ISO 14001)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Framework: Pytest](https://img.shields.io/badge/tested%20with-pytest-blueviolet)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Executive Overview

In the food manufacturing industry, maintaining strict adherence to **ISO 9001 (Quality Management)** and **ISO 14001 (Environmental Management)** standards is crucial. Traditional compliance auditing often relies on manual logs, delayed reporting, and error-prone Excel spreadsheets.

The **ISO Quality & Environmental Data Automation Engine** addresses this operational bottleneck by providing an automated **ETL (Extract, Transform, Load)** pipeline. Built with **Python** and **Pandas**, this tool ingests raw factory telemetry and operator logs, validates every batch against programmatic quality and environmental thresholds, logs detailed audit trails for non-conformances, and exports BI-ready datasets for real-time reporting in **Power BI**, **Tableau**, or **Streamlit**.

---

## ✨ Key Features & Capabilities

* 📥 **Automated Data Ingestion:** Reads multi-source factory telemetry, HACCP temperature records, packaging metrics, and operator sign-offs.
* 🎯 **ISO 9001 Quality Validation:**
  * **Temperature Monitoring:** Automatically flags batches exceeding safe Cold Chain limits ($2.0^\circ\text{C} - 4.0^\circ\text{C}$).
  * **Net Weight Control:** Assesses package weight tolerances ($500\text{g} \pm 5\text{g}$) to prevent under-filling or yield loss.
  * **Traceability & Governance:** Ensures mandatory Quality Assurance operator sign-off is logged per batch.
* 🌿 **ISO 14001 Environmental Tracking:**
  * **Energy Consumption Checks:** Monitors energy usage per batch, flagging spikes that exceed environmental benchmarks ($>150\text{ kWh}$).
* 🔍 **Granular Audit Trails:** Automatically compiles detailed failure reason codes for quick root-cause analysis and corrective action (CAPA).
* 🧪 **Automated Software SQA:** Includes unit testing built with `pytest` to guarantee rule engine reliability and prevent regressions.
* 📊 **BI-Ready Analytics Export:** Formats and exports clean, enriched data directly consumed by Business Intelligence tools.

---

## 🏗️ System Architecture & Workflow

```mermaid
flowchart TD
    A["📥 Raw Telemetry Data<br/><i>(Temp, Packaging Weights, Energy, Sign-offs)</i>"] --> B["⚙️ ISO Quality Engine<br/><i>(Python / Pandas Rules Engine)</i><br/>• ISO 9001 Controls<br/>• ISO 14001 Thresholds"]
    
    B --> C["📋 Audit Summary Metrics<br/><i>(CLI Logs & Audit Trail)</i>"]
    B --> D["📊 Enriched BI Dataset (.csv)<br/><i>(Power BI / Tableau Ready)</i>"]

    style A fill:#f9f9f9,stroke:#333,stroke-width:1px
    style B fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style C fill:#fff3e0,stroke:#f57c00,stroke-width:1px
    style D fill:#e8f5e9,stroke:#388e3c,stroke-width:1px
```

## 🚀 Quick Start Guide

### Prerequisites
* **Python 3.9+**
* **Git**

### 1. Clone the Repository
```bash
git clone [https://github.com/Laura-Torres-portfolio/project-1.git](https://github.com/Laura-Torres-portfolio/project-1.git)
cd project-1
