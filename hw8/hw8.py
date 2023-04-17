from datetime import datetime, timedelta


def get_birthdays_per_week(users:list):
    week_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    data_week_days = {i:None for i in week_days.values()}
    resalt = {i:[] for i in week_days.values()}
    num_today = datetime.now().weekday()         

    for i in range(7):
        if 0 <= num_today - i :
            #print(week_days[num_today-i])
            key = week_days[num_today-i]
            value = datetime.now().date() - timedelta(days=i)
            data_week_days[key] = value

        elif num_today + (i-num_today) <= 6:
            #print(week_days[num_today + (i-num_today)])
            key = week_days[num_today + (i - num_today)]
            value = datetime.now().date() + timedelta(days=(i - num_today))
            data_week_days[key] = value


    for user in users:
        
        
        if user['birthday'].date() == (data_week_days['Monday'] - timedelta(2)) or user['birthday'].date() == (data_week_days['Monday'] - timedelta(1)):
            resalt['Monday'].append(user['name'])
        elif user['birthday'].date() == data_week_days['Friday']:
            resalt['Friday'].append(user['name'])

        elif user['birthday'].date() == data_week_days['Monday']:
            resalt['Monday'].append(user['name'])

        elif user['birthday'].date() == data_week_days['Tuesday']:
            resalt['Tuesday'].append(user['name'])
        
        elif user['birthday'].date() == data_week_days['Wednesday']:
            resalt['Wednesday'].append(user['name'])

        elif user['birthday'].date() == data_week_days['Thursday']:
            resalt['Thursday'].append(user['name'])

    for day, name_lisr in resalt.items():
        if name_lisr:
            print(f'{day}: {", ".join(name_lisr)}')
            
                    
                
            

    
        
        
                

    


        


        
            
    

   

    

    
        







users = [{'name': f'name{i}', 'birthday': datetime(year=2023, month=4, day=i)} for i in range(12, 30) ]
#print(users)
users.append({'name': f'name{50}', 'birthday': datetime(year=2023, month=4, day=17)})
get_birthdays_per_week(users)

