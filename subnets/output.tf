output "subnet_ids" {
    description = "list of subnet Ids created in eu-west-1"
    value = [for subnet in aws_subnet.private : subnet.id]
}

output "subnet_cidr_blocks" {
    description = "Map of subnet CIDR blocks by AZ"
    value = {
        for az , subnter in aws_subnet.private : az => subnet.cidr_block 
    }
}

output "availablity_zones" {
    description = "List of avilablity zones used"
    value = local.ap_west_2_azs
}