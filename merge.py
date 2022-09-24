import csv
with open('movies.csv', errors='ignore') as f:
    reader = csv.reader(f)
    data = list(reader)
    all = data[1:]
    headers = data[0]

headers.append('poster_link')


with open('final.csv','a+', errors='ignore') as f:
    writer = csv.writer(f)
    writer.writerow(headers)


with open('movie_links.csv', errors='ignore') as f:
    reader = csv.reader(f)
    data = list(reader)
    allLinks = data[1:]

for movie_item in all:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in allLinks:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)