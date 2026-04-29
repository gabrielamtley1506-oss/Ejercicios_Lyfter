class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary  
    
    # PROPERTY FOR NAME
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Name must be a non-empty string")
        self._name = new_name
    
    # PROPERTY FOR SALARY
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if self.new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = self.new_salary
    
    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("Percentage cannot be negative")
        
        increase = self._salary * (percentage / 100)
        self._salary += increase
        print(f"{self._name} promoted!")
        print(f"  Increase: ${increase:.2f}")
        print(f"  New salary: ${self._salary:.2f}")
    
    def display_info(self):
        """Display employee information"""
        print(f"\n--- Employee Info ---")
        print(f"Name: {self._name}")
        print(f"Salary: ${self._salary:.2f}")


employee1 = Employee("Gabriela", 5000)
employee1.promote(10)
employee1.display_info()
employee1._salary=2600
employee1.display_info()



