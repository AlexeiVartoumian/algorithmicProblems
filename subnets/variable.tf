



variable "number_of_azs" {
    description = "the number of availablity zones to use "
    type = number
    default = 3 
}

variable "vpc_id" {
    description = "the id of the vpc in eu-west-1"
    type = string
    default = "vpc-123"

}

variable "vpc_cidr_block" {
    description = "the cidr block of the vpc in eu-west-1"
    type = string 
    default = "13.555.873" 
}