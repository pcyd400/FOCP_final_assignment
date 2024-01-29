import sys

def analyze_log_file(filename):
  """Analyzes the cat shelter log file and prints the results."""

  try:
    with open(filename, 'r') as file:
      cat_visits = 0      #setting the initial values 
      intruder_visits = 0
      total_time_in_house = 0
      visit_durations = []

      for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        try:
          cat_type, entry_time_str, exit_time_str = line.split(',') #splitting the string in log file with comma
          entry_time = int(entry_time_str)
          exit_time = int(exit_time_str)

          if cat_type == 'OURS':     #calcularing the cat data
            cat_visits += 1
            visit_duration = exit_time - entry_time      
            total_time_in_house += visit_duration     
            visit_durations.append(visit_duration)
          else:
            intruder_visits += 1    #if  it is not a cat, then it must be an intruder and i will add to intruder 

        except ValueError:
          print(f"Invalid data format on line: {line}")  #if encounters the error in data format it will handle the error 
          continue  # Skip to the next line

      average_visit_length = sum(visit_durations) / len(visit_durations)    #calculating average visit 
      longest_visit = max(visit_durations) #calculating longest visit 
      shortest_visit = min(visit_durations) #calculating  shortest visit  

      print("\nLog File Analysis")
      print("==================")
      print("\nCat Visits:", cat_visits)
      print("Other Cats:", intruder_visits)
      print("\nTotal Time in House:", format_time(total_time_in_house))
      print("\nAverage Visit Length:", int(average_visit_length), "Minutes") #formated in integer to neglect the decimal value 
      print("Longest Visit:", longest_visit, "Minutes")
      print("Shortest Visit:", shortest_visit, "Minutes")

  except FileNotFoundError:
    print(f"Cannot open \"{filename}\"!")   #if there is no file find in the directory  it will show this message

def format_time(minutes):
  """Formats a duration in minutes as hours and minutes."""

  hours = minutes // 60
  minutes = minutes % 60
  return f"{hours} Hours, {minutes} Minutes"

if __name__ == "__main__":   #if  we are running this script directly then call main function with no arguments
  
  if len(sys.argv) != 2:
    print("Missing command line argument!")
  else:
    analyze_log_file(sys.argv[1]) #passing  the name of the log file as arguement
