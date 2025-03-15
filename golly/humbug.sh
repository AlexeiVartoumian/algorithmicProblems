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
  token:              
  organization: 

web:
  port: 8080
  base-url: /
EOF

docker run --name terraboard -p 8080:8080 \
  -v $(pwd)/config.yml:/config.yml \
  -e CONFIG_FILE="/config.yml" \
  --net terranet \
  -d \
  camptocamp/terraboard:latest