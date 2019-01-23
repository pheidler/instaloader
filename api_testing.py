'''
First input: Username and Password for Instagram
Logs in to instagram, requests second input
Second input: Hashtag and number of posts (with max)
'''

import instaloader

#gets instance of instaloader
L = instaloader.Instaloader()

#CODE THAT ASKS FOR USERNAME AND PASSWORD:

#logs in with said username and password
#L.interactive_login("pete_heidler")
locationList = []
posts = L.get_hashtag_posts("materialmelttest")

for post in posts:
	#test = post.location.name
	#locationList.append(test)
	#print(type(test))
	try:
		locationList.append(post.location.name)
	except AttributeError:
		break

	#L.download_post(post, target='#materialmelttest')

print(locationList)
#for post in L.get_hashtag_posts('materialmelttest'):
#	L.download_post(post, target='#materialme')
