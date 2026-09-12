import pandas as pd
import pytest
from iso_quality_engine import ISOQualityEngine


@pytest.fixture
def engine():
    return ISOQualityEngine()


def test_temperature_validation_fails_out_of_bounds(engine):
    """Test that temperatures above 4.0°C trigger a temperature compliance failure."""
    sample_data = pd.DataFrame(
        [
            {
                "batch_id": "TEST-01",
                "storage_temp_celsius": 5.5,  # Too high
                "package_weight_grams": 500.0,
                "energy_kwh": 120.0,
                "qa_signoff_operator": "Tester",
            }
        ]
    )

    result = engine.validate_iso_compliance(sample_data)
    assert result.iloc[0]["temp_compliance"] == False
    assert result.iloc[0]["is_fully_compliant"] == False
    assert "Temp Out of Bounds" in result.iloc[0]["non_conformance_reason"]


def test_perfect_batch_passes_all_checks(engine):
    """Test that a compliant batch passes all checks."""
    sample_data = pd.DataFrame(
        [
            {
                "batch_id": "TEST-02",
                "storage_temp_celsius": 3.0,
                "package_weight_grams": 500.0,
                "energy_kwh": 130.0,
                "qa_signoff_operator": "Tester",
            }
        ]
    )

    result = engine.validate_iso_compliance(sample_data)
    assert result.iloc[0]["is_fully_compliant"] == True
    assert result.iloc[0]["non_conformance_reason"] == "Compliant"
