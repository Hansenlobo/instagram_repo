
import instaloader
import xlsxwriter
import urllib.request
L = instaloader.Instaloader()


username = ""
password = ""
L.login(username, password) 

# user 1
profile = instaloader.Profile.from_username(L.context,"username1")

follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("user1followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    count = count + 1
print(follow_list)

# user 2
profile2 = instaloader.Profile.from_username(L.context,"username2")

follow_list1 = []
count = 0
for followee in profile2.get_followers():
    follow_list1.append(followee.username)
    file = open("user2followers.txt", "a+")
    file.write(follow_list1[count])
    file.write("\n")
    file.close()
    count = count + 1


print(follow_list1)

print("====================================")
# find mutuals
list1_as_set = set(follow_list)
intersection = list1_as_set.intersection(follow_list1)


intersection_as_list = list(intersection)

print(intersection_as_list)



# write into excel and download images

loader = instaloader.Instaloader()
workbook = xlsxwriter.Workbook('details.xlsx')

loader.login(username,password)
worksheet = workbook.add_worksheet()

list_profile=intersection_as_list
count=0
for i in list_profile:
    profile = instaloader.Profile.from_username(loader.context,i)
    profile_pic = profile.profile_pic_url

    worksheet.write('A'+str(count), i)
    worksheet.write('B'+str(count), profile_pic)
    count+=1
    urllib.request.urlretrieve(profile_pic, "images/"+i+".jpg")
    print(count)

workbook.close()
