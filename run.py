from zeep import Client

client = Client('https://redlink.pl/ws/v1/Soap/Contacts/Groups.asmx?WSDL')
contacts = Client('https://redlink.pl/ws/v1/Soap/Contacts/Contacts.asmx?WSDL')


def allGroups(client):
    r = client.service.GetAllGroups(strUserName ='login', strPassword ='pswd')
    return r

def deleteGroup(client,grupa):
    dg = client.service.DeleteGroup(strUserName ='login', strPassword ='pswd', strGroupId = grupa)
    print('Grupy',dg)

def deleteContacts(contacts,grupa):
    dc = contacts.service.DeleteAllContactsInGroup(strUserName ='login', strPassword ='pswd', strGroupId = grupa)
    print('Kontakty',dc)

if __name__ == '__main__':

    r = allGroups(client)

    for c in r['DataArray']['GroupData']:
        grupid = c['GroupId']
        usun_kontakty = deleteContacts(contacts,grupid)
        usun_grupy = deleteGroup(client,grupid)



