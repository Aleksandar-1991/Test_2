current_dict = {"soapenv:Envelope": {"@xmlns:soapenv": "http://schemas.xmlsoap.org/soap/envelope/", "@xmlns:mat": "http://matter.ws.chromeriver.com/", "soapenv:Header": {"mat:credentials": {"token": "?", "user": {"companyId": "?", "userId": "?", "password": "?"}}}, "soapenv:Body": {"mat:inMatterCreate": {"matterNumber": "?", "clientNumber": "?", "clientName": "?", "parentClientNumber": "?", "matterName": "?", "type": "?", "routeIndependent": "true", "closedDate": "?", "GLAccount": "?", "entity1": "?", "entity2": "?", "entity3": "?", "languageCode": "?", "currencyCode": "?", "UDF1": "?", "UDF2": "?", "UDF3": "?", "UDF4": "?", "UDF1PersonUniqueID": "?", "UDF2PersonUniqueID": "?", "UDF3PersonUniqueID": "?", "extraLineItemData1LegalValues": "?", "onSelect1EntityTypeCode": "?", "onSelect2EntityTypeCode": "?", "isBillable": "?"}}}}

mapper = {
    "matterNumber": "allocationNumber",
    "clientNumber": "clientNumber",
    "clientName": "clientName",
    "matterName": "allocationName",
    "type": "type",
    "Bkzkp": None
}

new_dict = {}
for key_name in mapper.keys():
    if key_name in current_dict["soapenv:Envelope"]['soapenv:Body']['mat:inMatterCreate'].keys():
        new_dict.update({key_name: current_dict["soapenv:Envelope"]['soapenv:Body']['mat:inMatterCreate'][key_name]})

print(new_dict)
# print(current_dict["soapenv:Envelope"]['soapenv:Body']['mat:inMatterCreate'])

