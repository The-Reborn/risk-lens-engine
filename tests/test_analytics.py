import pytest
import os
from app.services.analytics_service import RiskAnalyticsService

def test_risk_analytics_service_loads_data():
    """Test that the analytics service successfully loads the dataset and returns expected metrics."""
    service = RiskAnalyticsService()
    results = service.load_and_process_data()
    
    assert results is not None
    assert "total_records" in results
    assert results["total_records"] == 1000
    assert "columns" in results
    assert "summary_statistics" in results
    
    assert "age" in results["columns"]
    assert "total_claim_amount" in results["columns"]

def test_file_not_found_handling():
    """Test that the service raises FileNotFoundError for invalid file paths."""
    invalid_path = os.path.join(os.getcwd(), 'data', 'non_existent_file.xlsx')
    service = RiskAnalyticsService(file_path=invalid_path)
    
    with pytest.raises(FileNotFoundError):
        service.load_and_process_data()