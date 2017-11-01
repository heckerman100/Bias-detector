#This program takes a paragraph of words and adds the numerical value of each word togethor to see if it is bais or not.
#Not 100% acurate


#Bias words
Their = 1
I = 1
Culture = 1
Race = 1
Kingsize = 1
Buisnessman = 1
Careergirl = 1
Careerwoman = 1
Foreman = 1
Mailman = 1
Landlord = 1
Landlady = 1
Newsman = 1
Repairman = 1
Policeman = 1
Salesman = 1
Saleswoman = 1
Saleslady = 1
Cleaninglady = 1
Paperboy = 1
Waitress = 1
Workman = 1
Spokesman = 1
Ladylike = 1
Manly = 1
Maiden = 1
Manhood = 1
Manmade = 1
Motherly = 1
Statesman = 1
Congressman = 1
Congresswoman = 1
Chairmen = 1
Craftsman = 1
Oldpeople = 1
Eskimo = 1
Fireman = 1
Illegalalien = 1
Indian = 1
Jew = 1
Mankind = 1
Underprivileged = 1
Wealthy = 1
Southside = 1
Bluecollar = 1
Innercity = 1
Waiter = 1

#Original value
Original_value = 0

#Input text
Text = input("Paste text or type here: ")

#Applied value
App1 = Text.count('I')
App2 = Text.count('Their')
App3 = Text.count('Culture')
App4 = Text.count('Race')
App5 = Text.count('Kingsize')
App6 = Text.count('Buisnessman')
App7 = Text.count('Careergirl')
App8 = Text.count('Congresswoman')
App9 = Text.count('Foreman')
App10 = Text.count('Mailman')
App11 = Text.count('Landlord')
App12 = Text.count('Landlady')
App13 = Text.count('Newsman')
App14 = Text.count('Repairman')
App15 = Text.count('Policeman')
App16 = Text.count('Saleswoman')
App17 = Text.count('Salesman')
App18 = Text.count('Saleslady')
App19 = Text.count('Cleaninglady')
App20 = Text.count('Paperboy')
App21 = Text.count('Waitress')
App22 = Text.count('Workman')
App23 = Text.count('Spokesman')
App24 = Text.count('Ladylike')
App25 = Text.count('Manly')
App26 = Text.count('Maiden')
App27 = Text.count('Manhood')
App28 = Text.count('Manmade')
App29 = Text.count('Motherly')
App30 = Text.count('Statesman')
App31 = Text.count('Congressman')
App32 = Text.count('Congresswoman')
App33 = Text.count('Chairmen')
App34 = Text.count('Craftsman')
App35 = Text.count('Oldpeople')
App36 = Text.count('Eskimo')
App37 = Text.count('Fireman')
App38 = Text.count('Illegalalien')
App39 = Text.count('Indian')
App40 = Text.count('Jew')
App41 = Text.count('Mankind')
App42 = Text.count('Underprivileged')
App43 = Text.count('Wealthy')
App44 = Text.count('Southside')
App45 = Text.count('Bluecollar')
App46 = Text.count('Innercity')
App47 = Text.count('Waiter')

Applied_value = App1 + App2 + App3 + App4 + App5 + App6 + App7 + App8 + App9 + App10 + App11 + App12 + App13 + App14 + App15 + App16 + App17 + App18 + App19 + App20 + App21 + App22 + App23 + App24 + App25 + App26 + App27 + App28 + App29 + App30 + App31 + App32 + App33 + App34 + App35 + App36 + App37 + App38 + App39 + App40 + App41 + App42 + App43 + App44 + App45 + App46 + App47

#Total
Total = Original_value - Applied_value
print(Total)
print("If the number is less than -10 the text is probably bias, if the number is more than -10 the text is probably not bias")
