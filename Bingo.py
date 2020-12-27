#!/usr/bin/env python
# coding: utf-8

# # Bingo
# <b>Date Created:</b> 13th November 2020 <br>
# <b>Author:</b> Scott Jenkins <br>
# <b>Date Modified:</b> 15th November 2020

# #### In this Notebook:
# 
# **(Complete)**  Expected number of ticks required before you get a line?
# 
# **(Complete)** Follow up question 1: Expected number of calls required before you get a line or full house (link calls to ticks to lines)
# 
# 
# **(Complete)** Follow up question 2: When playing with n people, expected number of calls required before anyone gets a line or full house

# In[450]:


import random
import plotly.express as px
import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()


# In[174]:


# First, define a function which checks for lines in a square grid of any grid size, it's pretty naive
def check_for_line(grid,grid_size):
    max_row_col_count = 0
    for i in range(grid_size):
        row_count = len(list(filter(lambda x: x[0] == i, grid)))
        col_count = len(list(filter(lambda x: x[1] == i, grid)))
        #print('Count of elements in row {}:'.format(i), row_count)
        #print('Count of elements in col {}:'.format(i), col_count)
        if row_count > max_row_col_count:
            max_row_col_count = row_count
        if col_count > max_row_col_count:
            max_row_col_count = col_count

    if max_row_col_count == grid_size:
        return True
    else:
        return False
    
# Extend this to the multiplayer scenario - we are interested if anyone has a line

def multiplayer_line_checker():
    anyone_has_a_line = False
    # print(anyone_has_a_line)
    for name in names:
        # print(check_for_line(globals()[name + '_ticked_squares_5'],grid_size))
        if check_for_line(globals()[name + '_ticked_squares_5'],grid_size) == True:
            anyone_has_a_line = True
        else:
            pass
    return anyone_has_a_line

def multiplayer_full_house_checker(grid_size):
    anyone_has_a_full_house = False
    # print(anyone_has_a_line)
    for name in names:
        # print(len(globals()[name +'_ticked_squares_5']))
        if len(globals()[name +'_ticked_squares_5']) == (grid_size**2):
            anyone_has_a_full_house = True
        else:
            pass
    return anyone_has_a_full_house


# ### Single Game Simulation 3x3 - count the number of ticks until you have a line

# In[3]:


all_squares_3 = [[0,0],[0,1],[0,2],
                 [1,0],[1,1],[1,2],
                 [2,0],[2,1],[2,2]
                  ]

empty_squares_3 = all_squares_3

ticked_squares_3 = []

some_squares_3 = [[0,0],[0,1],     
                  [1,0]      ,[1,2],
                  [2,0]
                 ]

grid_size = 3

while check_for_line(ticked_squares_3,grid_size) == False:
    tick_count = len(ticked_squares_3)
    # Remove random element from empty squares and add it to ticked squares
    next_tick = random.choice(empty_squares_3)
    print(tick_count + 1,'Ticking:', next_tick)
    empty_squares_3.remove(next_tick)
    ticked_squares_3.append(next_tick)

print('Tick Count',tick_count+1)


# ### 3 x 3 Simulations - How many Ticks Until Line Reached?

# In[4]:


ticks_for_line_list = []
for r in range(10000):
    all_squares_3 = [[0,0],[0,1],[0,2],
                 [1,0],[1,1],[1,2],
                 [2,0],[2,1],[2,2]
                  ]
    empty_squares_3 = all_squares_3
    ticked_squares_3 = []
    grid_size = 3

    while check_for_line(ticked_squares_3,grid_size) == False:
        tick_count = len(ticked_squares_3)
        # Remove random element from empty squares and add it to ticked squares
        next_tick = random.choice(empty_squares_3)
        # print(tick_count + 1,'Ticking:', next_tick)
        empty_squares_3.remove(next_tick)
        ticked_squares_3.append(next_tick)

    # print('Tick Count',tick_count+1)
    
    ticks_for_line_list.append(tick_count+1)

