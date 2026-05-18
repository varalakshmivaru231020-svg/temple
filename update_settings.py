from pymongo import MongoClient
client = MongoClient('mongodb+srv://rasvikas124verma_db_user:VPMolqJhzu5NO2Mt@cluster0.sqg2nyn.mongodb.net/temple_db?appName=Cluster0')
col = client['temple_db']['sitesettings']
col.update_one({'key': 'whatsapp_number'}, {'$set': {'value': '919845000000'}},  upsert=True)
col.update_one({'key': 'contact_phone'},   {'$set': {'value': '+91 98450 00000'}}, upsert=True)
for d in col.find({'key': {'$in': ['whatsapp_number','contact_phone']}}):
    print(d['key'], '=', d['value'])
client.close()
print('Done.')
