from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import a

def getList(movieList):
	title = []
	j = 0
	for i in movieList[:20]:
		div = i.find('div',attrs={'class':'lister-item-content'})
		title.append(div.h3.a.string)

		print (str(j+1) + '.' + title[j])
		j +=1
	return title


def getName(title, name):
	#name = input('Enter Movie:')
	flag = 0

	index = 0
	while(True):
		for i in title:
			if(i.lower()==name.lower()):
				flag = 1
				index = title.index(i)
				break

		if (flag==0):
			name = input('Enter correct movie:')
		else:
			break
	return index

def getGenre(movieList,index):
	div = movieList[index]
	content = div.find('div',attrs={'class':'lister-item-content'})
	genre = content.find('span', class_='genre').string
	return genre

def getRating(movieList,index):
	div = movieList[index]
	content = div.find('div',attrs={'class':'lister-item-content'})
	rating = content.find('div', class_='ratings-imdb-rating')["data-value"]
	return rating

def printResult(name,genre,rating):
	print('Movie: ' + name.title())
	print('Genre: ' + genre.strip())
	print('Rating: ' + rating)





year = int(input("Enter the year for which you want the movie (YYYY)"))
end_year = year+1
myurl = 'https://www.imdb.com/search/title?release_date='+str(year)+','+str(end_year)+'&title_type=feature'

#opening up connection, grabbing the page
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
movieList = page_soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

title = getList(movieList)

name = input('Enter Movie:')

index = getName(title,name)
genre = getGenre(movieList,index)
rating = getRating(movieList,index)

printResult(name,genre,rating)


"""title = []
j = 0
for i in movieList[:20]:
	div = i.find('div',attrs={'class':'lister-item-content'})
	title.append(div.h3.a.string)

	print (str(j+1) + '.' + title[j])
	j +=1

name = input('Enter Movie:')

flag = 0

index = 0
while(True):
	for i in title:
		if(i.lower()==name.lower()):
			flag = 1
			index = title.index(i)
			break

	if (flag==0):
		name = input('Enter correct movie:')
	else:
		break


div = movieList[index]
content = div.find('div',attrs={'class':'lister-item-content'})

genre = content.find('span', class_='genre').string
print (genre)

#rating = content.find('div', class_='ratings-imdb-rating').strong.string
rating = content.find('div', class_='ratings-imdb-rating')["data-value"]
print (rating)

"""


