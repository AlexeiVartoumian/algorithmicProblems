locals {
    eu_west_1_azs = slice(
        sort(data.aws_avaiablity_zones.eu_west_1.names),
        0,
        var.number_of_azs
    )
}