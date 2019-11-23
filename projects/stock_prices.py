ADJ_CLOSE_INDEX = 5
VOLUME = 6
MONTH_SLICE_INDEX = -3

def file_object():
   """Returns a opened file or nothing 
   if the user inputs the wrong file name"""
   filename = str(input("Enter filename: "))
   try:
      a_file = open(filename,"r")
      return a_file
   except FileNotFoundError:
      print("Filename {} not found!".format(filename))
      return False

def get_data_list(filename):
   """Returns a list with all the lines in a list"""
   full_line_list = []

   for line in filename:
      line_list = line.strip().split(",")
      full_line_list.append(line_list)
   return full_line_list

def month(a_list):
   """Returns a three dimentional list 
   [[[month,stock_prices],[month,stock_prices],...]]"""
   data_list_month = []
   month = a_list[1][0][:MONTH_SLICE_INDEX]
   month_list = []
   for line in a_list[1:]:
      date = line[0][:MONTH_SLICE_INDEX]
      
      if date != month:
         data_list_month.append(month_list)
         month_list = []
      month_list.append(line)
      month = date

      #appends the last line to the data_list month
      if line is a_list[-1]: 
         data_list_month.append(month_list)

   return data_list_month

def get_monthly_averages(a_list): 
   """Computes the average price and 
   appends that price in monthly_averages list
   average_price = (V1 ∗ C1 + V2 ∗ C2 +···+ Vn ∗ Cn)/(V1 + V2 +···+ Vn)"""
   
   monthly_averages = []
   for month in a_list:
      volume_sum_list = []
      V_times_C = []
      month_str = month[0][0][:MONTH_SLICE_INDEX]

      for day in month:
         volume = float(day[VOLUME])
         adj_close = float(day[ADJ_CLOSE_INDEX])
         volume_sum_list.append(volume)
         V_times_C.append(volume * adj_close)

      formula = (sum(V_times_C) / sum(volume_sum_list))
      monthly_averages.append([month_str, formula])
      
   return monthly_averages

def print_format(monthly_average, highest_value):
   """Prints the right format"""

   print("{:<10}{:>7}".format("Month","Price"))
   for x in monthly_average:
      month = x[0]
      value = x[1]
      print("{:<10s}{:>7.2f}".format(month,value))
   print("Highest price {:.2f} on day {}".format(highest_value[1],highest_value[0]))

def get_highest(a_list):
   """Returns a tuple which contains 
   the highest price with its corresponding date"""

   max_value = 0.0
   max_date = ""
   for line in a_list[1:]:
      date = line[0]
      adj_close = float(line[ADJ_CLOSE_INDEX])
      if adj_close > max_value:
         max_value = adj_close
         max_date = date
   return (max_date, max_value)

def main():
   filename = file_object()

   if filename == False:
      pass
   else:
      data_list = get_data_list(filename)
      data_list_months = month(data_list)
      monthly_average = get_monthly_averages(data_list_months)
      highestValue = get_highest(data_list)

      print_format(monthly_average, highestValue)

main()