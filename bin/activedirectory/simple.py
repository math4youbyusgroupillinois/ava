import ldap
import sys
con = ldap.initialize('ldap://dc.ava.test.domain') 
user_dn="Administrator"
user_pw="Password1"

try:
  con.bind_s(user_dn, user_pw)
#  con.start_tls_s()
except ldap.INVALID_CREDENTIALS:
  print "Your username or password is incorrect."
  sys.exit()
except ldap.LDAPError, e:
  if type(e.message) == dict and e.message.has_key('desc'):
    print e.message['desc']
  else: 
    print e
    sys.exit()

