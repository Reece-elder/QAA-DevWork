variable "region" {
  default = "eu-west-2"
}

variable "access_key" {
  #   default = "AKIA5KAPQHIRYPVWUUFP"
  sensitive = true
}

variable "secret_key" {
  #   default = "phHMdh0ZquTc+SaEuoR6a9PKTIWSaNC5fniqpxWh"
  sensitive = true
}

variable "ami" {
  default = "ami-0fb391cce7a602d1f"
}

variable "type" {
  default = "t2.micro"
}

variable "cidr_block" {
  default = "10.0.0.0/16"
}

variable "cidr_block_a" {
  default = "10.0.1.0/24"
}

variable "cidr_block_b" {
  default = "10.0.2.0/24"
}

variable "av_a" {
  default = "eu-west-2a"
}

variable "av_b" {
  default = "eu-west-2b"
}

variable "open_internet" {
  default = "0.0.0.0/0"
}

variable "public_key" {
  #   default = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0aEUfHOK5w5JwwiRJsW+NrAOzweEzPRajyi87LxaRwod3bCb8j1Y7dHAax+JCI9gqGIorZOgGibkCzoJpb9ICMZVEHeguz6/fSSgGTurCYVIyXU1axCawCBXAAl9gRuwZjGGp32kfL1qlPlWtHEtEMj2sUSnOse44vE2sUbGECKjJf4gzwmW6CiWNP+6E0lhj7sUKtcp0caCS21oZQaQLY08+QtQwmpN7U+RHWC6wHhPDywEvBdmXhGPROuWU9XqH3tW5igIsrsN3meO+6rAR+d6vh6wfRs/gdHzRqCL4oyljf/fxNq46B81iW93KAO1Ct+FtmaU0dcvMaU1/W5Cnej05CEKa+OHjPzZu8XomwG5SL6kJOAb3MbLkxxJVNZq+c9i6LuRwvKhXbPgjTDNUZt9rsgtzpsAeukBjfaTWPMUWsb8aL7U//n1r3av0jnSyGxLn4wGrCwdQ7TYnhOoKHoFmoIUxP4xTu1GMvP+z7dHYsREcks3gPdb6ru6/A6E= ubuntu@ip-172-31-33-20"
  sensitive = true
}