provider "aws" {
  region  = var.region
  profile = var.profile
}

terraform {
  backend "local" {
    path = "../state/terraform.tfstate"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 2.7.0"
    }
  }
}

