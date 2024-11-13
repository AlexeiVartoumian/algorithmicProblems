# main.tf
variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "bucket_prefix" {
  description = "Prefix for the S3 bucket name"
  type        = string
  default     = "my-app"
}

variable "table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default     = "my-table"
}

# Create S3 bucket with versioning
resource "aws_s3_bucket" "storage" {
  bucket = "${var.bucket_prefix}-${var.environment}-${random_string.suffix.result}"
}

resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

resource "aws_s3_bucket_versioning" "storage_versioning" {
  bucket = aws_s3_bucket.storage.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Add bucket encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "storage_encryption" {
  bucket = aws_s3_bucket.storage.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Create DynamoDB table
resource "aws_dynamodb_table" "table" {
  name           = "${var.table_name}-${var.environment}"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  
  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Environment = var.environment
    Terraform   = "true"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Create an SNS topic for notifications
resource "aws_sns_topic" "notifications" {
  name = "${var.environment}-notifications"
}

# Outputs
output "bucket_name" {
  description = "Name of the created S3 bucket"
  value       = aws_s3_bucket.storage.id
}

output "bucket_arn" {
  description = "ARN of the created S3 bucket"
  value       = aws_s3_bucket.storage.arn
}

output "dynamodb_table_name" {
  description = "Name of the created DynamoDB table"
  value       = aws_dynamodb_table.table.name
}

output "dynamodb_table_arn" {
  description = "ARN of the created DynamoDB table"
  value       = aws_dynamodb_table.table.arn
}

output "sns_topic_arn" {
  description = "ARN of the created SNS topic"
  value       = aws_sns_topic.notifications.arn
}

To use this module, you would:

First add a versions.tf file to your module:

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
  required_version = ">= 0.14"
}



Then call it from another Terraform configuration like this:

hclCopymodule "storage_resources" {
  source  = "app.terraform.io/<YOUR_ORG>/<MODULE_NAME>/<PROVIDER>"
  version = "1.0.0"

  environment    = "staging"
  bucket_prefix  = "my-company"
  table_name     = "users"
}

# You can reference outputs like this:
output "bucket_name" {
  value = module.storage_resources.bucket_name
}





📁 terraform-aws-storage/
├── README.md                   # Documentation of the module
├── main.tf                     # Main configuration file with resource definitions
├── variables.tf                # Variable declarations
├── outputs.tf                  # Output value declarations
├── versions.tf                 # Provider and terraform version constraints
└── examples/                   # Examples of how to use the module
    └── basic/
        ├── main.tf            # Example implementation
        ├── variables.tf       # Example variables
        └── outputs.tf         # Example outputs

# Contents of each file:

# variables.tf
variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "bucket_prefix" {
  description = "Prefix for the S3 bucket name"
  type        = string
  default     = "my-app"
}

variable "table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default     = "my-table"
}

# outputs.tf
output "bucket_name" {
  description = "Name of the created S3 bucket"
  value       = aws_s3_bucket.storage.id
}

output "dynamodb_table_name" {
  description = "Name of the created DynamoDB table"
  value       = aws_dynamodb_table.table.name
}

output "sns_topic_arn" {
  description = "ARN of the created SNS topic"
  value       = aws_sns_topic.notifications.arn
}

# versions.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
  required_version = ">= 0.14"
}

# examples/basic/main.tf
module "storage" {
  source = "../../"
  
  environment   = "dev"
  bucket_prefix = "example-company"
  table_name    = "users"
}

# README.md
# AWS Storage Terraform Module

This Terraform module creates:
- S3 bucket with versioning and encryption
- DynamoDB table with on-demand pricing
- SNS topic for notifications

## Usage

```hcl
module "storage" {
  source = "app.terraform.io/<YOUR_ORG>/storage/aws"
  
  environment   = "dev"
  bucket_prefix = "my-company"
  table_name    = "users"
}
```

## Requirements
- AWS provider >= 4.0
- Terraform >= 0.14

## Inputs
- `environment` - Environment name
- `bucket_prefix` - Prefix for S3 bucket
- `table_name` - DynamoDB table name

## Outputs
- `bucket_name` - Name of created S3 bucket
- `dynamodb_table_name` - Name of created DynamoDB table
- `sns_topic_arn` - ARN of created SNS topic