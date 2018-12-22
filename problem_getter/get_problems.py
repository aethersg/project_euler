import urllib2
from bs4 import BeautifulSoup

F = open("../README.md", "a")
for i in range(50, 51, 1):
    page = urllib2.urlopen("https://projecteuler.net/problem="+str(i))
    soup = BeautifulSoup(page, 'html.parser')
    header2 = soup.find('h2')
    problem = soup.find('h3')
    problem_statement = soup.find('div', attrs={'class': 'problem_content'})
    pt = problem.text.split()
    F.write("###" + " ".join(pt[:2]))
    F.write(":")
    F.write("\n\n")
    F.write("#####Problem Statement: ")
    F.write(header2.text)
    F.write("\n")
    F.write("```")
    en = problem_statement.text
    F.write(en.encode("utf-8"))
    F.write("```")
    F.write("\n\n")
F.close()
