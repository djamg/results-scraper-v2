import requests
from bs4 import BeautifulSoup


def loaded(url):
    lst = []
    page = url
    soup = BeautifulSoup(page, 'lxml')
    selectionForSoup = soup.select('tbody tr')
    for elements in selectionForSoup:
        for x in elements.find_all('td')[10]:
            lst.append(x.text)
            # print(x.text)

        # print(elements.text)
    # print(selectionForSoup[3].find('td').text)
    print(lst)
    resultCheck(lst)


def resultCheck(lst):
    if "F" in lst:
        print("You have failed :( Better Luck Next TIME!")
    else:
        print("Congrats! You have cleared everything!")


# for head in soup.select('thead tr'):
#     row_text = [x.text for x in head.find_all('th')]
#     print(', '.join(row_text))

# for row in soup.select('tbody tr'):
#     row_text = [x.text for x in row.find_all('td')]
#     print(', '.join(row_text))
