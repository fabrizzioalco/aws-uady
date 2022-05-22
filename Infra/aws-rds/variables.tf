variable "db_password" {
  description = "Password for the database"
  type        = string
}

variable "region" {
  default     = "us-east-1"
  description = "AWS Region"
  type        = string
}

variable "profile" {
  default     = "uady-profile"
  description = "AWS Profile"
  type        = string
}

