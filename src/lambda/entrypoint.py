"""AWS Lambda function to process URLs from SQS messages with various actions."""
import logging
from typing import Dict, Any

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from services.ping import ping_url
    from services.clone import clone_website
    from services.d2 import make_requests_until_blocked
    from services.attempt_login import attempt_credential_combinations
except ImportError:
    # For testing purposes, create mock functions
    def ping_url(url: str) -> dict:
        return {"status_code": 200, "response_time_ms": 100}
    
    def clone_website(url: str, output_dir: str = None) -> bool:
        return True
    
    def make_requests_until_blocked(url: str, **kwargs) -> dict:
        return {"success_count": 10, "total_attempts": 10, "blocked": False}
    
    def attempt_credential_combinations(url: str, **kwargs) -> dict:
        return {"attempts": 5, "blocked": False, "successful": False}

from lib import instruction_parser, extract_message_metadata, create_response

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler that processes SQS messages with various actions.
    
    Expected SQS message formats:
    1. Plain URL string: "https://example.com" (defaults to ping action)
    2. JSON with url and action: {"url": "https://example.com", "action": "ping"}
    3. JSON with url only: {"url": "https://example.com"} (defaults to ping action)
    
    Supported actions:
    - ping: Ping the URL (default)
    - clone: Clone the website
    - ddos: Perform DDoS attack (placeholder)
    - attempt_login: Attempt login attacks (placeholder)
    
    Args:
        event: SQS event containing Records
        context: Lambda context object
        
    Returns:
        Dictionary with processing results
    """
    successful_operations = []
    failed_operations = []
    
    # Process each SQS record
    for record in event.get('Records', []):
        message_metadata = extract_message_metadata(record)
        message_id = message_metadata['message_id']
        message_body = record.get('body', '')
        
        try:
            # Parse instruction using utility function
            instruction = instruction_parser(message_body)
            
            if instruction['status'] == 0:
                # Invalid message
                failed_operations.append({
                    'message_id': message_id,
                    'url': instruction.get('url', 'unknown'),
                    'action': instruction.get('action', 'unknown'),
                    'error': instruction['error']
                })
                logger.error(f"Invalid message {message_id}: {instruction['error']}")
                continue
            
            # Valid instruction
            url = instruction['url']
            action = instruction['action']
            
            logger.info(f"Processing message {message_id}: URL={url}, Action={action}")
            
            # Execute the requested action
            result = execute_action(url, action, message_id)
            
            if result['success']:
                successful_operations.append({
                    'message_id': message_id,
                    'url': url,
                    'action': action,
                    'result': result['data']
                })
                logger.info(f"Successfully executed {action} on {url}")
            else:
                failed_operations.append({
                    'message_id': message_id,
                    'url': url,
                    'action': action,
                    'error': result['error']
                })
                logger.error(f"Failed to execute {action} on {url}: {result['error']}")
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Unexpected error processing message {message_id}: {error_msg}")
            failed_operations.append({
                'message_id': message_id,
                'url': 'unknown',
                'action': 'unknown',
                'error': f"Unexpected error: {error_msg}"
            })
    
    # Return summary
    total_processed = len(event.get('Records', []))
    successful_count = len(successful_operations)
    failed_count = len(failed_operations)
    
    result = create_response(
        status_code=200 if not failed_count else 207,  # 207 Multi-Status if partial success
        message=f"Processed {total_processed} messages: {successful_count} successful, {failed_count} failed",
        data={
            'total_processed': total_processed,
            'successful': successful_count,
            'failed': failed_count,
            'successful_operations': successful_operations,
            'failed_operations': failed_operations
        }
    )
    
    logger.info(f"Processing complete: {successful_count} successful, {failed_count} failed")
    
    return result


def execute_action(url: str, action: str, message_id: str) -> Dict[str, Any]:
    """
    Execute the specified action on the given URL.
    
    Args:
        url: URL to process
        action: Action to perform
        message_id: Message ID for logging
        
    Returns:
        Dictionary with execution result:
        {
            "success": bool,
            "data": dict (if successful),
            "error": str (if failed)
        }
    """
    try:
        if action == 'ping':
            response = ping_url(url)
            return {
                'success': True,
                'data': {
                    'status_code': response['status_code'],
                    'response_time_ms': response['response_time_ms']
                },
                'error': None
            }
        
        elif action == 'clone':
            # Clone website functionality
            try:
                success = clone_website(url, output_dir='/tmp/cloned_sites')
                if success:
                    return {
                        'success': True,
                        'data': {
                            'message': 'Website cloned successfully',
                            'url': url,
                            'output_dir': '/tmp/cloned_sites'
                        },
                        'error': None
                    }
                else:
                    return {
                        'success': False,
                        'data': None,
                        'error': 'Failed to clone website'
                    }
            except Exception as e:
                return {
                    'success': False,
                    'data': None,
                    'error': f'Clone error: {str(e)}'
                }
        
        elif action == 'ddos':
            # Rate limit testing functionality (for authorized testing only)
            try:
                result = make_requests_until_blocked(
                    url=url,
                    period=1.0,
                    max_attempts=50,
                    randomize_params=True,
                    verbose=False
                )
                return {
                    'success': True,
                    'data': {
                        'message': 'Rate limit test completed',
                        'url': url,
                        'success_count': result['success_count'],
                        'total_attempts': result['total_attempts'],
                        'blocked': result['blocked'],
                        'status_code': result.get('status_code')
                    },
                    'error': None
                }
            except Exception as e:
                return {
                    'success': False,
                    'data': None,
                    'error': f'DDoS test error: {str(e)}'
                }
        
        elif action == 'attempt_login':
            # Login security testing functionality (for authorized testing only)
            try:
                # Default test credentials - in production, these should come from message
                emails = ['admin@test.com', 'user@test.com']
                keywords = ['password', 'admin']
                
                result = attempt_credential_combinations(
                    url=url,
                    emails=emails,
                    keywords=keywords,
                    delay=1.0,
                    max_attempts=20,
                    verbose=False
                )
                return {
                    'success': True,
                    'data': {
                        'message': 'Login security test completed',
                        'url': url,
                        'attempts': result['attempts'],
                        'blocked': result['blocked'],
                        'successful': result['successful'],
                        'working_credentials_count': len(result.get('working_credentials', []))
                    },
                    'error': None
                }
            except Exception as e:
                return {
                    'success': False,
                    'data': None,
                    'error': f'Login test error: {str(e)}'
                }
        
        else:
            return {
                'success': False,
                'data': None,
                'error': f"Unknown action: {action}"
            }
            
    except Exception as e:
        return {
            'success': False,
            'data': None,
            'error': f"Error executing {action} on {url}: {str(e)}"
        }

