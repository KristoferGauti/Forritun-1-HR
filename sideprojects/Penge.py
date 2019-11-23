import string

#csv_skjöl/ReikningsYfirlit_01.11.2019.csv
def file_obj(filename):
   try:
      file_obj = open(filename)
      return file_obj
   except FileNotFoundError:
      print("File {} not found!".format(filename))
      return False

def get_spended_money_list(filename):
   """I know this function does too many things.
   A good programmer should avoid doing that"""
   

   line_list = [line.strip().split(",") for line in filename]
   binary = "0010001000001010" #binary string for the " character
   quotes = chr(int(binary[:8], 2)) #to get the character "
   
   #get the money per day
   money_list = []
   for line in line_list:
      money = line[5]
      
      if money[0] or money[-1] == quotes:
         money_list.append(money.strip(quotes))
      else:
         money_list.append(money)

   #Remove the string words
   for money in money_list:
      if money.isalpha:
         money_list.remove(money)

   #Make all the indexes integers
   int_money_list = []
   for penge in money_list:
      int_money_list.append(int(penge))

   #get all the negative numbers
   total_spent_for_the_month = []
   for final_money in int_money_list:
      if final_money < 0:
         total_spent_for_the_month.append(final_money)

   #Calculate the monthly spenses 
   #Convert all negativ enumbers to positive
   total_spent_calculation_list = []
   for negative_num in total_spent_for_the_month:
      total_spent_calculation_list.append(negative_num * (-1))

   return sum(total_spent_calculation_list), total_spent_calculation_list


def main():
   filename = input("Enter filename: ")

   a_file = file_obj(filename)

   if file_obj == False:
      pass
   else:
      total_money_spent, total_list = get_spended_money_list(a_file)
      print()
      print("The money list: {}".format("".join(str(total_list)[1:-1])))
      print()
      print("The quantity of items you bought this month is {}".format(len(total_list)))
      print("Total money spent this month: {}kr".format(total_money_spent))
      print()

main()
