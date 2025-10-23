terraform {
  backend "s3" {
    bucket         = "pradeep-s3-demo-xyz" # change this
    key            = "pra/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
