provider "aws" {
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key

  default_tags {
    tags = {
      project = "tf_demo"
    }
  }
}

resource "aws_vpc" "default" {
  cidr_block           = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true

}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = var.cidr_block_a
  map_public_ip_on_launch = "true"
  availability_zone       = var.av_a
}

resource "aws_subnet" "public_b" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = var.cidr_block_b
  map_public_ip_on_launch = "true"
  availability_zone       = var.av_b
}

resource "aws_internet_gateway" "default_igw" {
  vpc_id = aws_vpc.default.id
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.default.id

  route {
    cidr_block = var.open_internet
    gateway_id = aws_internet_gateway.default_igw.id
  }
}

resource "aws_route_table_association" "rt_association_a" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "rt_association_b" {
  subnet_id      = aws_subnet.public_b.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_security_group" "allow_sql" {
  vpc_id = aws_vpc.default.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.open_internet]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [var.open_internet]
  }

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [var.open_internet]
  }
}

resource "aws_instance" "demo2" {
  ami                    = var.ami
  instance_type          = var.type
  subnet_id              = aws_subnet.public_a.id
  vpc_security_group_ids = [aws_security_group.allow_sql.id]
  key_name               = aws_key_pair.developer.key_name
}

resource "aws_key_pair" "developer" {
  key_name   = "developer_key"
  public_key = var.public_key
}

output "public_ip" {
  value = aws_instance.demo2.public_ip
}