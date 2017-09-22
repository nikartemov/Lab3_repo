from UserId import IdFromUsername
from Friends import Friends
from datetime import datetime

user = IdFromUsername('w8_us')
user_id = user.execute()

friends_client = Friends(user_id)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))

#b_date = datetime.strptime('22.9.2016', "%d.%m.%Y")
#n_date = datetime.now()
#print(int((n_date - b_date).))