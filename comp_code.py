import mysql.connector as sqltor
con= sqltor.connect(host='localhost',user='root',passwd='1234',database='library') 


def addbook():
    name=input('enter book name: ')
    code=input('enter book code: ')
    total=input('total number of copies of the book: ')
    sub=input('enter subject/genre\
: ')
    data=(name,code,sub,total)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('data entered successfully')
    main()

def issue():
    name=input('enter your name: ')
    code=input('enter book code: ')
    a='insert into issue values(%s,%s)'
    data=(name,code)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print('book issued to : ',name)
    st="update books set total=total-1 where code='%s'"%(code)
    c.execute(st)
    con.commit()
    main()
    
def submit():
    name=input('enter your name: ')
    code=input('enter book code: ')
    a='insert into submit values(%s,%s)'
    data=(name,code)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print('book submitted from : ',name)
    sta="update books set total=total+1 where code='%s'"%(code)
    c.execute(sta)
    con.commit()
    main()

def delete():
    ac=input('enter book code')
    a='delete from books where code=%s'
    data= (ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def display():
    a='select * from books'
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print('book name: ',i[0])
        print('book code: ',i[1])
        print('total copies: ',i[3])
        print('------------------------------------------------')
    main()

def main():
    print('''
                 LIBRARY MANAGER
1. ADD BOOK 
2. ADD TO BOOKS ISSUED REGISTER
3. ADD TO BOOKS RETURNED REGISTER
4. DELETE BOOK 
5. DISPLAY ALL THE BOOKS
 ''')
    ch=input('enter task no:')
    print('')
    if ch=='1':
        addbook()
    elif ch=='2':
        issue()
    elif ch=='3':
        submit()
    elif ch=='4':
        delete()
    elif ch=='5':
        display()
    else:
        print('wrong choice')
main()
    
