variable "ami_value" {
  description = "The AMI ID to use for the EC2 instance"
  type        = string
}

variable "instance_type_value" {
  description = "The type of instance to create"
  type        = string
  default     = "t2.micro"
}

variable "subnet_id_value" {
  description = "The Subnet ID where the instance will be launched"
  type        = string
}
