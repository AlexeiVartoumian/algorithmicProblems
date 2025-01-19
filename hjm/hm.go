package main

import (
    "context"
    "fmt"
    "github.com/aws/aws-sdk-go-v2/service/servicecatalogappregistry"
    "github.com/aws/aws-sdk-go-v2/service/servicecatalogappregistry/types"
    "github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func resourceAppRegistryCfnAssociation() *schema.Resource {
    return &schema.Resource{
        Create: resourceAppRegistryCfnAssociationCreate,
        Read:   resourceAppRegistryCfnAssociationRead,
        Delete: resourceAppRegistryCfnAssociationDelete,

        Schema: map[string]*schema.Schema{
            "application": {
                Type:        schema.TypeString,
                Required:    true,
                ForceNew:    true,
            },
            "stack_name": {
                Type:        schema.TypeString,
                Required:    true,
                ForceNew:    true,
            },
            // Store the returned values
            "stack_arn": {
                Type:        schema.TypeString,
                Computed:    true,
            },
        },
    }
}

func resourceAppRegistryCfnAssociationCreate(d *schema.ResourceData, m interface{}) error {
    client := m.(*servicecatalogappregistry.Client)
    
    input := &servicecatalogappregistry.AssociateResourceInput{
        Application:  aws.String(d.Get("application").(string)),
        Resource:     aws.String(d.Get("stack_name").(string)),
        ResourceType: types.ResourceTypeCfnStack,  // Using the correct enum value
        Options:     []types.AssociationOption{types.AssociationOptionApplyApplicationTag},
    }

    output, err := client.AssociateResource(context.Background(), input)
    if err != nil {
        return fmt.Errorf("error associating stack: %w", err)
    }

    // Store the returned ARN
    d.Set("stack_arn", output.ResourceArn)
    
    // Set the ID using the returned ARNs
    d.SetId(fmt.Sprintf("%s:%s", 
        aws.ToString(output.ApplicationArn), 
        aws.ToString(output.ResourceArn)))

    return nil
}

// hclCopyresource "appregistry_cfn_association" "example" {
//   application = "arn:aws:servicecatalog:eu-west-2:390746273208:/applications/07nvgtkrwb88n5h2k81iulc1l3"
//   stack_name  = "instance"
// }