provider "aws" {
    region = "eu-west-1"
}

module "my_module_name" {
    source = "gitlab.path-to-repo/lcaol
    version = 0.0.54
}