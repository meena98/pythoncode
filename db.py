import click
import _mysql
import xlrd
import  MySQLdb

'''
@click.command()
@click.option('--createdb', default='', help="Will create a database.")
@click.option('--dropdb', default='', help='will drop the database?')
@click.option('--importdata', default='', help="imports data from the files into tables")
@click.option('--collegestats', default='', help='will return the statictics of each college')
def cli(createdb,dropdb,importdata,collegestats):
    if(createdb):
        click.echo("hello")
'''
'''
dbPassword = "Mysql!@#"
database = MySQLdb.connect (host="localhost", user = "meena", passwd = dbPassword, db = "student")
#query = "CREATE TABLE `student`.`marks` (`students` VARCHAR(50) NOT NULL,`dbnames` VARCHAR(40),`marks1` VARCHAR(10),`marks2` VARCHAR(10),`marks3` VARCHAR(10),`maximum` VARCHAR(10),`total` VARCHAR(10), CONSTRAINT `dbnames`FOREIGN KEY (`dbnames`)REFERENCES `student`.`sinfo` (`dbnames`));"
#query="SELECT COUNT(college) FROM sinfo WHERE college = '%s'" % ("anits")
query1="SELECT DISTINCT(college) from sinfo"
cursor = database.cursor()
book = xlrd.open_workbook("output.xlsx")
sheet = book.sheet_by_name("Sheet1")
cursor.execute(query1)
result1=cursor.fetchall()
print(result1)
for temp in  result1:
    for col in temp:
        query = "SELECT sinfo.college,count(sinfo.college),sum(marks1),sum(marks2),sum(marks3),sum(maximum),sum(total) FROM sinfo INNER JOIN marks ON sinfo.dbnames=marks.dbnames WHERE sinfo.college='%s'" % (col)
        cursor.execute(query)
        result = cursor.fetchone()
        minimum = min(result[2], result[3], result[4],result[5])
        maximum = max(result[2], result[3], result[4],result[5])
        total = result[6]/4
        # print(result)
        print(result[0], result[1], minimum, total, maximum)
cursor.close()
database.commit()
database.close()
'''

'''
query1 = """INSERT INTO marks (students, dbnames, marks1,marks2,marks3,maximum,total) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
r=0
for r in range(100,sheet.nrows):
    name = sheet.cell(r, 0).value
    marks1 = sheet.cell(r, 1).value
    marks2 = sheet.cell(r, 2).value
    marks3 = sheet.cell(r, 3).value
    maximum = sheet.cell(r, 4).value
    total = sheet.cell(r, 5).value
    l = (name[7:]).split("_", 2)
    dbname = l[1].lower()
    values = (name, dbname, marks1, marks2, marks3, maximum, total)
    print(name, dbname, marks1, marks2, marks3, maximum, total)
    if dbname=="skc":
        pass
    else:
        cursor.execute(query1, values)
'''
'''
query = "CREATE TABLE `student`.`sinfo` (`name` VARCHAR(50) NOT NULL,`college` VARCHAR(20),`emailid` VARCHAR(50),`dbnames` VARCHAR(40),PRIMARY KEY (`dbnames`));"
query1 = """INSERT INTO sinfo (name, college, emailid,dbnames) VALUES (%s,%s,%s,%s)"""
book = xlrd.open_workbook("students.xlsx")
sheet = book.sheet_by_name("Current")
cursor = database.cursor()
print(sheet.nrows)
cursor.execute(query)
for r in range(1,sheet.nrows):
    name = sheet.cell(r, 0).value
    college = sheet.cell(r, 1).value
    emailid = sheet.cell(r, 2).value
    dbnames = sheet.cell(r, 3).value
    values=(name,college,emailid,dbnames.lower())
    cursor.execute(query1, values)
    print(dbnames)
cursor.close()
database.commit()
database.close()
'''







#sqlQuery="CREATE TABLE `student`.`marks` (`marks` INT NOT NULL,`subject` VARCHAR(45),`st_id` INT(11),PRIMARY KEY (`subject`),CONSTRAINT `st_id`FOREIGN KEY (`st_id`)REFERENCES `student`.`student`(`st_id`));"
#db = _mysql.connect(user='meena', passwd=dbPassword, host='127.0.0.1', db='student')
#db.query(sqlQuery);
#db.query(query);
#db.close()
