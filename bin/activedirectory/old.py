import ldap
# from ldap.controls import SimplePagedResultsControl
import sys
# import ldap.modlist as modlist

LDAP_SERVER = "ldaps://dc.ava.test.domain"
BIND_DN = "Administrator@ava.test.domain"
BIND_PASS = "Password1"
USER_FILTER = "(&(objectClass=person)(primaryGroupID=7235))"
USER_BASE = "ou=Special Peeps,ou=My Users,dc=host,dc=com"
PAGE_SIZE = 10

#  LDAP connection
try:
    print "start"
#   ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
    print "success 1"
    ldap_connection = ldap.initialize(LDAP_SERVER)
    print "success 2"
    ldap_connection.simple_bind_s(BIND_DN, BIND_PASS)
    print "success 3"
except:
# except ldap.LDAPError, e:
    #sys.stderr.write('Error connecting to LDAP server: ' + str(e) + '\n')
    print "bugger"
    sys.exit(1)

#  Lookup usernames from LDAP via paged search
# paged_results_control = SimplePagedResultsControl(
#   ldap.LDAP_CONTROL_PAGE_OID, True, (PAGE_SIZE, ''))
# accounts = []
# pages = 0
# while True:
#   serverctrls = [paged_results_control]
#   try:
#       msgid = ldap_connection.search_ext(USER_BASE,
#                                          ldap.SCOPE_ONELEVEL,
#                                          USER_FILTER,
#                                          attrlist=['employeeID',
#                                                    'sAMAccountName'],
#                                          serverctrls=serverctrls)
#   except ldap.LDAPError, e:
#       sys.stderr.write('Error performing user paged search: ' +
#                        str(e) + '\n')
#       sys.exit(1)
#   try:
#       unused_code, results, unused_msgid, serverctrls = \
#                  ldap_connection.result3(msgid)
#   except ldap.LDAPError, e:
#       sys.stderr.write('Error getting user paged search results: ' +
#                        str(e) + '\n')
#       sys.exit(1)
#   for result in results:
#       pages += 1
#       accounts.append(result)
#   cookie = None
#   for serverctrl in serverctrls:
 #     if serverctrl.controlType == ldap.LDAP_CONTROL_PAGE_OID:
#           unused_est, cookie = serverctrl.controlValue
#           if cookie:
#             paged_results_control.controlValue = (PAGE_SIZE, cookie)
#           break
#   if not cookie:
#       break

#  LDAP unbind
# ldap_connection.unbind_s()

#  Make dictionary with user data
# user_map = {}
# for entry in accounts:
#   if entry[1].has_key('employeeID') and \
#     entry[1].has_key('sAMAccountName'):
#       user_map[entry[1]['employeeID'][0]] = entry[1]['sAMAccountName'][0]



