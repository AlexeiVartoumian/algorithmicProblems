

resource "aws_subnet" "private" {

    for_each = {for idx , az in local.eu_west_1_azs: az => idx}

    vpc_id = var.vpc_id
    cidr_block = var.vpc_cidr_block
    availablity_zone = each.key
    
    tags = {
        Name = "Subnet-${each.key}"
        Environment = "Test"
    }

}