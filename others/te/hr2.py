import boto3
import json
from botocore.exceptions import ClientError
import time
import sys

def modify_default_security_groups(region=None, apply_changes=False):
    """
    Identify default security groups, print their rules, and modify them to block outbound traffic
    
    Args:
        region (str, optional): AWS region name. If None, checks all regions.
        apply_changes (bool): If True, will actually modify security groups
    
    Returns:
        tuple: (dict with results, summary message string)
    """
    # Initialize results dictionary
    results = {
        'default_security_groups': [],
        'summary': {}
    }
    
    try:
        # Get list of regions if not specified
        if not region:
            ec2_client = boto3.client('ec2')
            regions_response = ec2_client.describe_regions()
            regions = [r['RegionName'] for r in regions_response['Regions']]
        else:
            regions = [region]
        
        total_default_sgs = 0
        modified_sgs = 0
        
        # Check each region
        for reg in regions:
            try:
                ec2_client = boto3.client('ec2', region_name=reg)
                ec2_resource = boto3.resource('ec2', region_name=reg)
                
                # Get all VPCs in the region
                vpcs = list(ec2_resource.vpcs.all())
                
                for vpc in vpcs:
                    # Get security groups for this VPC
                    security_groups = list(vpc.security_groups.all())
                    
                    for sg in security_groups:
                        # Check if this is a default security group
                        if sg.group_name == 'default':
                            total_default_sgs += 1
                            
                            # Get current rules
                            inbound_rules = []
                            outbound_rules = []
                            
                            # Process inbound rules
                            for rule in sg.ip_permissions:
                                rule_desc = {
                                    'protocol': rule.get('IpProtocol', 'All'),
                                    'from_port': rule.get('FromPort', 'All'),
                                    'to_port': rule.get('ToPort', 'All'),
                                    'sources': []
                                }
                                
                                # IP ranges
                                if 'IpRanges' in rule:
                                    for ip_range in rule['IpRanges']:
                                        rule_desc['sources'].append(ip_range.get('CidrIp', 'Unknown'))
                                
                                # Security group sources
                                if 'UserIdGroupPairs' in rule:
                                    for group in rule['UserIdGroupPairs']:
                                        rule_desc['sources'].append(f"SG:{group.get('GroupId', 'Unknown')}")
                                
                                inbound_rules.append(rule_desc)
                            
                            # Process outbound rules
                            for rule in sg.ip_permissions_egress:
                                rule_desc = {
                                    'protocol': rule.get('IpProtocol', 'All'),
                                    'from_port': rule.get('FromPort', 'All'),
                                    'to_port': rule.get('ToPort', 'All'),
                                    'destinations': []
                                }
                                
                                # IP ranges
                                if 'IpRanges' in rule:
                                    for ip_range in rule['IpRanges']:
                                        rule_desc['destinations'].append(ip_range.get('CidrIp', 'Unknown'))
                                
                                # Security group destinations
                                if 'UserIdGroupPairs' in rule:
                                    for group in rule['UserIdGroupPairs']:
                                        rule_desc['destinations'].append(f"SG:{group.get('GroupId', 'Unknown')}")
                                
                                outbound_rules.append(rule_desc)
                            
                            # Check if we need to modify the outbound rules
                            needs_modification = len(outbound_rules) > 0
                            
                            # Modify the security group if needed
                            if needs_modification and apply_changes:
                                try:
                                    # First, revoke all existing outbound rules
                                    if outbound_rules:
                                        ec2_client.revoke_security_group_egress(
                                            GroupId=sg.id,
                                            IpPermissions=sg.ip_permissions_egress
                                        )
                                    
                                    # Now we don't need to add any rules, as the default with no rules is to deny all outbound traffic
                                    modified_sgs += 1
                                    
                                    # Wait a moment for changes to propagate
                                    time.sleep(0.5)
                                    
                                    # Refresh the security group
                                    sg = ec2_resource.SecurityGroup(sg.id)
                                    
                                    # Update the outbound_rules list
                                    outbound_rules = []
                                    for rule in sg.ip_permissions_egress:
                                        rule_desc = {
                                            'protocol': rule.get('IpProtocol', 'All'),
                                            'from_port': rule.get('FromPort', 'All'),
                                            'to_port': rule.get('ToPort', 'All'),
                                            'destinations': []
                                        }
                                        
                                        # IP ranges
                                        if 'IpRanges' in rule:
                                            for ip_range in rule['IpRanges']:
                                                rule_desc['destinations'].append(ip_range.get('CidrIp', 'Unknown'))
                                        
                                        # Security group destinations
                                        if 'UserIdGroupPairs' in rule:
                                            for group in rule['UserIdGroupPairs']:
                                                rule_desc['destinations'].append(f"SG:{group.get('GroupId', 'Unknown')}")
                                        
                                        outbound_rules.append(rule_desc)
                                    
                                except Exception as e:
                                    pass
                            
                            # Add information to results
                            results['default_security_groups'].append({
                                'region': reg,
                                'vpc_id': vpc.id,
                                'security_group_id': sg.id,
                                'security_group_name': sg.group_name,
                                'description': sg.description,
                                'inbound_rules': inbound_rules,
                                'outbound_rules': outbound_rules,
                                'modified': needs_modification and apply_changes
                            })
            except Exception as e:
                # If we encounter an error in a region, log it but continue with other regions
                print(f"Error processing region {reg}: {str(e)}")
        
        # Add summary
        results['summary'] = {
            'total_regions_checked': len(regions),
            'total_default_security_groups': total_default_sgs,
            'modified_security_groups': modified_sgs,
            'apply_changes': apply_changes
        }
        
        # Generate summary message
        if apply_changes:
            summary_msg = f"Modified {modified_sgs} out of {total_default_sgs} default security groups to block outbound traffic across {len(regions)} regions."
        else:
            summary_msg = f"Found {total_default_sgs} default security groups across {len(regions)} regions. Use --apply to modify them."
        
        return results, summary_msg
    
    except Exception as e:
        error_msg = f"Error processing default security groups: {str(e)}"
        return {'error': str(e)}, error_msg

def main():
    # Parse command line arguments
    apply_changes = False  # Default to not apply changes
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ['--apply', '-a', 'apply']:
            apply_changes = True
    
    # Print pretty dictionary (the shell script will capture this)
    results, summary_msg = modify_default_security_groups(apply_changes=apply_changes)
    
    # First print the full results as JSON
    print(json.dumps(results, indent=2))
    
    # End with the summary message (this will be captured by your shell script using tail -1)
    print(summary_msg)

if __name__ == "__main__":
    main()