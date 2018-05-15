import smtplib
import click
import _mysql
import xlrd
import  MySQLdb


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("s.meena9874@gmail.com", "19981954meee")
msg = "output.xlsx"
server.sendmail("s.meena9874@gmail.com", "aruna1976mmv@gmail.com", msg)
dbPassword = "Mysql!@#"
database = MySQLdb.connect (host="localhost", user = "meena", passwd = dbPassword, db = "student")
#query = "CREATE TABLE `student`.`marks` (`students` VARCHAR(50) NOT NULL,`dbnames` VARCHAR(40),`marks1` VARCHAR(10),`marks2` VARCHAR(10),`marks3` VARCHAR(10),`maximum` VARCHAR(10),`total` VARCHAR(10), CONSTRAINT `dbnames`FOREIGN KEY (`dbnames`)REFERENCES `student`.`sinfo` (`dbnames`));"
query = "SELECT sinfo.dbnames,sinfo.college,marks.marks1,marks.marks2,marks.marks3,marks.maximum,marks.total FROM sinfo INNER JOIN marks ON sinfo.dbnames=marks.dbnames WHERE sinfo.college='%s'" % ("anits")
cursor = database.cursor()
cursor.execute(query)
result1=cursor.fetchall()
print(result1)
query = "SELECT sinfo.college,count(sinfo.college),sum(marks1),sum(marks2),sum(marks3),sum(maximum),sum(total) FROM sinfo INNER JOIN marks ON sinfo.dbnames=marks.dbnames WHERE sinfo.college='%s'" % ("anits")
cursor.execute(query)
result = cursor.fetchone()
minimum = min(result[2], result[3], result[4],result[5])
maximum = max(result[2], result[3], result[4],result[5])
total = result[6]/4
print(result[0], result[1], minimum, total, maximum)
query = "SELECT count(sinfo.college),min(total),max(total),sum(total) FROM sinfo INNER JOIN marks ON sinfo.dbnames=marks.dbnames"
cursor.execute(query)
result = cursor.fetchone()
minimum = min(result[1], result[2], result[3],result[4])
maximum = max(result[6], result[7], result[8],result[9])
total = result[5]/103
print(result[0],minimum, total, maximum)
print(result[6], result[7], result[8],result[9])
cursor.close()
database.commit()
database.close()