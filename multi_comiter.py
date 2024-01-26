import os
import subprocess

def git_init_commit(service_path):
    # Navigate to the service directory
    os.chdir(service_path)

    # Initialize Git repository if not already a repo
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])

    # Add all files to the staging area
    subprocess.run(['git', 'add', '.'])

    # Commit the changes
    subprocess.run(['git', 'commit', '-m', 'fix: tonic-build dep'])

def main():
    base_path = "/home/victor/Workspace/Hackerthons/DevSpot/Bulto/"  # Update with the path to your workspace

    services = [
        "user_management",
        "financial_transactions",
        "credit_scoring",
        "lending",
        "card_integration",
        "point_of_sale",
        "mobile_money",
        "crm",
        "ai_assistant",
        "fraud_detection",
        "notification",
        "reporting_analytics",
        "api_gateway",
        "database_service",
        "authentication_authorization",
        "load_balancing",
        "cache_management",
        "logging_monitoring",
        "data_synchronization",
        "backup_recovery",
        "message_queuing",
        "configuration_management",
        "security",
        "service_discovery",
        "microservices_deployment"
    ]

    for service in services:
        service_path = os.path.join(base_path, service)
        git_init_commit(service_path)

    print("Initial commits completed for all services.")

if __name__ == "__main__":
    main()
