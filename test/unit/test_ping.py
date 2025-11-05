"""Unit tests for ping service."""
import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))

from services.ping import ping_url


@pytest.mark.unit
@pytest.mark.network
def test_ping_url_success():
    """Test successful URL ping."""
    result = ping_url("https://www.google.com")
    
    assert 'status_code' in result
    assert 'response_time_ms' in result
    assert isinstance(result['status_code'], int)
    assert isinstance(result['response_time_ms'], int)
    assert result['status_code'] == 200
    assert result['response_time_ms'] > 0


@pytest.mark.unit
def test_ping_url_invalid():
    """Test ping with invalid URL."""
    with pytest.raises(Exception):
        ping_url("not-a-valid-url")


@pytest.mark.unit
@pytest.mark.network
def test_ping_url_404():
    """Test ping returns 404 status."""
    result = ping_url("https://httpbin.org/status/404")
    
    assert result['status_code'] == 404
    assert 'response_time_ms' in result
