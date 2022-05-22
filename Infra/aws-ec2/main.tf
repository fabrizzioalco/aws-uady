locals {

  user_data = <<-EOT
  	#!/bin/bash
	sudo yum update -y
	sudo amazon-linux-extras install nginx1 -y 
	sudo systemctl enable nginx
	sudo systemctl start nginx
  EOT

  tags = {
    Owner       = "Fabrizzio A"
    Environment = "Production"
  }
}


####### RESOURCES THAT ARE NEED IT TO BE ABLE TO CREATE THE EC2 INSTNACE #######	
resource "aws_vpc" "PF-WebS-VPC" {
  cidr_block = "10.0.0.0/24"
}

resource "aws_subnet" "PF-PubSubnet1" {
  vpc_id            = aws_vpc.PF-WebS-VPC.id
  cidr_block        = "10.2.0.0/24"
  availability_zone = "us-east-1a"
}


resource "aws_network_interface" "PF-WebS-ENI" {
  subnet_id   = aws_subnet.PF-PubSubnet1.id
  private_ips = ["10.0.1.29/24"]

  tags = {
    Name = "PD-WebS-ENI"
  }
}

resource "aws_security_group" "allow_all" {
  name   = "allow_all"
  vpc_id = aws_vpc.PF-WebS-VPC.id
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "PF-WebS-SG"
  }
}

## 	EC2 INSTANCE ##
resource "aws_instance" "PF-WebS" {
  instance_type = "t2.micro"
  key_name      = "PF-WebS"
  ami           = "ami-0ff8a91507f77f867"

  network_interface {
    network_interface_id = aws_network_interface.PF-WebS-ENI.id
    device_index         = 0
  }
}