ticks_for_line = pd.DataFrame(pd.DataFrame(ticks_for_line_list).rename({0:'Ticks_For_Line'},axis=1)['Ticks_For_Line'].value_counts()).reset_index().rename({'index':'Ticks','Ticks_For_Line':'First_Line_Frequency'},axis=1).sort_values('Ticks')
ticks_for_line['Prob_Line_Now'] = ticks_for_line['First_Line_Frequency']/ticks_for_line['First_Line_Frequency'].sum()
ticks_for_line['Prob_Line_by_Now'] = ticks_for_line['First_Line_Frequency'].cumsum()/ticks_for_line['First_Line_Frequency'].sum()
print('Expected Ticks for First Line:', np.mean(ticks_for_line_list))
print('Standard Deviation of Ticks for First Line:', np.std(ticks_for_line_list).round(2))
ticks_for_line


# We conclude that the expected number of ticks to get a line is around 5 on a 3x3 grid, with a Standard Deviation of around 1.
# 
# How to interpret the above table:
# 
# We see that for a 3x3 grid, there is around a 21% chance of getting your first line after 4 ticks, a 37% of getting your first line after 5 ticks. 
# 
# We also see that given you have 3 ticks, there is around a 7% you have a line or that given you have 5 ticks, there is around a 66% you have a line 

# ### 5 x 5 Simulations - How Many Ticks until Line Reached?

# In[5]:


ticks_for_line_list = []
for r in range(10000):
    #print(r)
    all_squares_5 = [[0,0],[0,1],[0,2],[0,3],[0,4],
                     [1,0],[1,1],[1,2],[1,3],[1,4],
                     [2,0],[2,1],[2,2],[2,3],[2,4],
                     [3,0],[3,1],[3,2],[3,3],[3,4],
                     [4,0],[4,1],[4,2],[4,3],[4,4]
                  ]
    empty_squares_5 = all_squares_5
    ticked_squares_5 = []
    grid_size = 5

    while check_for_line(ticked_squares_5,grid_size) == False:
        tick_count = len(ticked_squares_5)
        # Remove random element from empty squares and add it to ticked squares
        next_tick = random.choice(empty_squares_5)
        # print(tick_count + 1,'Ticking:', next_tick)
        empty_squares_5.remove(next_tick)
        ticked_squares_5.append(next_tick)

    #print('Tick Count',tick_count+1)
    
    ticks_for_line_list.append(tick_count+1)
    
ticks_for_line = pd.DataFrame(pd.DataFrame(ticks_for_line_list).rename({0:'Ticks_For_Line'},axis=1)['Ticks_For_Line'].value_counts()).reset_index().rename({'index':'Ticks','Ticks_For_Line':'First_Line_Frequency'},axis=1).sort_values('Ticks')
ticks_for_line['Prob_Line_Now'] = ticks_for_line['First_Line_Frequency']/ticks_for_line['First_Line_Frequency'].sum()
ticks_for_line['Prob_Line_by_Now'] = ticks_for_line['First_Line_Frequency'].cumsum()/ticks_for_line['First_Line_Frequency'].sum()
print('Expected Ticks for First Line:', np.mean(ticks_for_line_list))
print('Standard Deviation of Ticks for First Line:', np.std(ticks_for_line_list).round(2))
ticks_for_line


# We conclude that the expected number of ticks to get a line is around 15.3 on a 5x5 grid, with a Standard Deviation of around 2.6
# 
# How to interpret the above table:
# 
# We see that for a 5x5 grid, there is around a 14% chance of getting your first line after 15 ticks, a 1% of getting your first line after 20 ticks.
# 
# We also see that given you have 9 ticks, there is around a 5% you have a line or that given you have 17 ticks, there is around a 80% you have a line

# Now, we take a step back from the tick to line relationship. Instead, what is the expected number of calls to get a line?

# # Full Bingo Simulation (Single Player)

# I have the formula for the probability of having t ticks after c calls, so with the above as a simulated estimated, I could calculate this numerically.
# 
# Let's run a simulation instead, to avoid the large factorials which are involved!

# Single Game Simulation - 5x5 card

# In[6]:


c = 90 # The size of the calling set
grid_size = 5 # The side length of the square bingo card

# Create a list to determine the call order of the numbers
call_list = list(np.random.permutation([i+1 for i in range(c)]))

# Produce a sample of these numbers to populate our bingo card
card_list = random.sample(list(call_list),grid_size**2)

# The locations on our bingo card
all_squares_5 = [[0,0],[0,1],[0,2],[0,3],[0,4],
                 [1,0],[1,1],[1,2],[1,3],[1,4],
                 [2,0],[2,1],[2,2],[2,3],[2,4],
                 [3,0],[3,1],[3,2],[3,3],[3,4],
                 [4,0],[4,1],[4,2],[4,3],[4,4]
                ]

