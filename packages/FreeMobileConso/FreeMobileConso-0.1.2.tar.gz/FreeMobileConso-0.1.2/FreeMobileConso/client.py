
import requests
from bs4 import BeautifulSoup

from . import dataClassification

class Client:
    """
    Class to get information about your Free Mobile account
    
    Parameters
    ----------
    identifiant : str
        Your Free Mobile identifiant
    password : str
        Your Free Mobile password

    Functions
    ---------
    getConsoDict()
        Return a dict with all information about your Free Mobile account
    consomation()
        Return a object with all information about your Free Mobile account
        
    """
    
    def __init__(self, identifiant, password):
        # Set the identifiant and password
        self.identifiant = identifiant
        self.password = password
        # Set the payload
        self.payload = {
            "login-ident": self.identifiant,
            "login-pwd": self.password,
            "bt-login": "1"
        }
        # Set the session
        self.session = requests.Session()
        # Set the headers of the session
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        # Set the url of the login page
        self.urlLogin = "https://mobile.free.fr/account/"
        # Information to grab
        listOfInternetInforamtion = ["conso", "consoMax", "remaining", "excludingPackage", "carbonFootprint"]
        listOfAppelInforamtion = ["conso", "consoMax", "callToMyCountry", "callToInternational", "excludingPackage"]
        listOfSMSInforamtion = ["conso", "consoMax", "maxNbSMS", "nbSMS", "excludingPackage"]
        listOfMMSInforamtion = ["conso", "consoMax", "maxNbMMS", "nbMMS", "excludingPackage"]
        # Set the dict of all information
        self.dictOfAllInformation = {
            "internet": listOfInternetInforamtion,
            "call": listOfAppelInforamtion,
            "SMS": listOfSMSInforamtion,
            "MMS": listOfMMSInforamtion
        }
                    
    

    def getConsoDict(self) -> dict:
        """
        getConsoDict()
        ---------------
        Return a dict with all information about your Free Mobile account
        """
        # Send the request
        req = self.session.post(self.urlLogin, data=self.payload)
        # Get the soup
        soup = BeautifulSoup(req.content, "html.parser")
        # Get the user information
        userInfo = soup.find("div", {"class": "current-user__infos"})
        # Get the name of the account, try to get the name of the account, if it doesn't work, raise an exception "Identifiant or password is incorrect"
        try:
            nameAcount = userInfo.find("div", {"class": "identite_bis"}).text.strip()
        except:
            raise Exception("Identifiant or password is incorrect")

        # Get name, identifiant, ligne and date
        nameAcount = userInfo.find("div", {"class": "identite_bis"}).text.strip()
        identifiant = userInfo.findAll("div", {"class": "smaller"})[0].text.strip()
        ligne = userInfo.findAll("div", {"class": "smaller"})[1].text.strip()
        date = soup.find("div", {"class": "details"}).find("div", {"class": "sub-title"}).text.strip()
        
        
        result= {}
        # Get the information about the internet, call, SMS and MMS in roaming and local
        for _ in range(2):
            
            # Get the div where the information is
            place = soup.find("div", {"class": "conso-local"}) if _ == 0 else soup.find("div", {"class": "conso-roaming"})
            # Prepare the dict
            result[place["class"][1].split("-")[1]] = {}
            
            # Get the information about the internet, call, SMS and MMS
            for key, value in self.dictOfAllInformation.items():
                
                if key == "internet": itteration = 0
                elif key == "call": itteration = 1
                elif key == "SMS": itteration = 2
                elif key == "MMS": itteration = 3
                
                result[place["class"][1].split("-")[1]][key] = {}
                result[place["class"][1].split("-")[1]][key][value[0]] = place.findAll("div", {"class": "number-circle"})[itteration].find("span").text.strip().replace("*","")
    
                dataSecondValue = place.findAll("div", {"class": "number-circle"})[itteration].find("p").text.strip().replace("*","")

                if "/" in dataSecondValue:
                    result[place["class"][1].split("-")[1]][key][value[1]] = dataSecondValue.split("/")[1]
                else:
                    result[place["class"][1].split("-")[1]][key][value[1]] = dataSecondValue

                if result[place["class"][1].split("-")[1]][key][value[1]] == "": 
                    result[place["class"][1].split("-")[1]][key][value[1]] = result[place["class"][1].split("-")[1]][key][value[0]]
                result[place["class"][1].split("-")[1]][key][value[2]] = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")[0].find("span").text.replace("/ ", "").strip().replace("*","")
                thirdInformation = result[place["class"][1].split("-")[1]][key][value[3]] = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")
                lastInternetAppelInformation = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")
                lastSMSMMSInformation = place.findAll("div", {"class": "text-conso-content"})[itteration].findAll("p")[1].text.strip().split(": ")[1].replace("*","")
                if key == "internet":
                    
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[1].text.strip().split(": ")[1].replace("*","")
                    
                elif key == "call":
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[1].text.strip().split(": ")[1].replace("*","")
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastInternetAppelInformation[2].text.strip().split(": ")[1].replace("*","")
                    
                else:
                    result[place["class"][1].split("-")[1]][key][value[3]] = thirdInformation[0].text.strip().split(" / ")[0].replace("*","")
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastSMSMMSInformation
                
                if key == "internet" and place["class"][1].split("-")[1] == "local":
                    result[place["class"][1].split("-")[1]][key][value[4]] = lastInternetAppelInformation[2].text.strip().split(": ")[1].replace("*","")
            
        # Initialize the totalExcludingPackage
        result["totalExcludingPackage"] = 0
        for key, value in result.items():
            if key == "local" or key == "roaming":
                for key2, value2 in value.items():
                    for key3, value3 in value2.items():
                        if key3 == "excludingPackage":
                            result["totalExcludingPackage"] += float(value3.replace("€", ""))
        
        result["totalExcludingPackage"] = str(result["totalExcludingPackage"]) + "€"
        result["nameAcount"] = nameAcount
        result["identifier"] = identifiant.split(" : ")[1]
        result["number"] = ligne.split(" : ")[1].replace(" ", "")
        result["date"] = date
        
        return result
    
    def consommation(self) -> object:
        """
        consommation()
        --------------
        Return a object with all information about your Free Mobile account
        """
        # Return the object
        return dataClassification.Classification(self.getConsoDict())
        
