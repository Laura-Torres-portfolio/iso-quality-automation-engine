import os
from datetime import datetime
import pandas as pd


class ISOQualityEngine:
    """Automated Quality Assurance & ISO Compliance Engine for Food Manufacturing."""

    def __init__(
        self,
        temp_min=2.0,
        temp_max=4.0,
        weight_target=500.0,
        weight_tolerance=5.0,
        max_energy_kwh=150.0,
    ):
        # ISO 9001 & Food Safety Parameters
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.weight_min = weight_target - weight_tolerance
        self.weight_max = weight_target + weight_tolerance

        # ISO 14001 Environmental Parameters
        self.max_energy_kwh = max_energy_kwh

    def load_data(self, file_path: str) -> pd.DataFrame:
        """Ingest raw operational CSV logs."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source data file '{file_path}' not found.")

        df = pd.read_csv(file_path)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        print(f"📥 Data Ingested successfully: {len(df)} rows.")
        return df

    def validate_iso_compliance(self, df: pd.DataFrame) -> pd.DataFrame:
        """Applies business and compliance rules to evaluate each batch."""
        validated_df = df.copy()

        # Rule 1: Temperature Safety Check (HACCP / ISO 9001)
        validated_df["temp_compliance"] = validated_df[
            "storage_temp_celsius"
        ].between(self.temp_min, self.temp_max)

        # Rule 2: Packaging Weight Tolerance (ISO 9001 Product Quality)
        validated_df["weight_compliance"] = validated_df[
            "package_weight_grams"
        ].between(self.weight_min, self.weight_max)

        # Rule 3: Energy Threshold Check (ISO 14001 Environmental Efficiency)
        validated_df["energy_compliance"] = (
            validated_df["energy_kwh"] <= self.max_energy_kwh
        )

        # Rule 4: Mandatory Quality Sign-off Check
        validated_df["signoff_compliance"] = (
            validated_df["qa_signoff_operator"].notna()
        )

        # Overall Batch Compliance Status
        validated_df["is_fully_compliant"] = (
            validated_df["temp_compliance"]
            & validated_df["weight_compliance"]
            & validated_df["energy_compliance"]
            & validated_df["signoff_compliance"]
        )

        # Flag specific non-conformance reasons
        validated_df["non_conformance_reason"] = validated_df.apply(
            self._compile_failure_reasons, axis=1
        )

        return validated_df

    @staticmethod
    def _compile_failure_reasons(row: pd.Series) -> str:
        """Helper function to compile audit trail details for non-compliant records."""
        reasons = []
        if not row["temp_compliance"]:
            reasons.append("Temp Out of Bounds")
        if not row["weight_compliance"]:
            reasons.append("Weight Tolerance Violation")
        if not row["energy_compliance"]:
            reasons.append("ISO14001 Energy Spike")
        if not row["signoff_compliance"]:
            reasons.append("Missing QA Sign-off")

        return "; ".join(reasons) if reasons else "Compliant"

    def generate_audit_summary(self, df: pd.DataFrame) -> dict:
        """Calculates key quality KPIs for BI Reporting."""
        total_batches = len(df)
        compliant_batches = int(df["is_fully_compliant"].sum())
        non_conformances = total_batches - compliant_batches

        compliance_rate = round((compliant_batches / total_batches) * 100, 2)

        summary = {
            "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_batches_audited": total_batches,
            "compliant_batches": compliant_batches,
            "non_conformance_count": non_conformances,
            "overall_compliance_rate_pct": compliance_rate,
            "temp_violations": int((~df["temp_compliance"]).sum()),
            "iso14001_energy_exceedances": int(
                (~df["energy_compliance"]).sum()
            ),
            "missing_signoffs": int((~df["signoff_compliance"]).sum()),
        }
        return summary

    def export_processed_data(
        self,
        df: pd.DataFrame,
        output_file="cleaned_iso_compliance_data.csv",
    ):
        """Export clean data enriched with compliance metrics for Power BI / Tableau ingestion."""
        df.to_csv(output_file, index=False)
        print(f"💾 Processed data exported to: '{output_file}'")


# --- Pipeline Execution Flow ---
if __name__ == "__main__":
    # Initialize Engine
    engine = ISOQualityEngine()

    # Step 1: Ingest Data
    raw_file = "raw_factory_logs.csv"
    if not os.path.exists(raw_file):
        from generate_data import generate_mock_food_quality_data

        generate_mock_food_quality_data(raw_file)

    raw_data = engine.load_data(raw_file)

    # Step 2: Run Automated Validations
    processed_data = engine.validate_iso_compliance(raw_data)

    # Step 3: Compute Audit Metrics
    metrics = engine.generate_audit_summary(processed_data)

    print("\n--- 📊 ISO QUALITY AUDIT SUMMARY ---")
    for key, value in metrics.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print("------------------------------------\n")

    # Step 4: Export to BI Ready CSV
    engine.export_processed_data(processed_data)
