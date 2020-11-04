class Tex_file():
    def __init__(self, doc_class):
        self.packages=["geometry"]
        self.doc_class=doc_class
        print(self)

    def create(self, filename, coding="utf8"):     #creating the output file
        with open("{}.tex".format(filename), "w") as f:
            f.write("\\documentclass{{{}}}\n".format(self.doc_class))           
            f.write("\\usepackage[{}]{{inputenc}}\n".format(coding))      #neeeded stuffs
            for i in self.packages:     #used packaages to the beggining of the file
                f.write("\\usepackage{{{}}}\n".format(i))
        

            f.write("\\begin{document}\n")
            f.write("{}\n".format("dsfasd"))
            f.write("\\end{document}\n")

if __name__ == '__main__':
    trial=Tex_file("article")
    trial.create('trial')


