import pickle


def bf_append():
    f = open("employee.txt", "ab")
    print("Append Data")
    pcode = int(input("Enter the Player code: "))
    pname = input("Enter Player Name: ")
    score = int(input("Enter individual score: "))
    rank = int(input("Enter Player Rank: "))
    rec = {'Pcode': pcode, 'Pname': pname, 'Score': score, 'Rank': rank}
    pickle.dump(rec, f)

    f.close()


def bf_read():
    f = open("employee.txt", "rb")
    print("*" * 50)
    print("Data stored in File....")
    while True:
        try:
            rec = pickle.load(f)
            print("Player Code: ", rec['Pcode'])
            print("Player Name: ", rec['Pname'])
            print("Individual Score: ", rec['Score'])
            print("Player Rank: ", rec['Rank'])
            print("." * 50)
        except Exception:
            break

        f.close()


def bf_search():
    f = open("employee.txt", "rb")
    pc = int(input("Player to code to search: "))
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Pcode'] == pc:
                print("Player Name: ", rec['Pname'])
                print("Individual Score: ", rec['Score'])
                print("Rank: ", rec['Rank'])
                flag = True
        except Exception:
            break
    if flag == False:
        print("Record not found...")

    f.close()


def bf_update():
    f = open('employee.txt', 'rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break

    f.close()

    pc = int(input("Enter player code to update: "))
    pn = input("Enter new name: ")
    ps = int(input("Enter Player Score: "))
    pr = int(input("Enter Player Rank: "))

    for i in range(len(reclst)):
        if reclst[i]['Pcode'] == pc:
            reclst[i]['Pname'] = pn
            reclst[i]['Score'] = ps
            reclst[i]['Rank'] = pr

    f = open('employee.dat', 'wb')

    for i in reclst:
        pickle.dump(i, f)

    f.close()


def bf_delete():
    f = open('employee.txt', 'rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break

    f.close()

    pc = int(input("Enter Player code to delete record: "))

    f = open('employee.txt', 'wb')

    for i in reclst:
        if i['Pcode'] == pc:
            continue
        pickle.dump(i, f)

    f.close()


def main():
    while True:
        print('1. Insert Record')
        print('2. Display Records')
        print('3. Search Record')
        print('4. Update Record')
        print('5. Delete Record')
        print('0. Exit')
        
        choice = int(input('Enter you choice: '))
        if choice == 0:
            break
        elif choice == 1:
            bf_append()
        elif choice == 2:
            bf_read()
        elif choice == 3:
            bf_search()
        elif choice == 4:
            bf_update()
        elif choice == 5:
            bf_delete()


if __name__ == "__main__":
    main()