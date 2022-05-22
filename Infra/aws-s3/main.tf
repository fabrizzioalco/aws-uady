resource "aws_s3_bucket" "PF-WebS-Bucket" {
  bucket = "pf-webs-bucket"
  acl    = "public-read"

  versioning {
    enabled = true
  }

  tags = {
    Name = "PF-WebS-Bucket"
  }
}
