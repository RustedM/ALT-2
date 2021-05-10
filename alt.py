import statistics
import matplotlib.pyplot as plt
import numpy as np

#creates lists of runtime and rating
file=open("runtime.csv","r")  
runtime=file.read()  
file.close() 

file=open("rating.csv","r")  
rating=file.read()  
file.close()  

#the variables used in the code
counter = 0
above = 0 
below = 0 
ascore = 0 
bscore = 0 
tick = 0 
ticker = 0
arating = []
brating = []

#divides the data
runtime = runtime.split("\n") 
rating = rating.split("\n")

#removes blank items
rating = rating[:-1] 
runtime = runtime[:-1]
rating = rating[1:] 
runtime = runtime[1:] 

#converts items to floats
rating = [float(item) for item in rating] 
runtime = [float(item) for item in runtime]

#removes negative items and their corresponding runtimes
for item in rating:
    counter += 1
    if item<0: 
        rating.remove(item)
        runtime = runtime[:counter-1] + runtime[counter:]

#removes negative items and their corresponding ratings
for item in runtime:
    counter += 1
    if item<0: 
        runtime.remove(item)
        rating = rating[:counter-1] + rating[counter:]

#counts the amount above and below
for item in runtime: 
    if item >= 120.0: 
        above += 1 
    else: 
        below += 1 

#total amounts
for item in rating: 
    ticker = runtime[tick] 
    if ticker >= 120.0: 
        ascore += item
        arating.append(item)
    else: 
        bscore += item
        brating.append(item)
    tick += 1 

#averages
amean = round(ascore/above,1)
bmean = round(bscore/below,1)

amode = statistics.mode(arating)
bmode = statistics.mode(brating)

arating.sort(reverse=True)
brating.sort(reverse=True)

amax = arating[0]
bmax = brating[0]

amin = arating[-1]
bmin = brating[-1]

if len(arating) %2==0: 
    middlePlusOne=len(arating)//2 
    amedian=(arating[middlePlusOne-1]+arating[middlePlusOne])/2 
else: 
    middle=len(arating)//2 
    amedian=arating[middle]

if len(brating) %2==0: 
    middlePlusOne=len(brating)//2 
    bmedian=(brating[middlePlusOne-1]+brating[middlePlusOne])/2 
else: 
    middle=len(brating)//2 
    bmedian=brating[middle]  

#printing results
print("Amount of Movies Over 2 Hours in Top 1000: " + str(above)) 
print("Amount of Movies Under 2 Hours in Top 1000: " + str(below)) 
print(" ") 
print("Mean Rating of Movies Over 2 Hours: " + str(amean)) 
print("Mean Rating of Movies Under 2 Hours: " + str(bmean))
print(" ")
print("Mode Rating of Movies Over 2 Hours: " + str(amode)) 
print("Mode Rating of Movies Under 2 Hours: " + str(bmode))
print(" ")
print("Median Rating of Movies Over 2 Hours: " + str(amedian)) 
print("Median Rating of Movies Under 2 Hours: " + str(bmedian))
print(" ")
print("Max Rating of Movies Over 2 Hours: " + str(amax)) 
print("Max Rating of Movies Under 2 Hours: " + str(bmax))
print(" ")
print("Minimum Rating of Movies Over 2 Hours: " + str(amin)) 
print("Minimum Rating of Movies Under 2 Hours: " + str(bmin))

#pie chart
activities = ['Over 2 Hours', 'Under 2 Hours']

slices = [above, below]

colors = ['#fb2554', '#1e85ac']

plt.pie(slices, labels = activities, colors=colors,
        startangle=90,
        radius = 1.2, autopct = '%1.1f%%')

centre_circle = plt.Circle((0,0),0.70,fc='#fcb324')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.legend()
plt.show()

#bar chart
plt.style.use('ggplot')
n = 5
graphabove= (amax, amin, amedian, amode, amean)
graphbelow = (bmax, bmin, bmedian, bmode, bmean)
fig, ax = plt.subplots()
index = np.arange(n)
bar_width = 0.35
opacity = 0.9
ax.bar(index, graphabove, bar_width, alpha=opacity, color='#fb2554',
                label='Above 2 Hours')
ax.bar(index+bar_width, graphbelow, bar_width, alpha=opacity, color='#1e85ac',
                label='Below 2 Hours')
ax.set_xlabel('')
ax.set_ylabel('Rating')
ax.set_title('Movie Ratings')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Max','Min','Median','Mode','Mean'
    ))
ax.legend()
plt.show()