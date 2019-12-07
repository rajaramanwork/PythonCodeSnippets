import pytest
import dto.employee as employee_ref
import dto.consultant as consultant_ref
class TestObjectCreations:
    def test_employee(self):
        _employee =  employee_ref.employee('Raj', 34)
        _employee.display()

    def test_consultant(self):
        _consultant =  consultant_ref.consultant('Ajay', 30)
        _consultant.display()