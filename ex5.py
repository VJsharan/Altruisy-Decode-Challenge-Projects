def get_input():
    strength_values = []
    for i in range(12):  # We need 12 values (4 trainees * 3 rounds)
        try:
            value = int(input())
            if value < 1 or value > 200:
                return "INVALID INPUT"
            strength_values.append(value)
        except ValueError:
            return "INVALID INPUT"
    return strength_values

def calculate_average(strength_values):
    averages = []
    for i in range(0, 12, 4):  # Trainee 1 to 4, for each round
        trainee_values = strength_values[i:i+4]
        average = round(sum(trainee_values) / 3)  # Calculate the average for each trainee
        averages.append(average)
    return averages

def main():
    strength_values = get_input()
    
    if strength_values == "INVALID INPUT":
        print("INVALID INPUT")
        return
    
    averages = calculate_average(strength_values)
    
    max_average = max(averages)
    
    if max_average < 100:
        print("All trainees are unfit.")
        return
    
    for i in range(4):
        if averages[i] == max_average:
            print(f"Trainee Number : {i + 1}")
    
if __name__ == "__main__":
    main()
