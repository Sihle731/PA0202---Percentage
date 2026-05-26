print('Question 1: Discount Calculator')

def discount(price, discount_p):
    discount_amount = price * (discount_p / 100)
    final_price = price - discount_amount
    return discount_amount, final_price

original_price = 586
discount_percentage = 20
discount_amount, final_price = discount(original_price, discount_percentage)
print(f'Original Price: {original_price}')
print(f'Discount Percentage: {discount_percentage}%')
print(f'The Discount amount is {discount_amount}')
print(f'The final price after applying the discount is {final_price}')



print('Question 2: Exam Percentage Calculator and Grade Assignment')
def cal_percentage(marks_obtained, total_marks):
    percentage = (marks_obtained / total_marks) * 100
    return percentage
def grade_assignment(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
    
marks_obtained = 85
total_marks = 100
percentage = cal_percentage(marks_obtained, total_marks)
grade = grade_assignment(percentage)
print(f'Marks Obtained: {marks_obtained}')
print(f'Total Marks: {total_marks}')
print(f'Percentage: {percentage}%')
print(f'Grade: {grade}')


print('Question 3: Salary Increase Calculator')
      
def salary_increase(current_salary, increase_percentage):
    increase_amount = current_salary * (increase_percentage / 100)
    new_salary = current_salary + increase_amount
    return increase_amount, new_salary

current_salary = 50000
increase_percentage = 10
increase_amount, new_salary = salary_increase(current_salary, increase_percentage)
print(f'Current Salary: {current_salary}')
print(f'Increase Percentage: {increase_percentage}%')
print(f'Increase Amount: {increase_amount}')
print(f'New Salary: {new_salary}')

print('Question 4: Profit percentage Calculator')
def profit_percentage(cost_price, selling_price):
    profit = selling_price - cost_price
    percentage_profit = (profit / cost_price) * 100
    return percentage_profit

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
percentage_profit = profit_percentage(cost_price, selling_price)
print(f'Cost Price: {cost_price}')
print(f'Selling Price: {selling_price}')
print(f'Percentage Profit: {percentage_profit}%')
