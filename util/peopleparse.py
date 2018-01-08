import csv
import sys

'''
KNOWN ISSUES:
Doesn't Remove newlines
Doesn't check for empty fields
Doesn't sanitize student type input
Doesn't sanitize imgur input (needs https)
'''

if __name__ == "__main__":
    csv_file = open(sys.argv[1], 'rU')
    people = csv.reader(csv_file)
    next(people)
    for person in people:
        markdown_name = ''.join(person[1].split())
        new_md = open("_people/" + markdown_name + ".md", 'w')
        new_md.write('---' + "\n")
        new_md.write("title: " + person[1] + " - Robot Learning Lab" + "\n")
        new_md.write("name: " + person[1] + "\n")
        new_md.write("bio: " + person[2] + "\n")
        new_md.write("picture: " + person[3] + "\n")
        new_md.write("github: " + person[5] + "\n")
        new_md.write("personal_site: " + person[6] + "\n")
        new_md.write("email: " + person[10] + "\n")
        new_md.write("layout: person" + "\n")
        new_md.write("type: " + person[9] + "\n")
        new_md.write("---" + "\n")
        print ''.join(person[1].split())


