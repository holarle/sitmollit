def main(account):
    """Main function."""

    # Import the client library.
    from google.cloud import securitycenter

    # Create a client.
    client = securitycenter.SecurityCenterClient()

    # organization_id is the numeric ID of the organization. e.g.:
    # organization_id = "1234567777"
    organization_name = "organizations/{org_id}".format(org_id=account)

    # Call the API and print results.
    result_iterator = client.list_sources(request={"parent": organization_name})
    for result in result_iterator:
        print(result.name)

  
