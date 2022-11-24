from from_json import read_json

def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    users=data['users']
    ans=0
    for i in users:
        if i['gender']=='male':
            ans+=1
    
    return ans
    # return data

data=read_json('users.json')
print(get_male_users(data))