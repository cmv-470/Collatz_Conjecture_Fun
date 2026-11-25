import streamlit as st
st.set_page_config("Collatz Conjecture Checker", "chart_with_upwards_trend")
number = st.number_input("Provide a value to check for the Collatz Conjecture: ", 1)
def collatz_data(number):
    original_number = number
    hailstone_sequence = []
    while number != 1:
        if number % 2 ==0:
            number=number/2
        else:
            number=3*number+1
        hailstone_sequence.append(int(number))

    averages = []
    average = 0
    for i in range(len(hailstone_sequence)):
        try:
            averages.append(hailstone_sequence[i+1]-hailstone_sequence[i])
        except:
            pass
    for item in averages:
        average += int(item)
    average = average/len(averages)

    max = 0
    for item in hailstone_sequence:
        if item>max:
            max = item

    evens = []
    odds = []
    for item in hailstone_sequence:
        if item % 2 == 0:
            evens.append(item)
        else:
            odds.append(item)
    mean = 0
    for item in hailstone_sequence:
        mean += item
    mean = mean/len(hailstone_sequence)

    standard_deviation = 0
    deviations = []
    for item in hailstone_sequence:
        deviations.append(item - mean)
    for item in deviations:
        item = item ** 2
        standard_deviation+=item
    standard_deviation = standard_deviation/len(deviations)
    standard_deviation = standard_deviation ** 0.5

    lower_number = original_number -1
    lower_hailstone_sequence = []
    while lower_number != 1:
        if lower_number % 2 ==0:
            lower_number=lower_number/2
        else:
            lower_number=3*lower_number+1
        lower_hailstone_sequence.append(int(lower_number))

    upper_number = original_number +1
    upper_hailstone_sequence = []
    while upper_number != 1:
        if upper_number % 2 ==0:
            upper_number=upper_number/2
        else:
            upper_number=3*upper_number+1
        upper_hailstone_sequence.append(int(upper_number))

    lower_max = 0
    for item in lower_hailstone_sequence:
        if item > lower_max:
            lower_max = item

    upper_max = 0
    for item in upper_hailstone_sequence:
        if item > upper_max:
            upper_max = item
    sum = 0
    for item in hailstone_sequence:
        sum += item

    if len(hailstone_sequence) % 2 != 0:
        sorted_hailstone_sequence = hailstone_sequence
        sorted_hailstone_sequence.sort()
        median = sorted_hailstone_sequence[int(len(hailstone_sequence)/2)]
    else:
        sorted_hailstone_sequence = hailstone_sequence
        sorted_hailstone_sequence.sort()
        median = (sorted_hailstone_sequence[int(len(hailstone_sequence)/2)]+sorted_hailstone_sequence[int(len(hailstone_sequence)/2)-1])/2

    return f"The value being checked is: {str(original_number)}.\n\nHailstone Sequence is: {str(hailstone_sequence)}.\n\n{str(original_number)} is not a solution to the Collatz Conjecture 🙁.\n\n{str(average)}, is the average change from element to element in the sequence.\n\nThe maximum value for {str(original_number)} in its hailstone sequence is {str(max)}. The length of the hailstone sequence is: {str(len(hailstone_sequence))}.\n\nThe percentage of even numbers in the hailstone sequence is: {str(100*(len(evens)/len(hailstone_sequence)))}%.\n\nThe percentage of odd numbers in the hailstone sequence is: {str(100*(len(odds)/len(hailstone_sequence)))}%.\n\nThe mean of this sequence is: {str(mean)}.\n\nThe standard deviation of the hailstone sequence is: {str(standard_deviation)}.\n\nThe median of the hailstone sequence for {str(original_number)} is: {str(median)}.\n\n{str(original_number)}'s hailstone sequence is {str((len(hailstone_sequence)/len(lower_hailstone_sequence))*100)}% longer than the number below {str(original_number)}'s ({str(original_number - 1)}) hailstone sequence.\n\n{str(original_number)}'s hailstone sequence is {str((len(hailstone_sequence)/len(upper_hailstone_sequence))*100)}% longer than the number above {str(original_number)}'s ({str(original_number + 1)}) hailstone sequence.\n\nThe maximum value for {str(original_number)} is {str((max/lower_max)*100)}% greater than the maximum for the number below {str(original_number)} ({str(original_number - 1)}).\n\nThe maximum value for {str(original_number)} is {str((max/upper_max)*100)}% greater than the maximum for the number above {str(original_number)} ({str(original_number + 1)}).\n\nThe sum of every number in the hailstone sequence is: {str(sum)}."
def hailstone_sequence(number):
    hailstone_sequence = []
    while number != 1:
        if number % 2 ==0:
            number=number/2
        else:
            number=3*number+1
        hailstone_sequence.append(int(number))
    return hailstone_sequence
if st.button("Check"):
    st.markdown(collatz_data(number))
    st.markdown(f":blue[A line chart showing the numbers in {number}'s hailstone sequence:]")
    st.line_chart(hailstone_sequence(number))