# Create lists of the empty and ticked squares. Note that these will complement each other. 
empty_squares_5 = all_squares_5
ticked_squares_5 = []
    
# Create a dictionary which for each number on our bingo card, gives the location on the card
card_dictionary = {card_list[i]: all_squares_5[i] for i in range(len(card_list))} 

while len(ticked_squares_5) < grid_size**2:
    
    # First play until you have a LINE
    
    while check_for_line(ticked_squares_5,grid_size) == False:
        
        line = 0 # Binary flag to record first line

        # Call the Next Number (pop removes from call_list
        this_call = call_list.pop(0) # removes the first element from call_list
        print('Number Called:', this_call)
        try:
            # Check if the called number is on our bingo card
            next_tick = card_dictionary[this_call]
            print('Location to tick:',card_dictionary[this_call])
            # Remove the location to be ticked from empty_squares to ticked_squares
            empty_squares_5.remove(next_tick)
            ticked_squares_5.append(next_tick)
        except:
            print('Not on our Bingo Card')
            pass       

        # Keep track of calls and ticks 
        call_count = c - len(call_list)
        tick_count = len(ticked_squares_5)
        print('Call Count:',call_count)
        print('Tick Count:',tick_count)
    
    if line == 0 :
        line_tick_count = tick_count
        line_call_count = call_count
        print('LINE after {} calls and {} ticks!'.format(call_count,tick_count))
    line = 1
    
    # Then keep playing until you have a FULL HOUSE!
    
    this_call = call_list.pop(0) # removes the first element from call_list
    print('Number Called:', this_call)
    try:
        # Check if the called number is on our bingo card
        next_tick = card_dictionary[this_call]
        print('Location to tick:',card_dictionary[this_call])
        # Remove the location to be ticked from empty_squares to ticked_squares
        empty_squares_5.remove(next_tick)
        ticked_squares_5.append(next_tick)
    except:
        print('Not on our Bingo Card')
        pass       

    # Keep track of calls and ticks 
    call_count = c - len(call_list)
    tick_count = len(ticked_squares_5)
    print('Call Count:',call_count)
    print('Tick Count:',tick_count)

print('FULL HOUSE after {} calls and {} ticks!'.format(call_count,tick_count))
print('Calls Until Line:',line_call_count)
print('Ticks Until Line:', line_tick_count)


# ## Full Simulation - 5x5 Grid, 10000 games

# In[483]:


c = 90 # The size of the calling set
grid_size = 5

ticks_for_line_list = []
calls_for_line_list = []
ticks_for_full_house_list = [] # Will always be 25 by definition
calls_for_full_house_list = []

for r in range(1000000):    # How many games to play
    print(r)
    
    # Create a list to determine the call order of the numbers
    call_list = list(np.random.permutation([i+1 for i in range(c)]))

    # Produce a sample of these numbers to populate our bingo card
    card_list = random.sample(list(call_list),grid_size**2)

    # The locations on our bingo card
    all_squares_5 = [[0,0],[0,1],[0,2],[0,3],[0,4],
                     [1,0],[1,1],[1,2],[1,3],[1,4],
                     [2,0],[2,1],[2,2],[2,3],[2,4],
                     [3,0],[3,1],[3,2],[3,3],[3,4],
                     [4,0],[4,1],[4,2],[4,3],[4,4]
                    ]

    empty_squares_5 = all_squares_5
    ticked_squares_5 = []

    # Create a dictionary which for each number on our bingo card, gives the location on the card
    card_dictionary = {card_list[i]: all_squares_5[i] for i in range(len(card_list))} 
    
    # Let's Play!
    while len(ticked_squares_5) < grid_size**2:
    
    # First play until you have a LINE
    
        while check_for_line(ticked_squares_5,grid_size) == False:

            line = 0 # Binary flag to record first line

            # Call the Next Number (pop removes from call_list
            this_call = call_list.pop(0) # removes the first element from call_list
            # print('Number Called:', this_call)
            try:
                # Check if the called number is on our bingo card
                next_tick = card_dictionary[this_call]
                # print('Location to tick:',card_dictionary[this_call])
                # Remove the location to be ticked from empty_squares to ticked_squares
                empty_squares_5.remove(next_tick)
                ticked_squares_5.append(next_tick)
            except:
                # print('Not on our Bingo Card')
                pass       

            # Keep track of calls and ticks 
            call_count = c - len(call_list)
            tick_count = len(ticked_squares_5)
            # print('Call Count:',call_count)
            # print('Tick Count:',tick_count)
    
        if line == 0 :
            line_tick_count = tick_count
            line_call_count = call_count
            print('LINE after {} calls and {} ticks!'.format(call_count,tick_count))
        line = 1

        # Then keep playing until you have a FULL HOUSE!

        this_call = call_list.pop(0) # removes the first element from call_list
        # print('Number Called:', this_call)
        try:
            # Check if the called number is on our bingo card
            next_tick = card_dictionary[this_call]
            # print('Location to tick:',card_dictionary[this_call])
            # Remove the location to be ticked from empty_squares to ticked_squares
            empty_squares_5.remove(next_tick)
            ticked_squares_5.append(next_tick)
        except:
            # print('Not on our Bingo Card')
            pass       

        # Keep track of calls and ticks 
        call_count = c - len(call_list)
        tick_count = len(ticked_squares_5)
        # print('Call Count:',call_count)
        # print('Tick Count:',tick_count)

    print('FULL HOUSE after {} calls and {} ticks!'.format(call_count,tick_count))
    # print(line_call_count,line_tick_count,call_count, tick_count)
    
    ticks_for_line_list.append(line_tick_count)
    calls_for_line_list.append(line_call_count)
    ticks_for_full_house_list.append(tick_count)
    calls_for_full_house_list.append(call_count)


