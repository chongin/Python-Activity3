from map_api_client import MapApiClient
from route import Route

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    #orig = 'Square One Shopping Centre, City Centre Drive, Mississauga, ON'
    dest = input("Destination: ")
    if dest == "quit" or dest == "q": 
        break
    
    #dest = 'Algonquin Provincial Park, Ontario 60, Ontario'
    response = MapApiClient().get_2_location_route(orig, dest)
    if response['status'] != 0:
        print(f"API Status: {response['status']}, A fail route call: {response['error']}\n")
        continue
        
    print(f"API Status: {response['status']}, A successful route call.")
    route = Route(response['route'])
    route.display(orig, dest)
