# import ldap
import ldap3
from pprint import pprint

from ldap3 import Server, Connection, ALL
server = Server('modnet.mindef.my', get_info=ALL)
# conn = Connection(server, 'uid=790322085545,ou=OU AWAM,ou=BPM,ou=KPM,dc=modnet,dc=mindef,dc=my', 'Newnewnew**1', auto_bind=True)
# conn = Connection(server, '790322085545@modnet.mindef.my', 'Newnewnew**1', auto_bind=True)
conn = Connection(server, 'eksaad@modnet.mindef.my', 'qaz@1234', auto_bind=True)
# conn = Connection(server, 'uid=790322085545,dc=modnet,dc=mindef,dc=my', 'Newnewnew**1', auto_bind=True)
print(conn.search('dc=modnet,dc=mindef,dc=my', '(objectclass=person)'))
# print(conn.entries)

for c in conn.entries:
    pprint(c)
# print(str(len(conn.entries)))
