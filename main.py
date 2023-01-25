import os
import time
import pickle
import csv
from hashlib import sha256
os.system('color A')





# gets the password input from the user and returns True(if the password is correct) or returns False(if the password is incorrect)
def login():
    f = open('login.bin', 'rb')
    root_pass = pickle.load(f)
    f.close()
    if sha256(input('enter the root password : ').encode()).hexdigest() == root_pass:
        print('ACCESS GRANTED')
        time.sleep(1)
        return True
    else:
        os.system('color C')
        print("ACCESS DENIED")
        time.sleep(1)
        os.system('color A')
        return False
# gets the input(new password) and updates the password login.bin file
def change_pass():
    f = open('login.bin', 'wb')
    data = sha256(input('enter the root password : ').encode()).hexdigest()
    pickle.dump(data, f)
    f.close()
    return True

# dashboard that will get displayed after the user has successfully logged in
def main():
    print('WELCOME TO PERSONAL EXPENSE!')
    choice = input('1. log\n2. get report\n3. view raw data\n4. refresh\n5. change password\n6. logout\n >>')
    if choice == '1':
        exp()
    elif choice == '2':
        get_report()
    elif choice == '3':
        for i in get_all_data():
            print(i)
        input('')
    elif choice == '4':
        os.system('python init.py')
    elif choice == '5':
        change_pass()
    elif choice == '6':
        exit()
    else:
        os.system('color C')
        print('invalid input...')
        time.sleep(1)
        os.system('color A')


# a function that return a nested list containing all the rows in the csv file
def get_all_data():
    f = open('data.csv', 'r')
    content = list(csv.reader(f))
    f.close()
    return content


def return_data(data):
    old_content = get_all_data()
    old_content.extend([data])
    f = open('data.csv', 'w')
    obj = csv.writer(f)
    obj.writerows(old_content)
    f.close()
    return True



def exp():
    old_balance = int(get_all_data()[-2][-1])
    structure = {
        "personal" : ['snacks', 'education', 'manditiory', 'occational purchase', 'monthly', 'medical', 'stationary', 'subscription', 'clothing', 'transport'],
        "income" : ["dad", 'mom', 'friends', 'others'],
        "lend in" : ['get', "return"],
        "lend out" : ['give', "return"],
        "others" : ["none"],
        "home" : ["none"]
    }
    general = []
    general.append(time.ctime(time.time())[8:10] + '-' + time.ctime(time.time())[4:7] + '-' + time.ctime(time.time())[-4:])
    general.append(input('from? '))
    general.append(input('to? '))
    if "sanjiv_kannaa_jeganathan" == general[1]:
        balance_char = -1
    elif "sanjiv_kannaa_jeganathan" == general[2]:
        balance_char = 1
    else:
        balance_char = 0
    first_trans_no = int(get_all_data()[-2][0]) + 1
    for i in range(int(input('enter the no of transactions'))):
        data = list(general)
        data.insert(0, str(first_trans_no + i))
        data.append(input('category[personal/income/lend in/lend out/others/home] : '))
        if data[4] == "personal":
            data.append(input('sub category[snacks/education/manditory/occational purchase/monthly/medical/stationary/subscription/clothing/transport] : '))
        elif data[4] == "income":
            data.append(input('sub category[dad/mom/friends/others] : '))
        elif data[4] == "lend in":
            data.append(input('sub category[get/return] : '))
        elif data[4] == "lend out":
            data.append(input('sub category[give/return] : '))
        elif data[4] == "others":
            data.append('none')
        elif data[4] == "home":
            data.append('none')
        else:
            os.system('color C')
            print('failed category tests')
            os.system('color A')
        #try:
        just_a_try_to_see_exist_in_structure = structure[data[4]]
        #except:
        #    os.system('color C')
        #    print('sub category tests failed')
        #    os.system('color A')
        #    exp()
        data.append(input('description : '))
        data.append(input('type[cash/bank_1] : '))
        if data[7] == 'cash':
            data.append('none')
        else:
            data.append('type_description[card/online banking/cheque/other] : ')
        data.append(input('amount : '))
        try:
            amount = int(data[9])
        except:
            main()
        data.append(input('can it be avoided?[yes/no/maybe/NA]  '))
        if data[-1] in ['yes', 'no', 'maybe', 'NA']:
            pass
        else:
            main()
        try:
            if balance_char != 0:
                balance = balance + (amount*balance_char)
                data.append(str(balance))
            else:
                data.append(old_balance)
        except:
            if balance_char != 0 :
                balance = old_balance + (amount*balance_char)
                data.append(str(balance))
            else:
                data.append(old_balance)
        return_data(data)







