from number_list import *
import _thread
import random
import time
import os.path
from os import path


def create(phone_list,select_int):
    f.write(phone_list[select_int]())
    f.write('\n')
    return


file_n = "number.txt"
path_number = "phone_number/"
if not os.path.isdir(path_number):
    os.mkdir(path_number)

phone_list = [french,belgium,swiss,netherland,germany,spain,uae,uk,sweden,norway,finland,denmark,austria,australia,saoudi_arabia,qatar]
file_list = ["french","belgium","swiss","netherland","germany","spain","uae","uk","sweden","norway","finland","denmark","austria","australia","saoudi_arabia","qatar"]

select = str(input("\nCountry:\n 1.France\n 2.Belgium \n 3.Swiss \n 4.pays bas \n 5.allemagne \n 6.espagne \n 7.emirates arab united \n 8.united kingdom \n 9.suede \n 10.norvege \n 11.finlande \n 12.danemark \n 13.autriche \n 14.australie \n 15.arabie saoudite \n 16.qatar \n"))
select_int = int(select)-1
number = int(input("How many: "))

start_time = time.time()

file_n = path_number + file_list[select_int] +  "_" + file_n
f = open(file_n, "w")
for n in range(number):
    _thread.start_new_thread(create, (phone_list, select_int))


duration = time.time() - start_time
print(number, " numbers created for country :", select, "in", duration, "seconds")
print("created ", number/duration , " per second", )


f.close()
