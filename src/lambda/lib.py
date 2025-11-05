"""Helper functions for Lambda entrypoint."""
import json
from typing import Dict, Any


def instruction_parser(message_body: str) -> Dict[str, Any]:
    """
    Parse SQS message body into instruction format.
    
    Args:
        message_body: Raw message body (plain URL or JSON)
        
    Returns:
        Dictionary with parsed instruction:
        {
            "status": 1 (success) or 0 (failure),
            "url": parsed URL,
            "action": action to perform (default: "ping"),
            "error": error message if status is 0
        }
    """
    # Try to parse as JSON first
    try:
        data = json.loads(message_body)
        
        # Extract URL
        if isinstance(data, dict):
            url = data.get('url')
            action = data.get('action', 'ping')
        else:
            # If it's not a dict, treat the whole thing as a URL
            url = str(data)
            action = 'ping'
    except (json.JSONDecodeError, ValueError):
        # Not JSON, treat as plain URL string
        url = message_body.strip()
        action = 'ping'
    
    # Validate URL
    if not url:
        return {
            'status': 0,
            'url': '',
            'action': '',
            'error': 'Empty URL'
        }
    
    if not isinstance(url, str):
        return {
            'status': 0,
            'url': str(url),
            'action': action,
            'error': 'URL must be a string'
        }
    
    # Basic URL validation
    if not url.startswith(('http://', 'https://')):
        return {
            'status': 0,
            'url': url,
            'action': action,
            'error': 'Invalid URL format - must start with http:// or https://'
        }
    
    return {
        'status': 1,
        'url': url,
        'action': action,
        'error': None
    }


def extract_message_metadata(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract metadata from SQS record.
    
    Args:
        record: SQS record dictionary
        
    Returns:
        Dictionary with message metadata
    """
    return {
        'message_id': record.get('messageId', 'unknown'),
        'receipt_handle': record.get('receiptHandle'),
        'attributes': record.get('attributes', {}),
        'message_attributes': record.get('messageAttributes', {})
    }


def create_response(status_code: int, message: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Create standardized Lambda response.
    
    Args:
        status_code: HTTP status code
        message: Response message
        data: Additional response data
        
    Returns:
        Standardized response dictionary
    """
    response = {
        'statusCode': status_code,
        'message': message
    }
    
    if data:
        response.update(data)
    
    return response