# In[484]:


summary_df = pd.DataFrame(columns=['Players','Avg_Calls_Line','SD_Calls_Line','P20_Calls_Line','P50_Calls_Line','P80_Calls_Line',
                                   'Avg_Calls_FH','SD_Calls_FH','P20_Calls_FH','P50_Calls_FH','P80_Calls_FH'
                                  ]
                         )

distribution_df = pd.DataFrame({'Calls':[x for x in range(1,91)]})
    
new_row = {'Players': 1,
       'Avg_Calls_Line': np.mean(calls_for_line_list),
       'SD_Calls_Line': np.std(calls_for_line_list).round(2),
       'P20_Calls_Line': np.quantile(calls_for_line_list, 0.2),
       'P50_Calls_Line': np.quantile(calls_for_line_list, 0.5),
       'P80_Calls_Line': np.quantile(calls_for_line_list, 0.8),
       'Avg_Calls_FH': np.mean(calls_for_full_house_list),
       'SD_Calls_FH': np.std(calls_for_full_house_list).round(2),
       'P20_Calls_FH': np.quantile(calls_for_full_house_list, 0.2),
       'P50_Calls_FH': np.quantile(calls_for_full_house_list, 0.5),
       'P80_Calls_FH': np.quantile(calls_for_full_house_list, 0.8)
       }

summary_df = summary_df.append(new_row, ignore_index = True)

summary_df


# In[485]:


calls_for_line = pd.DataFrame(pd.DataFrame(calls_for_line_list).rename({0:'Calls_For_Line'},axis=1)['Calls_For_Line'].value_counts()).reset_index().rename({'index':'Calls','Calls_For_Line':'First_Line_Frequency'},axis=1).sort_values('Calls')
calls_for_line['Prob_Line_Now'] = calls_for_line['First_Line_Frequency']/calls_for_line['First_Line_Frequency'].sum()
calls_for_line['Prob_Line_by_Now'] = calls_for_line['First_Line_Frequency'].cumsum()/calls_for_line['First_Line_Frequency'].sum()
print('Expected Calls for First Line:', np.mean(calls_for_line_list))
print('Standard Deviation of Calls for First Line:', np.std(calls_for_line_list).round(2))
calls_for_line


# In[488]:


# calls_for_line.to_excel('Million_by_1_player_bingo.xlsx')


# We see that we expect 53.5 calls before we get a line.
# 
# After 43 Calls there is a 20% chance that we have a line.
# 
# After 63 Calls there is an 80% chance that we have a line.

# In[486]:


px.bar(calls_for_line,x='Calls',y='Prob_Line_by_Now',height=350)


# In[487]:


px.bar(calls_for_line,x='Calls',y='Prob_Line_Now',height=350)


# In[11]:


