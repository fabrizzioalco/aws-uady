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

variable "security_group_ids" {
  default     = ["sg-01c5908666c3e76c2"]
  description = "Security group IDs"
  type        = list(string)
}

