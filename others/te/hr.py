import boto3
import json
from botocore.exceptions import ClientError
import time

def modify_default_security_groups(region=None, dry_run=True):
    """
    Identify default security groups, print their rules, and modify them to block outbound traffic
    
    Args:
        region (str, optional): AWS region name. If None, checks all regions.
        dry_run (bool): If True, only shows what would be done without making changes.
    
    Returns:
        dict: Information about default security groups and modifications
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
            print(f"Checking region: {reg}")
            ec2_client = boto3.client('ec2', region_name=reg)
            ec2_resource = boto3.resource('ec2', region_name=reg)
            
            # Get all VPCs in the region
            vpcs = list(ec2_resource.vpcs.all())
            
            for vpc in vpcs:
                print(f"  Checking VPC: {vpc.id}")
                # Get security groups for this VPC
                security_groups = list(vpc.security_groups.all())
                
                for sg in security_groups:
                    # Check if this is a default security group
                    if sg.group_name == 'default':
                        total_default_sgs += 1
                        print(f"    Found default security group: {sg.id}")
                        
                        # Get current rules
                        inbound_rules = []
                        outbound_rules = []
                        
                        # Process inbound rules
                        print("      Inbound rules:")
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
                            
                            # Print the rule
                            protocol = rule.get('IpProtocol', 'All')
                            from_port = rule.get('FromPort', 'All')
                            to_port = rule.get('ToPort', 'All')
                            
                            if protocol == '-1':
                                protocol_display = 'All Traffic'
                                port_display = 'All'
                            else:
                                protocol_display = protocol
                                if from_port == to_port:
                                    port_display = from_port
                                else:
                                    port_display = f"{from_port}-{to_port}"
                            
                            sources = []
                            if 'IpRanges' in rule:
                                for ip_range in rule['IpRanges']:
                                    sources.append(ip_range.get('CidrIp', 'Unknown'))
                            
                            if 'UserIdGroupPairs' in rule:
                                for group in rule['UserIdGroupPairs']:
                                    sources.append(f"SG:{group.get('GroupId', 'Unknown')}")
                            
                            source_display = ', '.join(sources) if sources else 'None'
                            
                            print(f"        {protocol_display} {port_display} from {source_display}")
                        
                        # Process outbound rules
                        print("      Outbound rules:")
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
                            
                            # Print the rule
                            protocol = rule.get('IpProtocol', 'All')
                            from_port = rule.get('FromPort', 'All')
                            to_port = rule.get('ToPort', 'All')
                            
                            if protocol == '-1':
                                protocol_display = 'All Traffic'
                                port_display = 'All'
                            else:
                                protocol_display = protocol
                                if from_port == to_port:
                                    port_display = from_port
                                else:
                                    port_display = f"{from_port}-{to_port}"
                            
                            destinations = []
                            if 'IpRanges' in rule:
                                for ip_range in rule['IpRanges']:
                                    destinations.append(ip_range.get('CidrIp', 'Unknown'))
                            
                            if 'UserIdGroupPairs' in rule:
                                for group in rule['UserIdGroupPairs']:
                                    destinations.append(f"SG:{group.get('GroupId', 'Unknown')}")
                            
                            destination_display = ', '.join(destinations) if destinations else 'None'
                            
                            print(f"        {protocol_display} {port_display} to {destination_display}")
                        
                        # Check if we need to modify the outbound rules
                        needs_modification = False
                        
                        if not outbound_rules:
                            print("      No outbound rules to modify.")
                        else:
                            needs_modification = True
                        
                        # Modify the security group if needed
                        if needs_modification and not dry_run:
                            try:
                                print(f"      Modifying outbound rules to block all traffic...")
                                
                                # First, revoke all existing outbound rules
                                if outbound_rules:
                                    ec2_client.revoke_security_group_egress(
                                        GroupId=sg.id,
                                        IpPermissions=sg.ip_permissions_egress
                                    )
                                
                                # Now we don't need to add any rules, as the default with no rules is to deny all outbound traffic
                                print("      Successfully modified outbound rules.")
                                modified_sgs += 1
                                
                                # Wait a moment for changes to propagate
                                time.sleep(1)
                                
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
                                print(f"      Error modifying outbound rules: {str(e)}")
                        elif needs_modification and dry_run:
                            print("      Would modify outbound rules (dry run)")
                        
                        # Add information to results
                        results['default_security_groups'].append({
                            'region': reg,
                            'vpc_id': vpc.id,
                            'security_group_id': sg.id,
                            'security_group_name': sg.group_name,
                            'description': sg.description,
                            'inbound_rules': inbound_rules,
                            'outbound_rules': outbound_rules,
                            'modified': needs_modification and not dry_run
                        })
        
        # Add summary
        results['summary'] = {
            'total_regions_checked': len(regions),
            'total_default_security_groups': total_default_sgs,
            'modified_security_groups': modified_sgs,
            'dry_run': dry_run
        }
        
        return results
    
    except Exception as e:
        print(f"Error processing default security groups: {str(e)}")
        return {'error': str(e)}

def main():
    # Initially do a dry run to see what would be changed
    print("Checking default security groups across all regions (DRY RUN)...")
    print("This will only show what would be modified, but won't make any changes.")
    print()
    
    dry_run_results = modify_default_security_groups(dry_run=True)
    
    # Save full dry run results to file
    with open('default_sg_dry_run.json', 'w') as f:
        json.dump(dry_run_results, f, indent=2)
    
    # Print summary
    summary = dry_run_results['summary']
    print("\nDry Run Summary:")
    print(f"Regions checked: {summary['total_regions_checked']}")
    print(f"Total default security groups found: {summary['total_default_security_groups']}")
    print(f"Security groups that would be modified: {summary['total_default_security_groups']}")
    
    # Ask for confirmation before making actual changes
    proceed = input("\nDo you want to proceed with modifying these security groups? (yes/no): ")
    
    if proceed.lower() == 'yes':
        print("\nProceeding with actual modifications...")
        results = modify_default_security_groups(dry_run=False)
        
        # Save full results to file
        with open('default_sg_modifications.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        # Print summary
        summary = results['summary']
        print("\nFinal Summary:")
        print(f"Regions checked: {summary['total_regions_checked']}")
        print(f"Total default security groups found: {summary['total_default_security_groups']}")
        print(f"Security groups successfully modified: {summary['modified_security_groups']}")
        print("\nDetailed results saved to default_sg_modifications.json")
    else:
        print("\nNo changes were made. Exiting.")

if __name__ == "__main__":
    main()