ticks_for_line = pd.DataFrame(pd.DataFrame(ticks_for_line_list).rename({0:'Ticks_For_Line'},axis=1)['Ticks_For_Line'].value_counts()).reset_index().rename({'index':'Ticks','Ticks_For_Line':'First_Line_Frequency'},axis=1).sort_values('Ticks')
ticks_for_line['Prob_Line_Now'] = ticks_for_line['First_Line_Frequency']/ticks_for_line['First_Line_Frequency'].sum()
ticks_for_line['Prob_Line_by_Now'] = ticks_for_line['First_Line_Frequency'].cumsum()/ticks_for_line['First_Line_Frequency'].sum()
print('Expected Ticks for First Line:', np.mean(ticks_for_line_list))
print('Standard Deviation of Ticks for First Line:', np.std(ticks_for_line_list).round(2))
ticks_for_line


# This is the same distribution as found in the previous section (Relationship of ticks to line prob)

# In[423]:


calls_for_full_house = pd.DataFrame(pd.DataFrame(calls_for_full_house_list).rename({0:'Calls_For_Full_House'},axis=1)['Calls_For_Full_House'].value_counts()).reset_index().rename({'index':'Calls','Calls_For_Full_House':'First_Full_House_Frequency'},axis=1).sort_values('Calls')
calls_for_full_house['Prob_full_house_Now'] = calls_for_full_house['First_Full_House_Frequency']/calls_for_full_house['First_Full_House_Frequency'].sum()
calls_for_full_house['Prob_full_house_by_Now'] = calls_for_full_house['First_Full_House_Frequency'].cumsum()/calls_for_full_house['First_Full_House_Frequency'].sum()
print('Expected Calls for First Full House:', np.mean(calls_for_full_house_list))
print('Standard Deviation of Calls for First Full House:', np.std(calls_for_full_house_list).round(2))
calls_for_full_house


# We see in 60% of cases, we have to wait until there are less than 3 numbers to go before we get a full house!
# 
# There is only a 3% chance of getting a full house after 80 out fo 90 numbers are called.

# And finally, of course, the Ticks for a full house is always 25, by definition of Full House.

# In[13]:


px.bar(calls_for_full_house,x='Calls',y='Prob_full_house_by_Now',height=350)


# # Full Bingo Simulation (Multi-Player)

# I expect that having more players will reduce the number of calls until anyone gets a line or full house. By how many calls, I don't know! This is analogous to taking the minimum of a set of n random variables.

# In[237]:


players = 20 # The number of players
games = 5 # The number of games to play
c = 90 # The size of the calling set
grid_size = 5

calls_for_line_list = []
ticks_for_full_house_list = [] # Will always be 25 by definition
calls_for_full_house_list = []

names = []
for i in range(players):
    name = 'player_{}'.format(i+1)
    names.append(name)         

