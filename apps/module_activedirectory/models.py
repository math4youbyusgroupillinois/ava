from django.db import models
from ava_core.models import TimeStampedModel
from ava_core_org.models import Organisation

from django.contrib.auth.models import User
from ldap import *
import ldif, sys
from StringIO import StringIO
from ldap.cidict import cidict
#from django.core.exceptions import DoesNotExist

class ActiveDirectoryUser(TimeStampedModel):
    dn = models.CharField(max_length = 300)
    accountExpire = models.CharField(max_length = 300)
    adminCount = models.CharField(max_length = 300)
    badPasswordTime = models.CharField(max_length = 300)
    badPwdCount = models.CharField(max_length = 300)
    cn = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    displayName = models.CharField(max_length = 300)
    distinguishedName = models.CharField(max_length = 300)
    isCriticalSystemObject = models.CharField(max_length = 300)
    lastLogoff = models.CharField(max_length = 300)
    lastLogon = models.CharField(max_length = 300)
    lastLogonTimestamp = models.CharField(max_length = 300)
    logonCount = models.CharField(max_length = 300)
    logonHours = models.CharField(max_length = 300)
    name = models.CharField(max_length = 300)
    objectGUID = models.CharField(max_length = 300)
    objectSid = models.CharField(max_length = 300)
    primaryGroupID = models.CharField(max_length = 300)
    pwdLastSet = models.CharField(max_length = 300)
    sAMAccountName = models.CharField(max_length = 300)
    sAMAccountType = models.CharField(max_length = 300)
    uSNChanged = models.CharField(max_length = 300)
    uSNCreated = models.CharField(max_length = 300)
    userAccountControl = models.CharField(max_length = 300)
    whenChanged = models.CharField(max_length = 300)
    whenCreated = models.CharField(max_length = 300)
    memberOf = models.ManyToManyField('ActiveDirectoryGroup') 
    user = models.ForeignKey(User) 
    queryParameters = models.ForeignKey('QueryParameters')

    def __unicode__(self):
        return self.displayName or u''

    class Meta:
        unique_together = ('objectGUID','objectSid')

class ActiveDirectoryGroup(TimeStampedModel):
    cn = models.CharField(max_length = 300)
    distinguishedName = models.CharField(max_length = 300, unique=True)
    name = models.CharField(max_length = 100)
    objectCategory = models.CharField(max_length = 300)
    sAMAccountName = models.CharField(max_length = 300)
    objectGUID = models.CharField(max_length = 300)
    objectSid = models.CharField(max_length = 300)
    member = models.ManyToManyField('ActiveDirectoryUser')
    user = models.ForeignKey(User) 
    queryParameters = models.ForeignKey('QueryParameters')

    def __unicode__(self):
        return self.cn or u''

    class Meta:
        unique_together = ('objectGUID','objectSid')

class QueryParameters(TimeStampedModel):
    #user_dn = "cn=Administrator,cn=Users,dc=ava,dc=test,dc=domain"
    #user_pw = "Password1"
    #dump_dn = "dc=ava,dc=test,dc=domain"
    #server = 'ldap://dc.ava.test.domain'
    user_dn = models.CharField(max_length = 100, verbose_name='User')
    user_pw = models.CharField(max_length = 100, verbose_name='Password')
    dump_dn = models.CharField(max_length = 100, verbose_name='Domain')
    server = models.CharField(max_length = 100, verbose_name='Server')
    organisation = models.ForeignKey('ava_core_org.Organisation')
    user = models.ForeignKey(User, null=False)    

    def __unicode__(self):
        return self.server or u''
    
    class Meta:
        unique_together=('user','server','user_dn')

