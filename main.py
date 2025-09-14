#!/usr/bin/env python3
"""
Python Development Utilities
Simple standalone tools - independent of Jenkins pipeline
"""
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_config():
    """Generate application configuration"""
    config = {
        'app_name': 'DevOps Pipeline',
        'version': '1.0.0',
        'environments': {
            'dev': {'debug': True, 'timeout': 30},
            'prod': {'debug': False, 'timeout': 120}
        },
        'created': datetime.now().isoformat()
    }
    
    with open('app_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    logger.info("Configuration file created: app_config.json")
    return config

def process_sample_data():
    """Process sample deployment data"""
    sample_logs = [
        "INFO: Deployment started",
        "INFO: Docker image pulled",
        "WARNING: Service restart needed", 
        "INFO: Deployment completed"
    ]
    
    stats = {
        'total_logs': len(sample_logs),
        'info_count': sum(1 for log in sample_logs if 'INFO' in log),
        'warning_count': sum(1 for log in sample_logs if 'WARNING' in log)
    }
    
    logger.info(f"Processed {stats['total_logs']} log entries")
    return stats

def main():
    """Main utility function"""
    print("=" * 50)
    print("Python Development Utilities")
    print("Independent of Jenkins CI/CD Pipeline")
    print("=" * 50)
    
    # Generate config
    config = generate_config()
    
    # Process sample data
    stats = process_sample_data()
    
    # Show results
    print(f"✓ Config created for {config['app_name']}")
    print(f"✓ Processed {stats['total_logs']} log entries")
    print("✓ Utilities completed successfully")

if __name__ == '__main__':
    main()
