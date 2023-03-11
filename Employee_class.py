class Employee:
    def __init__(self, id = "00000", month = 1, day = 1, year = 2000, title = "engineer"):
        self.id = id
        self.month = month
        self.day = day
        self.year = year
        self.title = title
        if (self.title == "engineer"):
            self.salary = "$50,000"
        elif(self.title == "lead engineer"):
            self.salary = "$65,000"
        else:
            self.salary = "$80,000"
        

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id_value):
        if (len(id_value) == 5):
            self._id = id_value
        else:
            self._id = "00000"

    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        if (value > 12 or value < 1):
            self._month = 1
        else:
            self._month = value

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, value):
        if (value > 32 or value < 1):
            self._day = 1
        else:
            self._day = value

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        if (value < 1900 or value > 2004):
            self._year = 2000
        else:
            self._year = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if (value != "engineer" and value != "lead engineer" and value != "supervisor"):
            self._title = "engineer"
        else:
            self._title = value

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if (self.title == "engineer"):
            self._salary = "$50,000"
        elif(self.title == "lead engineer"):
            self._salary = "$65,000"
        else:
            self._salary = "$80,000"

    def __str__(self):
        return ("|Employee id: {}\tD.O.B: {}-{}-{} \tTitle: {}  \tSalary: {}|".format(self.id, self.month, self.day, self.year, self.title, self.salary))


bob = Employee()
print(bob)
sarah = Employee("12345", 4, 20, 1988, "lead engineer")
print(sarah)
john = Employee("123", 12, 33, 1899, "supervisor")
print(john)
jill = Employee("45573", 3, 12, 1976, "engineer")
print(jill)
