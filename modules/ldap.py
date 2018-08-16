from django_python3_ldap.utils import format_search_filters, sync_user_relations

# def custom_format_search_filters(ldap_fields):
    # Add in simple filters.
    # ldap_fields["memberOf"] = "BPM"
    # Call the base format callable.
    # search_filters = format_search_filters(ldap_fields)
    # Advanced: apply custom LDAP filter logic.
    # search_filters.append("(|(memberOf=groupA)(memberOf=GroupB))")
    # All done!
    # return search_filters


def custom_format_search_filters(ldap_fields):
    # Add in simple filters.
    ldap_fields["objectclass"] = "person"
    # ldap_fields["groups"] = "App_Admin"
    # Call the base format callable.
    search_filters = format_search_filters(ldap_fields)
    # Advanced: apply custom LDAP filter logic.
    # search_filters.append("(|(memberOf=groupA)(memberOf=GroupB))")
    # search_filters.append("(memberOf=CN=OrganizerEKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    # search_filters.append("(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    # search_filters.append("(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my)")
    search_filters.append("(&(objectclass=person)(memberOf=CN=EKSA,OU=Groups,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my))")
    # All done!
    return search_filters


def custom_sync_user_relations(user, ldap_attributes):
	# 
	# search_filters = sync_user_relations(user, ldap_attributes)
	print(user)
	# print(ldap_attributes['memberOf'][0])
	for l in ldap_attributes['memberOf']:
		if 'CN=LeadAuditorEKSA,OU=Users,OU=BPM,OU=OU Awam,OU=KPM,DC=modnet,DC=mindef,DC=my' == l:
			print(l)
	# pass