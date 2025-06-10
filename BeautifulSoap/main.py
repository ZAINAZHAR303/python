from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()


# Extracting simple HTML tags
    # soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text)


# Extracting HtML tags with Classname

    # soup = BeautifulSoup(content, 'lxml')
    # html_tags_class = soup.find_all(class_='card')
    # for course in html_tags_class:
    #     print(course.h5)
        

#Extracting specific info from HTML

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')
        # print(course_price)