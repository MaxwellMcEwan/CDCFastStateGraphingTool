import matplotlib.pyplot as plt
# LIST OF YEARS DATA INCLUDES
yearList = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# SORTED CATERGORIES + LIST FOR ALGO
suicides = []
homocides = []
circulatoryDisease = []
transportAccident = []
massShootings = []

deathCatergories = [suicides, homocides, circulatoryDisease, transportAccident,massShootings]

# DATA FILE NAMES + LIST FOR ALGO
suicideDataFile = 'suicideData.txt'
homocideDataFile = 'homocideData.txt'
heartDiseaseDataFile = 'heartDiseaseData.txt'
transportAccidentDataFile = 'transportAccidentData.txt'
massShootingsDataFile = 'massShootingData.txt'

dataFiles = [suicideDataFile, homocideDataFile, heartDiseaseDataFile, transportAccidentDataFile, massShootingsDataFile]

# DEATH NUM LISTS
RAWdeathNumbers = []
deathNumbers = []

# GET RAW DATA FROM THE FILES
for i in range(len(dataFiles)):
    RAWdeathNumbers.append(open(dataFiles[i], 'r').readlines())

# FILTER DATA AND REMOVE \n FROM NUMBERS
for list in RAWdeathNumbers:
    for deathStat in list:
        deathStat = deathStat[:-1]
        deathNumbers.append(int(deathStat))

# CATERGORY MODIFIER
catergoryModifier = 0

# SORT FILTERED DEATH NUMS INTO CATERGORIES
for catergory in deathCatergories:
    for year in range(21):
        catergory.append(deathNumbers[year + catergoryModifier])

    catergoryModifier += 21

# LIST OF DATA WE WANT TO PLOT
listToPlot = [suicides, homocides, transportAccident, massShootings, circulatoryDisease]

# PLOT THE DATA
for list in listToPlot:
    plt.plot(yearList, list)

plt.show()

plt.plot(yearList, suicides)
plt.plot(yearList, homocides)
plt.plot(yearList, transportAccident)
#plt.plot(yearList, circulatoryDisease)
plt.show()