for r in range(games):  
    print(r)
    
    # Create a list to determine the call order of the numbers
    call_list = list(np.random.permutation([i+1 for i in range(c)]))
    
    for name in names:
        # Produce a sample of these numbers to populate each bingo card
        globals()[name + '_card_list'] = random.sample(list(call_list),grid_size**2)
    
        # The locations on each bingo card
        globals()[name + '_all_squares_5'] = [[0,0],[0,1],[0,2],[0,3],[0,4],
                                             [1,0],[1,1],[1,2],[1,3],[1,4],
                                             [2,0],[2,1],[2,2],[2,3],[2,4],
                                             [3,0],[3,1],[3,2],[3,3],[3,4],
                                             [4,0],[4,1],[4,2],[4,3],[4,4]
                                            ]

        globals()[name + '_empty_squares_5'] = [[0,0],[0,1],[0,2],[0,3],[0,4],
                                               [1,0],[1,1],[1,2],[1,3],[1,4],
                                               [2,0],[2,1],[2,2],[2,3],[2,4],
                                               [3,0],[3,1],[3,2],[3,3],[3,4],
                                               [4,0],[4,1],[4,2],[4,3],[4,4]
                                              ]
        
        globals()[name + '_ticked_squares_5'] = []
        
        # Create a dictionary which for each number on our bingo card, gives the location on the card
        globals()[name + '_card_dictionary'] = {globals()[name + '_card_list'][i]: globals()[name + '_all_squares_5'][i] for i in range(len(globals()[name + '_card_list']))}
        
    # Let's Play!
    # while no one yet has a full house...
    while multiplayer_full_house_checker(grid_size) == False:
        
        # While no one has a line
        while multiplayer_line_checker() == False:

            line = 0 # Binary flag to record first line by anybody

            # Call the Next Number (pop removes from call_list)
            this_call = call_list.pop(0) # removes the first element from call_list
            print('Number Called:', this_call)

            # Cross this number off for each player where possible
            for name in names:
                try:
                    # Check if the called number is on our bingo card
                    next_tick = globals()[name + '_card_dictionary'][this_call]
                    # print('Location to tick:',globals()[name + '_card_dictionary'][this_call])
                    # Remove the location to be ticked from empty_squares to ticked_squares
                    globals()[name + '_empty_squares_5'].remove(next_tick)
                    globals()[name + '_ticked_squares_5'].append(next_tick)

                    globals()[name + '_tick_count'] = len(globals()[name + '_ticked_squares_5'])
                    print("On {}'s Bingo Card, Tick Count:".format(name), globals()[name + '_tick_count'])

                except:
                    print("Not on {}'s Bingo Card".format(name))
                    pass       

            # Keep track of calls
            call_count = c - len(call_list)
            print('Call Count:',call_count)


        # Break out of the while loop, when one player has a line
        if line == 0 :
            line_call_count = call_count
            print('LINE after {} calls!'.format(line_call_count))

        line = 1


        # Call the Next Number (pop removes from call_list)
        this_call = call_list.pop(0) # removes the first element from call_list
        print('Number Called:', this_call)

        # Cross this number off for each player where possible
        for name in names:
            try:
                # Check if the called number is on our bingo card
                next_tick = globals()[name + '_card_dictionary'][this_call]
                print('Location to tick:',globals()[name + '_card_dictionary'][this_call])
                # Remove the location to be ticked from empty_squares to ticked_squares
                globals()[name + '_empty_squares_5'].remove(next_tick)
                globals()[name + '_ticked_squares_5'].append(next_tick)

                globals()[name + '_tick_count'] = len(globals()[name + '_ticked_squares_5'])
                print("On {}'s Bingo Card, Tick Count:".format(name), globals()[name + '_tick_count'])
                print('Tick Count:', globals()[name + '_tick_count'])

            except:
                print("Not on {}'s Bingo Card".format(name))
                pass       

        # Keep track of calls
        call_count = c - len(call_list)
        print('Call Count:',call_count)

    print('FULL HOUSE after {} calls and {} ticks!'.format(call_count,tick_count))
    
    calls_for_line_list.append(line_call_count)
    ticks_for_full_house_list.append(tick_count)
    calls_for_full_house_list.append(call_count)


# In[238]:


calls_for_line_list, ticks_for_full_house_list, calls_for_full_house_list        


# In[239]:


calls_for_line = pd.DataFrame(pd.DataFrame(calls_for_line_list).rename({0:'Calls_For_Line'},axis=1)['Calls_For_Line'].value_counts()).reset_index().rename({'index':'Calls','Calls_For_Line':'First_Line_Frequency_{}'.format(players)},axis=1).sort_values('Calls')
calls_for_line


# In[210]:


calls_for_line['Prob_Line_Now'] = calls_for_line['First_Line_Frequency']/calls_for_line['First_Line_Frequency'].sum()
calls_for_line['Prob_Line_by_Now'] = calls_for_line['First_Line_Frequency'].cumsum()/calls_for_line['First_Line_Frequency'].sum()
print('Expected Calls for First Line:', np.mean(calls_for_line_list))
print('Standard Deviation of Calls for First Line:', np.std(calls_for_line_list).round(2))
calls_for_line


# ## Let's Try Bigger Scale
# 
# Use the number of players as a variable - experimentally find the expected number of calls before a line and a full house.
# 
# Try 100 games to begin with, package the above code as a function, and return the resulting distributions in a dataframe, with each column notating a different number of players.

# In[404]:


