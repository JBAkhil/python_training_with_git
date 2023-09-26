'''demonstration of file handling in text csv and excel files'''
import csv
import pandas as pd
from openpyxl import load_workbook
class TextFile:
    '''collection of various file handling methods'''

    def __init__(self,file_name):
        '''initialization'''
        self.file_name=file_name

    def read_file_without_context_manager(self):
        '''read a file without context manager and print its mode'''
        file=open(self.file_name,'r', encoding="utf-8")
        print(file.mode,'\nread a file with no kind of context manager!!\n')
        file.close()

    def read_file_small(self):
        '''read a small file using simple readlines'''
        with open(self.file_name,'r', encoding="utf-8") as file:
            f_content=file.readlines()
            for content in f_content:
                print(content,end='')
            print('\n\nprinted a file using readlines()\n')

    def read_file_large(self):
        '''print a large file with basic context manager'''
        size_to_read=5
        with open(self.file_name,'r', encoding="utf-8") as file:
            f_content=file.read(size_to_read)
            while len(f_content)>0: #we keep printing until we run out of content to print
                print(f_content,end='')
                f_content=file.read(size_to_read)
            print('\n\nprinted a file using read(character_length)\n')

    def make_copy_of_file(self):
        '''make a copy of a file using context manager'''
        chunk_size=1000
        with open(self.file_name,'rb', encoding="utf-8") as readf:
            with open('file_with_text_copy.txt','wb', encoding="utf-8") as writef:
                chunk=readf.read(chunk_size)
                while len(chunk)>0:
                    writef.write(chunk)
                    chunk=readf.read(chunk_size)
        print("made a copy of file_with_text")

    def write_some_text(self,file_name):
        '''write some text in a fresh file'''
        self.file_name=file_name
        with open(self.file_name,'w', encoding="utf-8") as writef:
            writef.write('this text file was made in the write_some_text method\n')
            writef.write('added another line for better understanding of write')

class CSVFile:
    '''demonstrating file handling in csv files'''

    def __init__(self,file_name):
        '''initialization'''
        self.file_name=file_name

    def simple_csv_reader(self):
        ''' csv_reader without header'''
        with open(self.file_name,'r', encoding="utf-8") as csv_file:
            csv_reader=csv.reader(csv_file)
            next(csv_reader) #to skip the first line which is usually a header in a csv file
            for line in csv_reader:
                print(line[1]) #printing the second column elements in the csv file

    def make_copy_csv(self):
        '''made a copy of the csv file'''
        with open(self.file_name,'r', encoding="utf-8") as csv_read:
            csv_reader=csv.reader(csv_read)
            with open("random_csv_data_copy.csv",'w', encoding="utf-8") as csv_write:
                csv_writer=csv.writer(csv_write,delimiter='\t')
                for line in csv_reader:
                    csv_writer.writerow(line)

    def read_as_dictionary(self):
        '''reading a csv file as a dictionary'''
        with open(self.file_name,'r', encoding="utf-8") as csv_read:
            csv_reader=csv.DictReader(csv_read)#to read as a dictionary
            with open("random_csv_data_dict_copy.csv",'w', encoding="utf-8") as csv_write:
                headline=['way','seat','loud','remain','dig']#dictionary fieldnames
                csv_writer=csv.DictWriter(csv_write,fieldnames=headline,delimiter='\t')
                csv_writer.writeheader()
                for line in csv_reader:
                    csv_writer.writerow(line)

    def csv_handling_with_pandas(self):
        '''csv file handling using pandas library'''
        dataf=pd.read_csv(self.file_name)
        #print(df.head()) to print top five rows
        #print(df.tail(3)) to print the bottom three lines
        print(dataf['way'].values)

class ExcelFile:
    '''excel file handling'''
    def __init__(self,file_name):
        '''initialization'''
        self.file_name=file_name

    def read_excel_using_openpyxl(self):
        '''using openpyxl to read excel files'''
        workb = load_workbook(self.file_name) #single workbook with 1 or many sheets
        works = workb.active
        print(works['A1'].value)

    def read_excel_using_pandas(self):
        '''using pandas to read excel'''
        pd.read_excel(self.file_name,index_col=0) #usecols="A:C" for A-C column

file_handler=TextFile('file_with_text.txt')
file_handler.read_file_without_context_manager()
file_handler.read_file_small()
file_handler.read_file_large()
file_handler.make_copy_of_file()
file_handler.write_some_text('empty_file.txt')

file_handler_csv=CSVFile('random_csv_data.csv')
file_handler_csv.simple_csv_reader()
file_handler_csv.make_copy_csv()
file_handler_csv.read_as_dictionary()
file_handler_csv.csv_handling_with_pandas()

file_handler_excel=ExcelFile('random_excel_data.xlsx')
file_handler_excel.read_excel_using_openpyxl()
file_handler_excel.read_excel_using_pandas()
