 
import os

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

def create_cargo_toml(service_name):
    content = f"""[package]
name = "{service_name}"
version = "0.1.0"
edition = "2021"

[dependencies]
env_logger = "0.11.0"
log = "0.4.20"
tonic = "0.10"
prost = "0.12"
prost-types = "0.12"
tokio = {{ version = "1", features = ["full"] }}

[build-dependencies]
tonic-build = "0.10"
"""
    return content

def create_main_rs():
    return """use env_logger;
use log::info;

fn main() {
    env_logger::init();
    info!("Service is starting up.");
    // Rest of the main function
}
"""

def create_lib_rs():
    return """use log::info;

pub fn run() {
    info!("Library code goes here");
    // Rest of the library code
}
"""

def create_build_rs(service_name):
    return f"""use tonic_build;

fn main() -> Result<(), Box<dyn std::error::Error>> {{
    tonic_build::compile_protos("protocol/{service_name}.proto")?;
    Ok(())
}}
"""

def create_proto_file(service_name):
    return f"""syntax = "proto3";

package {service_name};

// The {service_name} service definition.
service {service_name}Service {{
  // Define RPC methods here
  rpc SampleMethod (SampleRequest) returns (SampleResponse);
}}

// The request message containing the user's name.
message SampleRequest {{
  string name = 1;
}}

// The response message containing the greetings
message SampleResponse {{
  string message = 1;
}}
"""

def main():
    base_path = "./"

    for service in services:
        service_path = os.path.join(base_path, service)
        src_path = os.path.join(service_path, "src")
        os.makedirs(src_path, exist_ok=True)

        # Create Cargo.toml and build.rs
        with open(os.path.join(service_path, "Cargo.toml"), "w") as file:
            file.write(create_cargo_toml(service))
        with open(os.path.join(service_path, "build.rs"), "w") as file:
            file.write(create_build_rs(service))

        # Create main.rs and lib.rs
        with open(os.path.join(src_path, "main.rs"), "w") as file:
            file.write(create_main_rs())
        with open(os.path.join(src_path, "lib.rs"), "w") as file:
            file.write(create_lib_rs())

        # Create protocol directory and .proto file
        proto_path = os.path.join(service_path, "protocol")
        os.makedirs(proto_path, exist_ok=True)
        with open(os.path.join(proto_path, f"{service}.proto"), "w") as file:
            file.write(create_proto_file(service))

    print("Cargo projects with gRPC dependencies, build.rs, and protocol files generated.")

if __name__ == "__main__":
    main()