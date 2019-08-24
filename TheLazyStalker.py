import requests
c='Y'
while True:
    user = input("Enter the userId: ")
    url = "https://codeforces.com/api/user.info?handles="+user
    json_data = requests.get(url).json()
    data = json_data['result']
    i=data[0]
    print("Username: "+i['firstName']+' '+i['lastName'])
    print("Country: "+i['country'])
    print("City: "+i['city'])
    print("Current Rating: "+str(i['rating']))
    print("Title: "+i['rank'])
    print("Friend of "+str(i['friendOfCount'])+' '+'users')
    print("Maximum Rating: "+str(i['maxRating']))
    print("Best Title achieved: "+i['maxRank'])
    c=input("Enter your choice(Y/N): ")
    print("\n")
    if c!='Y':
        break