def n_player_bingo(players):   
    global calls_for_line_list, calls_for_full_house_list, names
    players = players # The number of players
    games = 1000 # The number of games to play
    c = 90 # The size of the calling set
    grid_size = 5

    calls_for_line_list = []
    ticks_for_full_house_list = [] # Will always be 25 by definition
    calls_for_full_house_list = []

    names = []
    for i in range(players):
        name = 'player_{}'.format(i+1)
        names.append(name)         

    for r in range(games):  
        # print(r)

        # Create a list to determine the call order of the numbers
        call_list = list(np.random.permutation([i+1 for i in range(c)]))

        for name in names:
            # Produce a sample of these numbers to populate each bingo card
            globals()[name + '_card_list'] = random.sample(list(call_list),grid_size**2)

            # The locations on each bingo card
            globals()[name + '_all_squares_5'] = [[0,0],[0,1],[0,2],[0,3],[0,4],
                                                 [1,0],[1,1],[1,2],[1,3],[1,4],
                                                 [2,0],[2,1],[2,2],[2,3],[2,4],
                                                 [3,0],[3,1],[3,2],[3,3],[3,4],
                                                 [4,0],[4,1],[4,2],[4,3],[4,4]
                                                ]

            globals()[name + '_empty_squares_5'] = [[0,0],[0,1],[0,2],[0,3],[0,4],
                                                   [1,0],[1,1],[1,2],[1,3],[1,4],
                                                   [2,0],[2,1],[2,2],[2,3],[2,4],
                                                   [3,0],[3,1],[3,2],[3,3],[3,4],
                                                   [4,0],[4,1],[4,2],[4,3],[4,4]
                                                  ]

            globals()[name + '_ticked_squares_5'] = []

            # Create a dictionary which for each number on our bingo card, gives the location on the card
            globals()[name + '_card_dictionary'] = {globals()[name + '_card_list'][i]: globals()[name + '_all_squares_5'][i] for i in range(len(globals()[name + '_card_list']))}

        # Let's Play!
        # while no one yet has a full house...
        while multiplayer_full_house_checker(grid_size) == False:

            # While no one has a line
            while multiplayer_line_checker() == False:

                line = 0 # Binary flag to record first line by anybody

                # Call the Next Number (pop removes from call_list)
                this_call = call_list.pop(0) # removes the first element from call_list
                # print('Number Called:', this_call)

                # Cross this number off for each player where possible
                for name in names:
                    try:
                        # Check if the called number is on our bingo card
                        next_tick = globals()[name + '_card_dictionary'][this_call]
                        # print('Location to tick:',globals()[name + '_card_dictionary'][this_call])
                        # Remove the location to be ticked from empty_squares to ticked_squares
                        globals()[name + '_empty_squares_5'].remove(next_tick)
                        globals()[name + '_ticked_squares_5'].append(next_tick)

                        globals()[name + '_tick_count'] = len(globals()[name + '_ticked_squares_5'])
                        # print("On {}'s Bingo Card, Tick Count:".format(name), globals()[name + '_tick_count'])

                    except:
                        # print("Not on {}'s Bingo Card".format(name))
                        pass       

                # Keep track of calls
                call_count = c - len(call_list)
                # print('Call Count:',call_count)


            # Break out of the while loop, when one player has a line
            if line == 0 :
                line_call_count = call_count
                # print('LINE after {} calls!'.format(line_call_count))

            line = 1


            # Call the Next Number (pop removes from call_list)
            this_call = call_list.pop(0) # removes the first element from call_list
            # print('Number Called:', this_call)

            # Cross this number off for each player where possible
            for name in names:
                try:
                    # Check if the called number is on our bingo card
                    next_tick = globals()[name + '_card_dictionary'][this_call]
                    # print('Location to tick:',globals()[name + '_card_dictionary'][this_call])
                    # Remove the location to be ticked from empty_squares to ticked_squares
                    globals()[name + '_empty_squares_5'].remove(next_tick)
                    globals()[name + '_ticked_squares_5'].append(next_tick)

                    globals()[name + '_tick_count'] = len(globals()[name + '_ticked_squares_5'])
                    # print("On {}'s Bingo Card, Tick Count:".format(name), globals()[name + '_tick_count'])

                except:
                    # print("Not on {}'s Bingo Card".format(name))
                    pass       

            # Keep track of calls
            call_count = c - len(call_list)
            # print('Call Count:',call_count)

        # print('FULL HOUSE after {} calls and {} ticks!'.format(call_count,tick_count))

        calls_for_line_list.append(line_call_count)
        ticks_for_full_house_list.append(tick_count)
        calls_for_full_house_list.append(call_count)


# In[412]:


## After each extra player is added:
# - Record the summary stats (mean, SD, Percentiles of calls until first line and until first FH)
# Create a df of the distribution of these values. This table will be a cool plot moving to the left as n increases

