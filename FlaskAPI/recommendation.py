import datetime

def getDOB(input_dob):
    month = int(input_dob[0:2])
    day = int(input_dob[3:5])
    year = int(input_dob[6:10])
    dob = datetime.date(year, month, day)
    return dob


def addTime(dob, months):

    maxday = {
            1:31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12:31
        }

    m = dob.month
    d = dob.day
    yr = dob.year

    m += months
    yr += + int(months/12)

    m -= 1
    m = m%12
    m += 1

    if d > maxday[m]:
        d = 0
        m += 1
        if m == 12:
            m = 1

    new_date = datetime.date(yr, m, d)
    return new_date


def dateToString(date):
    return "" + date.month + "/" + date.day + "/"  + date.year + " "


def allergyResponse(vName):
    res = "Due to history of post-vaccination anaphylaxis due to the " + vName + " vaccine, further does may not be recommended."
    res += "\nPlease talk to a medical provider for futher information."
    return res


def immunocompResponse(vName):
    res = "Immunocompromised staus may prevent individual from taking live-attentuated vaccines."
    res += "\nThus, " + vName + " may not be recommended."
    res += "\nPlease contact a medical provider for addition information."
    return res


class Person:

    def __init__ (self, dob, allergy, immunocompromised, sex):
        
        self.dob = getDOB(dob)                         # datetime object
        self.allergy = allergy                         # allergy list
        self.immunocompromised = immunocompromised     # boolean of immunocompromised
        self.sex = sex                                 # gender
        self.age = int ((datetime.date.today() - self.dob).days / 365)

    def HepB(self):
        # birth, 1-2, 3-6
        vName = "Hepatitis B"
        if "HepB" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(self.dob) + " at birth\n"
            dateString += str(addTime(self.dob, 1)) + " at 1 month\n"
            dateString += str(addTime(self.dob, 3)) + " at 3 months\n"

        dict = {
            "Name": vName,
            "dInfo": "Hepatitis B is an infection of the liver that can cause lasting damage. It can lead to chronic infection lasting over 6 months, and children are more susceptible to such illness. It can lead to cirrhosis, a scarring of the liver, and increase chances of liver failure if left untreated. Fortunately, it is a vaccine preventable disease, and ​most people who are vaccinated with the Hepatitis B Vaccine are immune for life.",
            "vInfo": "The Hepatitis B Vaccine typically comes in a 3-dose series in the months after birth. It is a subunit vaccine.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/vaccines/hcp/vis/vis-statements/hep-b.html","https://www.mayoclinic.org/diseases-conditions/hepatitis-b/symptoms-causes/syc-20366802", "https://en.wikipedia.org/wiki/Hepatitis_B_vaccine"]
        }
        
        return dict

    def RV(self):
        # 2, 4, 6
        vName = "Rotavirus"
        if "RV" in self.allergy:
            dateString = allergyResponse(vName)
        elif self.immunocompromised:
            dateString = immunocompResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 2)) + " at 2 months\n"
            dateString += str(addTime(self.dob, 4)) + " at 4 months\n"
            dateString += str(addTime(self.dob, 6)) + " at 6 months\n"

        dict = {
            "Name": vName,
            "dInfo": "Rotavirus is a highly contagious intestinal illness that causes severe diarrhea and fluid loss. While it can usually be treated with extra fluids and prevented with proper hygiene like hand-washing, a Rotavirus vaccine regimen can avoid unnecessary harm.",
            "vInfo": "The Rotavirus vaccine is typically 3 doses administered orally. It is highly effective in preventing disease occurrence. It is a live-attenuated vaccine.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/rotavirus/index.html","https://www.mayoclinic.org/diseases-conditions/rotavirus/symptoms-causes/syc-20351300"]
        }

        return dict

    def DTaP(self):
        # 2, 4, 6, 15, 48
        vName = "Diphtheria Tetanus Acellular Pertussis"
        if "DTaP" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 2)) + " at 2 months\n"
            dateString += str(addTime(self.dob, 4)) + " at 4 months\n"
            dateString += str(addTime(self.dob, 6)) + " at 6 months\n"
            dateString += str(addTime(self.dob, 15)) + " at 15 months\n"
            dateString += str(addTime(self.dob, 48)) + " at 4 years\n"

        dict = {
            "Name": vName,
            "dInfo": "The DTaP vaccine protects against 3 bacterial illnesses: Diphtheria, Tetanus, and Pertussis. Diphtheria causes difficulty breathing and heart failure in severe cases. Tetanus spread through cuts, usually from metal objects. Tetanus leads to muscle stiffening, difficulty swallowing, and potentially paralysis. Pertussis, commonly called the whooping cough, causes respiratory trouble and violent coughing. The DTaP vaccine can successfully prevent these bacterial infections.",
            "vInfo": "DTaP is a combination vaccine that prepares the body for bacterial toxins. It comes 5 doses during childhood, but boosters are needed periodically throughout life to ensure immunity. ",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/vaccines/hcp/vis/vis-statements/dtap.html","https://www.health.ny.gov/diseases/communicable/diphtheria/fact_sheet","https://www.webmd.com/vaccines/tdap-vaccine-for-adults"]
        }

        return dict

    def HiB(self):
        # 2, 4, 6, 12
        vName = "Haemophilus Influenzae Type B"
        if "Hib" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 2)) + " at 2 months\n"
            dateString += str(addTime(self.dob, 4)) + " at 4 months\n"
            dateString += str(addTime(self.dob, 6)) + " at 6 months\n"
            dateString += str(addTime(self.dob, 12)) + " at 12 months\n"

        dict = {
            "Name": vName,
            "dInfo": "Haemophilus Influenzae Type B is a host of bacterial infection that can lead to a range of conditions. These conditions can include but are not limited to: Pneumonia, Bloodstream infection, Meningitis, and Infectious arthritis. It can also be a cause of ear infections.",
            "vInfo": "The Hib vaccine is a polysaccharide conjugate vaccine, a type of inactivated bacterial vaccine. It provides immunity through a 4-vaccine regimen.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/hi-disease/about/types-infection.html","https://www.cdc.gov/vaccines/vpd/hib/hcp/"]
        }
        return dict

    def PCV(self):
        # 2, 4, 6, 12
        vName = "Pneumococcal Conjugate Vaccine"
        if "PCV13" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 2)) + " at 2 months\n"
            dateString += str(addTime(self.dob, 4)) + " at 4 months\n"
            dateString += str(addTime(self.dob, 6)) + " at 6 months\n"
            dateString += str(addTime(self.dob, 12)) + " at 12 months\n"

        dict = {
            "Name": vName,
            "dInfo": "The PCV13 vaccine protects against Pneumococcal disease. This is a bacterially induced respiratory illness that causes severe coughing and breathing difficulty when it infects the lungs as Pneumonia. It can also cause sinus infections and meningitis. The PCV13 vaccine can prevent illness and reduce severity of infection.",
            "vInfo": "PCV13 is a conjugate vaccine. It is administered in 4 doses in the year following birth.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/pneumococcal/","https://kidshealth.org/en/parents/pneumococcal-vaccine.html","https://www.cdc.gov/vaccines/schedules/hcp/imz/child-adolescent.html"]
        }

        return dict

    def IPV(self):
        # 2, 4, 6, 48
        vName = "Inactivated Polio Vaccine"
        if "IPV" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 2)) + " at 2 months\n"
            dateString += str(addTime(self.dob, 4)) + " at 4 months\n"
            dateString += str(addTime(self.dob, 6)) + " at 6 months\n"
            dateString += str(addTime(self.dob, 48)) + " at 4 years\n"

        dict = {
            "Name": vName,
            "dInfo": "The inactivated Polio Vaccine prevents the poliovirus. Polio, also known as Poliomyelitis is a viral infection that can infect an individual's brain and spinal cord. This can lead to permanent paralyzation and death. Polio is highly contagious. Fortunately, the IPV can provide immunity against the disease. ",
            "vInfo": "The IPV vaccine (the one administered in the United States) is an intramuscular shot in the arm or leg. Other countries use oral polio vaccines as well. IPV uses an inactivated form of Polio.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/vaccines/vpd/polio/index.html","https://www.mayoclinic.org/diseases-conditions/polio/symptoms-causes/syc-20376512"]
        }

        return dict

    def Flu(self):
        pass

    def MMR(self):
        # 12, 48
        vName = "Measles Mumps Rubella"
        if "MMR" in self.allergy:
            dateString = allergyResponse(vName)
        elif self.immunocompromised:
            dateString = immunocompResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 12)) + " at 12 months\n"
            dateString += str(addTime(self.dob, 48)) + " at 4 years\n"

        dict = {
            "Name": vName,
            "dInfo": "The MMR Vaccine is a vaccine that protects against measles, mumps, rubella. These diseases are highly contagious viral infections. Measles causes fever and cough and has a high fatality rate among small children. Mumps causes swelling of the salivary gland and potentially hearing loss. Mumps outbreaks still occur among unvaccinated populations. Rubella causes a distinctive red rash and congenital birth defects. ",
            "vInfo": "The MMR vaccine is a combined vaccine that protects against all 3 viruses. It is a live-attenuated vaccine. ",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/vaccines/vpd/mmr/public/index.html#what-is-mmr","https://www.mayoclinic.org/diseases-conditions/measles/symptoms-causes/syc-20374857","https://www.mayoclinic.org/diseases-conditions/rubella/symptoms-causes/syc-20377310","https://www.mayoclinic.org/diseases-conditions/mumps/symptoms-causes/syc-20375361"]
        }

        return dict

    def Varicella(self):
        # 12, 48
        vName = "Varicella"
        if "VAR" in self.allergy:
            dateString = allergyResponse(vName)
        elif self.immunocompromised:
            dateString = immunocompResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 12)) + " at 12 months\n"
            dateString += str(addTime(self.dob, 48)) + " at 4 years\n"

        dict = {
            "Name": vName,
            "dInfo": "Varicella (more commonly referred to as Chicken Pox) is a highly infectious disease caused by a virus. The first symptoms of varicella are rashes that break out on the skin anywhere from 10-21 days after initial infection.",
            "vInfo": "Two doses of the Varicella Vaccine are 90% effective at preventing the disease. Children should receive two doses of the vaccine—the first dose at 12 through 15 months old and a second dose at 4 through 6 years old.",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/chickenpox/hcp/","https://www.cdc.gov/vaccines/vpd/varicella/"]
        }

        return dict

    def HepA(self):
        # 12, 18
        vName = "Hepatitis A"
        if "HepA" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 12)) + " at 12 months\n"
            dateString += str(addTime(self.dob, 18)) + " at 18 months\n"

        dict = {
            "Name": vName,
            "dInfo": "The Hepatitis A Vaccine prevents the liver infection caused by the Hepatitis A virus. The Hepatitis A virus can be found in an individual’s blood or stool. This virus is very contagious and can spread through ingestion (eating or drinking contaminated food/drink). Symptoms such as jaundice, nausea, stomach pain, and fatigue can last up to 2 months. ",
            "vInfo": "The Hepatitis A vaccine is an inactivated virus vaccine. A regimen of 2 doses provides immunity from the disease. ",
            "Dates": dateString,
            "Cite": ["https://www.cdc.gov/hepatitis/hav/","https://en.wikipedia.org/wiki/Hepatitis_A_vaccine"]
        }

        return dict

    def TDaP(self):
        pass

    def HPV(self):
        # 132, 138
        vName = "Human Papillomavirus"
        if "HPV" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 132)) + " at 11 years\n"
            dateString += str(addTime(self.dob, 138)) + " at 11 years, 6 months\n"

        dict = {
            "Name": vName,
            "dInfo": "Human Papillomavirus refers to a multitude of pathogens within that category. They commonly cause warts of the skin. HPV spreads through sexual or skin-skin contact. Some strains of the virus can lead to cancerous growths.Thus, it is important to be vaccinated to reduce the risk of complications.",
            "vInfo": "The HPV vaccine is a non-infectious recombinant vaccine. It is intended to protect against 9 of the most threatening stains of the virus. ",
            "Dates": dateString,
            "Cite": ["https://www.mayoclinic.org/diseases-conditions/hpv-infection/symptoms-causes/syc-20351596","https://www.cdc.gov/vaccines/vpd/hpv/hcp/"]
        }

        return dict


    def MenACYW(self):
        # 132, 192
        vName = "Meningitis ACYW"
        if "MenACYW" in self.allergy:
            dateString = allergyResponse(vName)
        else:
            dateString = "Recommended time to get vaccinated: \n\n"
            dateString += str(addTime(self.dob, 132)) + " at 11 years\n"
            dateString += str(addTime(self.dob, 192)) + " at 16 years\n"

        dict = {
            "Name": vName,
            "dInfo": "Meningitis refers to the bacterial infection of the brain and spinal cord. It can infect the bloodstream and lead to life-threatening disease. Meningitis infection is highly contagious and can occur in an outbreak. Historically college dormitories have been susceptible to severe outbreaks.",
            "vInfo": "The MenACWY vaccine protects against 4 strains of meningitis bacteria. It is a conjugate vaccine that is administered during adolescence.",
            "Dates": dateString,
            "Cite": ["https://www.mayoclinic.org/drugs-supplements/meningococcal-vaccine-intramuscular-route-subcutaneous-route/description/drg-20064657","https://vk.ovg.ox.ac.uk/vk/menacwy-vaccine"]
        }

        return dict

    def MenB(self):
        pass

    def PPSV(self):
        pass

    def Dengue(self):
        pass


"""
Hepatitis B (3)
RV (2 or 3 depending on vaccine administered)
DTaP (4)
HiB (depends on vaccine brand)
PCV (4)
IPV (3)
Influenza (yearly)
MMR
Varicella
Hepatitis A
TDaP
HPV
Meningococcal ACYW
Meningococcal B
PPSV
Dengue
"""