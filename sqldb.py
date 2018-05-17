import click
import _mysql
import xlrd
import  MySQLdb


@click.command()
@click.option('--create',is_flag=True,help="will create the database")
@click.option('--drop',is_flag=True,help="drops db")
@click.option('--importdata',is_flag=True,help="will import the data from xlsx sheets")
@click.option('--collegestats',is_flag=True,help="will return a report of the college")
def cli(create,drop,importdata,collegestats):
    if create:
        click.echo("hello")
        dbPassword = "Mysql!@#"
        database = MySQLdb.connect(host="localhost", user="meena",
                                   passwd=dbPassword, db="student")
        query = "CREATE TABLE `student`.`sinfo` (`name` VARCHAR(50) NOT NULL,`college` VARCHAR(20),`emailid` VARCHAR(50)," \
                "`dbnames` VARCHAR(40),PRIMARY KEY (`dbnames`));"
        query1 = "CREATE TABLE `student`.`marks` (`students` VARCHAR(50) NOT NULL,`dbnames` VARCHAR(40),`marks1` VARCHAR(10)," \
                 "`marks2` VARCHAR(10),`marks3` VARCHAR(10),`maximum` VARCHAR(10),`total` VARCHAR(10)," \
                 " CONSTRAINT `dbnames`FOREIGN KEY (`dbnames`)REFERENCES `student`.`sinfo` (`dbnames`));"
        cursor = database.cursor()
        cursor.execute(query)
        cursor.execute(query1)
        cursor.close()
        database.commit()
        database.close()
        click.echo("database and tables created")
    if drop:
        dbPassword = "Mysql!@#"
        database = MySQLdb.connect(host="localhost", user="meena",
                                   passwd=dbPassword, db="student")
        query = "DROP DATABASE student;"
        cursor = database.cursor()
        cursor.execute(query)
        cursor.close()
        database.commit()
        database.close()
        click.echo("database dropped")
    if (importdata):
        dbPassword = "Mysql!@#"
        database = MySQLdb.connect(host="localhost", user="meena",
                                   passwd=dbPassword, db="student")
        query = """INSERT INTO sinfo (name, college, emailid,dbnames) VALUES (%s,%s,%s,%s)"""
        book = xlrd.open_workbook("students.xlsx")
        sheet = book.sheet_by_name("Current")
        cursor = database.cursor()
        for r in range(1, sheet.nrows):
            name = sheet.cell(r, 0).value
            college = sheet.cell(r, 1).value
            emailid = sheet.cell(r, 2).value
            dbnames = sheet.cell(r, 3).value
            values = (name, college, emailid, dbnames.lower())
            cursor.execute(query1, values)
            print(dbnames)
        query1 = """INSERT INTO marks (students, dbnames, marks1,marks2,marks3,maximum,total) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        book = xlrd.open_workbook("output.xlsx")
        sheet = book.sheet_by_name("Sheet1")
        for r in range(0, sheet.nrows):
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
            if dbname == "skc":
                pass
            else:
                cursor.execute(query1, values)
        cursor.close()
        database.commit()
        database.close()
    if(collegestats):
        dbPassword = "Mysql!@#"
        database = MySQLdb.connect(host="localhost", user="meena",
                                   passwd=dbPassword, db="student")
        query1 = "SELECT DISTINCT(college) from sinfo"
        cursor = database.cursor()
        cursor.execute(query1)
        result1 = cursor.fetchall()
        print(result1)
        for temp in result1:
            for col in temp:
                query = "SELECT sinfo.college,count(sinfo.college),sum(marks1),sum(marks2),sum(marks3),sum(maximum),sum(total) FROM sinfo INNER JOIN marks ON sinfo.dbnames=marks.dbnames WHERE sinfo.college='%s'" % (col)
                cursor.execute(query)
                result = cursor.fetchone()
                minimum = min(result[2], result[3], result[4], result[5])
                maximum = max(result[2], result[3], result[4], result[5])
                total = result[6] / 4
                # print(result)
                print(result[0], result[1], minimum, total, maximum)
        cursor.close()
        database.commit()
        database.close()

