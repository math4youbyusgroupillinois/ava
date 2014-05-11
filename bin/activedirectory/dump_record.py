# !/usr/bin/env python

import ldap, ldaphelper, sys, getpass

# user_dn = None
# user_pw = None
# dump_dn = None
user_dn = "cn=Administrator,cn=Users,dc=ava,dc=test,dc=domain"
user_pw = "Password1"
dump_dn = "dc=ava,dc=test,dc=domain"

server = 'ldap://dc.ava.test.domain'
filter = '(objectclass=user)'
#filter = ''
attrs = ['*']
#attrs = ['*']

# usage="""Usage: %s user_dn dn

# Log in as user_dn and dump the record for person dn.n""" % sys.argv[0]

# if (len(sys.argv) != 3):
#   sys.stderr.write("Error: expected user_dn and dn.n\n")
#   sys.stdout.write(usage)
#   sys.exit(1)

#   user_dn = sys.argv[1]
#   dump_dn = sys.argv[2]
#   user_pw = getpass.getpass("Password for %s:" % user_dn)
    # Add a blank line...
#   sys.stdout.write("\n")

try:
    l = ldap.initialize(server)

    try:
    #l.start_tls_s()
    
        sys.stdout.write("user_dn = "+user_dn+" user_pw="+user_pw+"\n")
        l.set_option(ldap.OPT_REFERRALS, 0)    
        l.simple_bind_s(user_dn, user_pw)
        print (l.whoami_s())
        raw_res = l.search_s(dump_dn, ldap.SCOPE_SUBTREE, filter,attrs)
    
        res = ldaphelper.get_search_results(raw_res)

        for record in res:
            sys.stdout.write(record.to_ldif())

    except ldap.INVALID_CREDENTIALS:
        print "Your username or password is incorrect."
        sys.exit()

except ldap.LDAPError, e:
    if type(e.message) == dict:
        for (k, v) in e.message.iteritems():
            sys.stderr.write("%s: %sn" % (k, v))
            sys.stderr.write("\n")
    else:
        sys.stderr.write(e.message)
        sys.exit(1)

finally:
    l.unbind()
