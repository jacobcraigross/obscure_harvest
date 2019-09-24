#type conversion, one liner
print(type(int(str(8277364))))

#type conversion, 4 liner
alpha_one = str(8277364)
omega_two = int(alpha_one)
sigma_three = type(omega_two)
print(sigma_three)


"""
# pounds to kilos. 
weight_lbs = input('how much do you weigh in pounds? ')
weight_kg = int(weight_lbs) * 0.45
print('your weight in kilograms is ---> ',weight_kg)

# email formatting
email = '''
Hello, 

I am writing this email to confirm **insert email jargon**
We would like to say x y and z, please continue. 
For now, you can go into the back and...
Beneath the shelf there is a thing that will 

Thanks,
The Watchers
'''

# string formatting
thrash = 'Exodus'
death = 'Obituary'
black = 'Darkthrone'
doom = 'Saint Vitus'
message_one = f'{doom} was an early example of Doom Metal. From Norway we have {black}. '
message_two = f'{death} has a great song called Threatening Skies. {thrash} are from the Bay Area.'
print(message_one, message_two)

# string methods
random_lyrics = 'A great exaltation of the infernal cabal is torched across the blazing skies. We behold the serpent dawn as the fires consume the horizon.'
print(len(random_lyrics))
# does NOT change the original variable.
print(random_lyrics.upper())
# the original variable. 
print(random_lyrics)
# prints / returns the index of the first occurence of i
print(random_lyrics.find('i'))
# replaces things via feeding in arguments. 
print(random_lyrics.replace('infernal', 'BLACKENED'))
"""