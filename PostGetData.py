from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix",
                      "Z7fxGuyYLzsOyfpC5AtOptOceTInWeOYwvk3fCZJ7jr_",
                      url="https://bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()


def PostData(data):
    data = {
        "data": {
            'double': data
        }
    }

    DataBase_Name = "hackisu-2019"
    My_DataBase = client['hackisu-2019']
    my_document = My_DataBase.create_document(data)
    if my_document.exists():
        print(f"'{DataBase_Name}' successfully created.")
    else:
        print("oof")

    session = client.session()
    client.disconnect()