def get_report():
    print('sort by \n1. date\n2. avoidition\n3. category\n4. description\n5. amount\n6. type')
    ch1 = input('  >>')
    if ch1 == '1':
        report_date()
    elif ch1 == '2':
        report_avoidition()
    elif ch1 == '3':
        report_category()
    elif ch1 == '4':
        report_description()
    elif ch1 == '5':
        report_amount()
    elif ch1 == '6':
        report_type()
    else:
        os.system('color C')
        print('invalid input')
        os.system('color A')




def report_date():
    from_ = input('enter the start date[1-apr-2021] : ')
    to_ = input('enter the end date[30-apr-2021] : ')
    content = get_all_data()
    final = content

def report_avoidition():
    try:
        avoidition_status = input('enter the type of avolidition[yes/no/maybe/NA] : ')
        content = list(get_all_data())
        final = []
        for i in content:
            try:
                if i[-2] == avoidition_status:
                    final.append(i)
            except:
                pass
        for i in final:
            print(i)
        sum = 0
        count = 0
        for i in final:
            count += 1
            sum += int(i[-3])
        final_line = 'total number of records : ' + str(count) + '\n' + 'total amount spend on this selection : ' + str(sum)
        print(final_line)
        input('')
    except:
        os.system('color C')
        print('error occoured')
        time.sleep(1)
        os.system('color A')
        main()

def report_category():
    try:
        content = list(get_all_data())
        final = []
        category = input('enter the catrgory[personal/income/lend in/lend out/others/home] : ')
        if category == "personal":
            sub_category = input('sub category[snacks/education/manditory/occational purchase/monthly/medical/stationary/subscription/clothing/transport] : ')
        elif category == "income":
            sub_category = input('sub category[dad/mom/friends/others] : ')
        elif category == "lend in":
            sub_category = input('sub category[get/return] : ')
        elif category == "lend out":
            sub_category = input('sub category[give/return] : ')
        elif category == "others":
            sub_category = 'none'
        elif category == "home":
            sub_category = 'none'
        else:
            sub_category = ''
        if sub_category == "":
            for i in content:
                try:
                    if i[4] == category:
                        final.append(i)
                except:
                    pass
        else:
            for i in content:
                try:
                    if i[4] == category and i[5] == sub_category:
                        final.append(i)
                except:
                    pass
        for i in final:
            print(i)
        sum = 0
        count = 0
        for i in final:
            count += 1
            sum += int(i[-3])
        final_line = 'total number of records : ' + str(count) + '\n' + 'total amount spend on this selection : ' + str(sum)
        print(final_line)
        input('')
    except:
        os.system('color C')
        print('error occoured')
        time.sleep(1)
        os.system('color A')
        main()

def report_description():
    try:
        content = list(get_all_data())
        final = []
        description = input('enter the description/keyword : ')
        for i in content:
            try:
                if description in str(i[6]):
                    final.append(i)
            except:
                pass
        for i in final:
            print(i)
        sum = 0
        count = 0
        for i in final:
            count += 1
            sum += int(i[-3])
        final_line = 'total number of records : ' + str(count) + '\n' + 'total amount spend on this selection : ' + str(sum)
        print(final_line)
        input('')
    except:
        os.system('color C')
        print('error occoured')
        os.system('color A')
        main()

def report_amount():
    lower_limit = input('enter the lower limit : ')
    upper_limit = input("enter the upper limit : ")
    try:
        check = int(lower_limit)
        check = int(upper_limit)
        del check
    except:
        os.system('color C')
        print('error occoured')
        time.sleep(1)
        os.system('color A')
        main()
    content = list(get_all_data())
    final = []
    try:
        for i in content:
            try:
                if int(i[-3])>int(lower_limit) and int(i[-3])<int(upper_limit):
                    final.append(i)
            except:
                pass
        for i in final:
            print(i)
        sum = 0
        count = 0
        for i in final:
            count += 1
            sum += int(i[-3])
        final_line = 'total number of records : ' + str(count) + '\n' + 'total amount spend on this selection : ' + str(sum)
        print(final_line)
        input('')
    except:
        os.system('color C')
        print('error occoured')
        time.sleep(1)
        os.system('color A')
        main()


def report_type():
    pass






# this function calls the main() dashboard function after login
def start():
    content = get_all_data()
    final = []
    for i in content:
        if i != []:
            final.append(i)
    f = open('data.csv', 'w')
    obj = csv.writer(f)
    obj.writerows(final)
    f.close()
    while True:
        if login() == True:
            while True:
                main()
        else:
            pass


start()