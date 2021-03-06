# COVID 19
### Dependencies:
```console
 pip install -r requirements.txt
```

### How To Use:
#### Command:
```console
 python main.py $option1 $option2 $country1 $country2 ... $countryN 
```
#### Option1:
- d : Total Deaths
- c : Total Confirmed Cases
- dd : Daily Deaths
- cd : Daily Confirmed Cases

#### Option2:
- time : The X axis are dates.
- max : The X axis represent the days after the first death/confirmed case of every country, the focus is on the country with more days.
- min : The focus is on the country with less days.


### Examples:
```console
 python main.py d max US Italy Spain
```
![alt text](https://github.com/Joaquin98/Covid-19/blob/master/Examples/US_Spain_Italy.png "Logo Title Text 1")

```console
 python main.py d time Italy China
```
![alt text](https://github.com/Joaquin98/Covid-19/blob/master/Examples/China_Italy.png "Logo Title Text 1")

```console
 python main.py c min Italy Brazil
```
![alt text](https://github.com/Joaquin98/Covid-19/blob/master/Examples/Italy_Brazil.png "Logo Title Text 1")