class ActiveDirectoryHelper():
    

    def getConnection(self, parameters):
        try:
            connection = initialize(parameters.server)
            print "user_dn = "+parameters.user_dn+" user_pw="+parameters.user_pw+"\n"
            connection.set_option(OPT_REFERRALS, 0)    
            connection.simple_bind_s(parameters.user_dn, parameters.user_pw)
            print (connection.whoami_s())
            return connection

        except LDAPError, e:
            if type(e.message) == dict:
                for (k, v) in e.message.iteritems():
                    sys.stderr.write("%s: %sn" % (k, v))
                    sys.stderr.write("\n")
            else:
                sys.stderr.write(e.message)
                sys.exit(1)
   
    
    def search(self, parameters, filter, attrs):
        connection = self.getConnection(parameters)
        results = connection.search_s(parameters.dump_dn, SCOPE_SUBTREE, filter,attrs)
        res = []

        if type(results) == tuple and len(results) == 2:
            (code, arr) = results
        elif type(results) == list:
            arr = results

        if len(results) == 0:
            return res

        for item in arr:
            res.append(LDAPSearchResult(item))

        ret_res = []
        for record in res:
            ret_res.append(record.to_ldif())
            #print "Test::"+record.to_ldif()

        connection.unbind()
        return res
    
    def getAll(self,parameters,user):
        print "Getting groups"
        self.getGroups(parameters,user)
        print "Getting users"
        self.getUsers(parameters,user)
        print "Getting groups"
        self.getGroups(parameters,user)

    def getGroups(self,parameters,user):
        filter = '(objectclass=group)'
        attrs = ['cn','distinguishedName','name','objectCategory','sAMAccountName','objectGUID','objectSid','member']
        results = self.search(parameters,filter,attrs)
        for  v in results:
            new_attrs = {}
            users = []
            new_attrs.update(v.get_attributes())
            for key, value in new_attrs.iteritems():
                if len(value) >  0:
                    value = ' '.join(value)
                    valid_utf8 = True
                    try:
                        value.decode('utf-8')
                    except UnicodeDecodeError:
                        valid_utf8 = False

                    if valid_utf8:
                        new_attrs[key] = value
                        if key == 'member':
                            user_cn = value.split(' CN=')
                            #print  value
                            #print  user_cn
                            #print  "************************"
                            for cn in user_cn:
                                if not cn.startswith('CN='):
                                    cn = "CN="+cn
                                #print cn
                                qs=ActiveDirectoryUser.objects.filter(user=user,queryParameters=parameters,distinguishedName=cn).first()
                                #print qs
                                if qs:
                                    users.append(qs)
                    else:
                        new_attrs[key] = self.cleanhex(value)
            
            new_attrs.pop('member',None)
            rows = ActiveDirectoryGroup.objects.filter(**new_attrs).count()
            if rows == 0:
                ad_group = ActiveDirectoryGroup.objects.create(queryParameters=parameters,user=user,**new_attrs)
                ad_group.member.add(*users)
                ad_group.save()

    def cleanhex(self,val):
        s = ['\\%02X' % ord(x) for x in val] 
        return ''.join(s)

    def getUsers(self,parameters,user):
        filter = '(objectclass=user)'
        attrs = ['dn','accountExpire','adminCount','badPasswordTime','badPwdCount','cn','description','displayName','isCriticalSystemObject','lastLogoff','lastLogon','lastLogonTimestamp','logonCount','logonHours','name','objectGUID','objectSid','primaryGroupID','pwdLastSet','sAMAccountName','sAMAccountType','uSNChanged','uSNCreated','userAccountControl','whenChanged','whenCreated','memberOf','distinguishedName']
        results = self.search(parameters,filter,attrs)
        for  v in results:
            new_attrs = {}
            groups = []
            new_attrs.update(v.get_attributes())
            for key, value in new_attrs.iteritems():
                if len(value) >  0:
                    value = ' '.join(value)
                    valid_utf8 = True
                    try:
                        value.decode('utf-8')
                    except UnicodeDecodeError:
                        valid_utf8 = False

                    if valid_utf8:
                        new_attrs[key] = value
                        if key == 'memberOf':
                            group_cn = value.split(' CN=')
                            #print  value
                            #print  "************************"
                            for cn in group_cn:
                                if not value.startswith('CN='):
                                    cn = "CN="+cn
                                #print cn
                                qs = ActiveDirectoryGroup.objects.filter(user=user,queryParameters=parameters,cn=cn).first()
                                #print qs
                                if qs:
                                    #print "goldfish"
                                    groups.append(qs)
                    else:
                        new_attrs[key] = self.cleanhex(value)
            
            new_attrs.pop('memberOf',None)
            rows = ActiveDirectoryUser.objects.filter(**new_attrs).count()
            if rows == 0:
                ad_user = ActiveDirectoryUser.objects.create(queryParameters=parameters,user=user,**new_attrs)
                ad_user.memberOf.add(*groups)
                ad_user.save()
    
    #def getFiltered(self,filter):
    #    filter = '(objectclass=group)'
    #    attrs = ['*']
    #    results = self.search(parameters,filter,attr)




class LDAPSearchResult:
    #A class to model LDAP results.
    dn = ''
    attrs = {}

    def __init__(self, entry_tuple):
        #Create a new LDAPSearchResult object.
        (dn, attrs) = entry_tuple
        if dn:
            self.dn = dn
        else:
            return
    
        self.attrs = cidict(attrs)


    def get_attributes(self):
        #Get a dictionary of all attributes.
        #get_attributes()-> {'name1': ['value1', 'value2', ...], 'name2': [value1...]}
        return self.attrs


    def set_attributes(self, attr_dict):
        #Set the list of attributes for this record.
        #The format of the dictionary should be string key, list of
        #string alues. e.g. {'cn': ['M Butcher','Matt Butcher']}
        #set_attributes(attr_dictionary)
        self.attrs = cidict(attr_dict)


    def has_attribute(self, attr_name):
        #Returns true if there is an attribute by this name in the
        #record.
        #has_attribute(attr_name)-> boolean
        return self.attrs.has_key(attr_name)


    def get_attr_values(self, key):
        #Get a list of attribute values.
        #get_attr_values(key)-> ['value1', 'value2']
        return self.attrs[key]


    def get_attr_names(self):
        #Get a list of attribute names.
        #get_attr_names()-> ['name1', 'name2', ...]
        return self.attrs.keys()


    def get_dn(self):
        #Get the DN string for the record.
        #get_dn()-> string dn
        return self.dn


    def pretty_print(self):
        #Create a nice string representation of this object.
        #pretty_print()-> string
        str = "DN: " + self.dn + "\n"
        for a, v_list in self.attrs.iteritems():
            str = str + "Name: " + a + "\n"
        for v in v_list:
            str = str + " Value: " + v + "\n"
            str = str + "========"
        return str


    def to_ldif(self):
        #Get an LDIF representation of this record.
        #to_ldif()-> string
        out = StringIO()
        ldif_out = ldif.LDIFWriter(out)

        # what's all this then?  the unparse method will currently only accept
        # a list or a dict, not a class derived from them.  self.data is a
        # cidict, so unparse barfs on it.  I've filed a bug against python-ldap,
        # but in the meantime, we have to convert to a plain old dict for printing
        newdata = {}
        if hasattr(self, 'attrs'):
            newdata.update(self.attrs)


        ldif_out.unparse(self.dn, newdata)
        return out.getvalue()


