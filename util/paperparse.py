import csv
import sys
def genPubs(reader):
    next(reader)
    publications = ""
    for row in reader:
        title = "- title: \'" + row[1] + "\'\n"
        authors = "  authors: " + row[2] + "\n"
        conf = "  in: " + row[5] + "\n"
        links = ""
        if row[6] != "":
            links = "  links:\n"
            row[6] = row[6].replace("\n", "") # one of the entries has a newline in the middle of it
                                              # this solution is a bit of a hack
            csv_links = csv.reader(row[6:])
            for link_list in csv_links:
                for link in link_list:
                    links += "    - url: " + link + "\n"
        paper = title + authors + links + conf + "\n"
        publications += paper
    return publications

if __name__ == "__main__":
    with open(sys.argv[1], 'rU') as csv_file:
        reader = csv.reader(csv_file)
        final_yaml = genPubs(reader)

    output_file = open("publications.yaml", "w")
    output_file.write(final_yaml)
    output_file.close()

