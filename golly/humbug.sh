cat > config.yml << EOF
# Terraboard configuration for Terraform Enterprise
log:
  level: info
  format: plain

database:
  host: db
  port: 5432
  user: gorm
  password: supersecret
  name: gorm
  sslmode: disable
  sync-interval: 1

tfe:
  address: https://app.terraform.io 
  token: YOUR_TFE_TOKEN              
  organization: YOUR_ORGANIZATION    

web:
  port: 8080
  base-url: /
EOF