summary_df = pd.DataFrame(columns=['Players','Avg_Calls_Line','SD_Calls_Line','P20_Calls_Line','P50_Calls_Line','P80_Calls_Line',
                                   'Avg_Calls_FH','SD_Calls_FH','P20_Calls_FH','P50_Calls_FH','P80_Calls_FH'
                                  ]
                         )

distribution_df = pd.DataFrame({'Calls':[x for x in range(1,91)]})

player_list = [x for x in range(3,21)] + [30,40,50,100] # Try these numbers of players

for attendance in player_list:     
    print('ATTENDANCE:',attendance)
    n_player_bingo(attendance)
    # print(calls_for_line_list, calls_for_full_house_list)
    
    new_row = {'Players': attendance,
           'Avg_Calls_Line': np.mean(calls_for_line_list),
           'SD_Calls_Line': np.std(calls_for_line_list).round(2),
           'P20_Calls_Line': np.quantile(calls_for_line_list, 0.2),
           'P50_Calls_Line': np.quantile(calls_for_line_list, 0.5),
           'P80_Calls_Line': np.quantile(calls_for_line_list, 0.8),
           'Avg_Calls_FH': np.mean(calls_for_full_house_list),
           'SD_Calls_FH': np.std(calls_for_full_house_list).round(2),
           'P20_Calls_FH': np.quantile(calls_for_full_house_list, 0.2),
           'P50_Calls_FH': np.quantile(calls_for_full_house_list, 0.5),
           'P80_Calls_FH': np.quantile(calls_for_full_house_list, 0.8)
           }

    summary_df = summary_df.append(new_row, ignore_index = True)
    
    calls_for_line = pd.DataFrame({'Calls' : calls_for_line_list})['Calls'].value_counts().reset_index().rename({'index':'Calls','Calls':'Calls_for_Line_{}'.format(attendance)},axis=1)
    calls_for_full_house = pd.DataFrame({'Calls' : calls_for_full_house_list})['Calls'].value_counts().reset_index().rename({'index':'Calls','Calls':'Calls_for_FH_{}'.format(attendance)},axis=1)
    distribution_df = distribution_df.merge(calls_for_line,how='outer',on='Calls').merge(calls_for_full_house, how='outer', on='Calls').fillna(0)
    


# In[413]:


summary_df


# In[437]:


distribution_df


# This is producing 427000 bingo cards!

# In[416]:


# summary_df.to_excel('Bingo_Summary.xlsx',index=False)


# In[417]:


# distribution_df.to_excel('Bingo_Distribution.xlsx',index=False)


# ### Adding in the distribution for single player

# In[471]:


# calls_for_line_df = calls_for_line[['Calls','First_Line_Frequency']].rename({'First_Line_Frequency':'Calls_for_Line_1'},axis=1)
# calls_for_line_df.head(2)

# calls_for_full_house_df = calls_for_full_house[['Calls','First_Full_House_Frequency']].rename({'First_Full_House_Frequency':'Calls_for_FH_1'},axis=1)
# calls_for_full_house_df.head(2)

# distribution_df = distribution_df.merge(calls_for_line_df,how='outer',on='Calls').merge(calls_for_full_house_df, how='outer', on='Calls').fillna(0)
# distribution_df

# distribution_df.to_excel('Bingo_Distribution.xlsx',index=False)


# ## Animated Plot as players increases?

# In[475]:


distribution_df = pd.read_excel('Bingo_Distribution.xlsx')


# In[477]:


distribution_df.head(2)


# In[474]:


fig = go.Figure()
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_1']/1000, fill='tozeroy'  , name="1 Player"))
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_3']/1000, fill='tozeroy'  , name="3 Players"))
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_10']/1000, fill='tozeroy' , name="10 Players"))
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_20']/1000, fill='tozeroy' , name="20 Players"))
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_50']/1000, fill='tozeroy' , name="50 Players"))
fig.add_trace(go.Scatter(x = distribution_df['Calls'], y = distribution_df['Calls_for_Line_100']/1000, fill='tozeroy', name="100 Players"))

fig.update_layout(title = 'Distribution of number of calls before first Line: 1, 3, 10, 20, 50, 100  players',
                  xaxis_title = 'Number of Calls Until First Line',
                  yaxis_title = 'Probability',
                  height = 400)
fig.show()


# Lesson: If you run a bingo hall, and people pay for a set number of games, the more people the better.

# ### END
