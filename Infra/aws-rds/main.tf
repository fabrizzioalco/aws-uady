resource "aws_db_instance" "pf-webs-db" {
  identifier             = "pf-webs-db"
  name                   = "WebS-DB"
  instance_class         = "db.t2.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "14.5"
  skip_final_snapshot    = true
  publicly_accessible    = true
  vpc_security_group_ids = var.security_group_ids
  username               = "postgres"
  password               = var.db_password
}
