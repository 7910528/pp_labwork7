import cx_Oracle

def insert_values(cursor, query, values):
    for value in values:
        try:
            cursor.execute(query, value)
        except cx_Oracle.IntegrityError:
            continue

def create_it_corporation(cursor):
    cursor.execute(
        '''
        CREATE TABLE it_corporation (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            last_name VARCHAR2(255),
            first_name VARCHAR2(255),
            birth_date DATE,
            phone VARCHAR2(13),
            educ VARCHAR2(255),
            position VARCHAR2(255),
            department VARCHAR2(255),
            skill VARCHAR2(255),
            rate NUMBER
        )
        '''
    )
    print("Created table 'it_corporation'")

def create_computers(cursor):
    cursor.execute(
        '''
        CREATE TABLE computers (
            id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            name VARCHAR2(255),
            chipset VARCHAR2(255),
            processor VARCHAR2(255),
            ram NUMBER,
            vga VARCHAR2(255),
            hdd NUMBER,
            os VARCHAR2(255),
            cost NUMBER
        )
        '''
    )
    print("Created table 'computers'")

def insert_itcorp(cursor):
    query = """
    INSERT INTO it_corporation (last_name, first_name, birth_date, phone, educ, position, department, skill, rate)
    VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7, :8, :9)
    """
    data = [
        ('Абрамов', 'Афанасій', '1967-05-24', '+380675764938', 'вища', 'завідувач відділу', 'Фінансовий відділ', '1C Бухгалтерія', 7238),
        ('Абрамов', 'Іван', '1988-09-19', '+380457668521', 'середня', 'стажер', 'Фінансовий відділ', 'MS Office', 3500),
        ('Абрамов', 'Інгатій', '1989-09-22', '+380577843547', 'вища', 'web-програміст', 'Відділ проектування', 'PHP, JavaScript, Drupal', 9200),
        ('Шевченко', 'Інна', '1977-04-25', '+380612836579', 'середня', 'стажер', 'Відділ проектування', 'PHP, JavaScript', 4305),
        ('Ігнатьєв', 'Іван', '1995-07-22', '+380452232707', 'вища', 'програміст', 'Відділ проектування', 'C#, C++', 15480),
        ('Степанова', 'Ганна', '1989-06-21', '+380358470001', 'середня', 'програміст', 'Відділ проектування', 'Java', 7900),
        ('Федоров', 'Іван', '1958-08-19', '+380533209578', 'вища', 'адміністратор БД', 'Відділ проектування', 'DB2', 9600),
        ('Федоров', 'Інгатій', '1978-05-27', '+380612896086', 'середня', 'адміністратор БД', 'Відділ проектування', 'Oracle DB', 8500),
        ('Кириленко', 'Іван', '1977-12-12', '+380545903940', 'вища', 'системний адміністратор', 'Відділ проектування', 'Windows Server, Unix Server', 10300),
        ('Іваненко', 'Анастасія', '1994-04-04', '+380457645345', 'вища', 'бухгалтер', 'Фінансовий відділ', '1C Бухгалтерія', 7500)
    ]
    insert_values(cursor, query, data)
    print("Inserted rows into 'it_corporation'")

def insert_computers(cursor):
    query = """
    INSERT INTO computers (name, chipset, processor, ram, vga, hdd, os, cost)
    VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
    """
    data = [
        ('Base NW-01', 'MSI H61M-P31/W8', 'Intel Celeron G1620', 1, 'ASUS 210-SL-TC1GD3-L', 250, 'no', 4500),
        ('Base MF-45', 'MSI H81M-P33', 'Intel Celeron G1820', 2, 'Sapphire Radeon HD5450 512 MB', 320, 'DOS', 5700),
        ('Universal KL-32', 'ASUS B85-PLUS', 'Intel Core i3-4330', 8, 'ASUS GTX750-PH-1GD5', 500, 'Windows 8', 11300),
        ('Universal GHL-09', 'ASUS Z97-P', 'Intel Core i5-4670', 16, 'ASUS R7250X-2GD5', 600, 'Linux', 10000),
        ('Extreme FV-110', 'ASUS Maximus VI Ranger', 'Intel Core i5-4670K', 16, 'ASUS R9270X-DC2T-2GD5', 1000, 'Windows 7', 27800),
        ('Base SM-31', 'MSI H81M-P33', 'Intel Celeron G1610', 2, 'ASUS HD5450-SL-HM1GD3-L-V2', 250, 'Linux', 2700),
        ('Extreme FD-56', 'ASUS Z97-PRO', 'Intel Core i7-4930K', 32, 'Zotac GeForce GTX960 ZT-90303-10M', 2000, 'Windows 7', 35800),
        ('Universal U-04', 'ASUS Z97-P', 'Intel Core i5-4460', 8, 'ASUS GT740-2GD3', 1000, 'Windows 8', 12900),
        ('Base DH-321', 'MSI H81M-P33', 'Intel Celeron G1840', 4, 'ASUS 210-1GD3-L', 320, 'no', 6100),
        ('Extreme AW-789', 'ASUS Maximus VII GENE', 'Intel Core i7-4960X', 32, 'ASUS GTX760-DC2T-2GD5-SSU', 3000, 'Windows 7', 42500)
    ]
    insert_values(cursor, query, data)
    print("Inserted rows into 'computers'")

def select_higher_educ_or_over_40(cursor):
    cursor.execute(
        '''
        SELECT last_name, first_name, birth_date, phone, educ, position, department, skill, rate
        FROM it_corporation
        WHERE educ = 'вища'
        UNION
        SELECT last_name, first_name, birth_date, phone, educ, position, department, skill, rate
        FROM it_corporation
        WHERE EXTRACT(YEAR FROM SYSDATE) - EXTRACT(YEAR FROM birth_date) > 40
        '''
    )
    print('Employees with higher education or those over 40:')
    for row in cursor.fetchall():
        print(row)

def select_not_programmers(cursor):
    cursor.execute(
        '''
        SELECT last_name, first_name, birth_date, phone, educ, position, department, skill, rate
        FROM it_corporation
        WHERE position != 'програміст'
        '''
    )
    print('Employees who are not programmers:')
    for row in cursor.fetchall():
        print(row)

def main():
    try:
        dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XEPDB1")
        connection = cx_Oracle.connect(user="SYS", password="7910528", dsn=dsn, mode=cx_Oracle.SYSDBA)
        cursor = connection.cursor()
        
        create_it_corporation(cursor)
        create_computers(cursor)
        connection.commit()

        insert_itcorp(cursor)
        insert_computers(cursor)
        connection.commit()

        select_higher_educ_or_over_40(cursor)
        select_not_programmers(cursor)

    except cx_Oracle.DatabaseError as e:
        print("Database error occurred:", e)
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    main()