variable "instance_type" {
  default     = "t2.micro"
  description = "Type of instance type"
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
