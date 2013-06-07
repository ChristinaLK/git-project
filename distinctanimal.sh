  
# get dates of distinct animal sightings
grep $1 ./data/sightings.csv | cut -d , -f 1  > ./results/$1.dat
 
