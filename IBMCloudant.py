from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam("bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix",
                      "Z7fxGuyYLzsOyfpC5AtOptOceTInWeOYwvk3fCZJ7jr_",
                      url="https://bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "HackISUDataBase"
mydata = client['hackisu-2019']
result = Result(mydata.all_docs)
print("Retrieved minimal document:\n{0}\n".format(result[0]) + " :::: happened")

# response = client.r_session.get(end_point, params=params)
# print("{0}\n".format(response.json()))

session = client.session()
print(session)
client.disconnect()


def PostCaller(data):
    PostData(data)


def PostData(data):
    data = {
        "data": {
            'double': data
        }
    }
    client = Cloudant.iam("bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix",
                          "Z7fxGuyYLzsOyfpC5AtOptOceTInWeOYwvk3fCZJ7jr_",
                          url="https://bfa69c17-0655-41d3-80ed-0ad99818ba28-bluemix.cloudantnosqldb.appdomain.cloud")
    client.connect()
    DataBase_Name = "hackisu-2019"
    My_DataBase = client['hackisu-2019']
    my_document = My_DataBase.create_document(data)

    if my_document.exists():
        print(f"'{DataBase_Name}' successfully created.")
    else:
        print("oof")

    session = client.session()
    client.disconnect()
