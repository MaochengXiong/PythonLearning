from book import *
import json
class Library:

    # global library 
    # library = []
    def __init__(self):
        global library
        library = Library.readFile(self)
        pass
    
    def readFile(self):
        # print("in")
        with open(r"C:\Users\Sean\Desktop\NandPtest\libraryL\library.json",'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            return json_data    

    def saveFile(self, file):
        with open(r"C:\Users\Sean\Desktop\NandPtest\libraryL\library.json",'w+', encoding='utf8') as fp:
            json.dump(file, fp, ensure_ascii=False)

    def addBook(self, a):
        # print("in+",a)
        library.append(a)
        Library.saveFile(self, library)
        # print(library)

    def processBook(self, name, number):
        book = {"name":name,"number": number, "remain":number}
        a = False
        # print(library,name,number)
        for i in range(len(library)):
            # print(library)
            if (library[i]["name"] == name):
                a = True
                # print(library[i]["number"])
                library[i]["number"]=library[i]["number"]+1
                library[i]["remain"]=library[i]["remain"]+1
                # print("new:", library[i]["number"])
                Library.saveFile(self, library)
        if(a==False):
            Library.addBook(self,book)

    def createBook(self,name,number):        
        Library.processBook(self,name,number)

    def canBorrow (self,name):
        for i in range(len(library)):
            if((library[i]["name"] == name) and (library[i]["remain"]>0)):
                return True
        return False
    
    def borrow(self, name):
        if (Library.canBorrow(self,name) == True):
            for i in range(len(library)):
                if (library[i]["name"] == name):
                    library[i]["remain"]=library[i]["remain"]-1
                    Library.saveFile(self, library)
        else:
            print ("There is no", name, "remaining!")

    def returnBook(self, name):
        for i in range(len(library)):
            if (library[i]["name"] == name):
                temp = library[i]["remain"]
                if(temp >= library[i]["number"]):
                    print("Some books do not belong here!")
                else:
                    library[i]["remain"] = temp+1
                    Library.saveFile(self, library)        






    
        

    


