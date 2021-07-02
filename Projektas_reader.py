class Reader():
    def __init__(self, fname, fname2):
        self.fname = fname
        self.fname2 = fname2
        self.auks_is_zmones_kaime = 0
        self.auks_is_zmones_mieste = 0
        self.apskrities_kodai = []
        self.alytaus_g = 0
        self.kauno_g = 0 
        self.klaipedos_g = 0
        self.marijampoles_g = 0
        self.panevezio_g = 0
        self.siauliu_g = 0
        self.taurages_g = 0
        self.telsiu_g = 0
        self.utenos_g = 0
        self.vilniaus_g = 0
        self.algos_alytus = []
        self.algos_kaunas = []
        self.algos_klaipeda = []
        self.algos_marijampole = []
        self.algos_panevezys = []
        self.algos_siauliai = []
        self.algos_taurage = []
        self.algos_telsiai = []
        self.algos_utena = []
        self.algos_vilnius = []
        self.zmones_a_k = []
        self.zmones_a_m = []
        self.zmones_nu = []
        self.nu_su_kanalizacija = []
        self.nu_su_lauko_tualetu = []
        self.nu_su_kompiuteriu = []       
        self.zmoniu_kiekis_su_kanalizacija = 0
        self.zmoniu_kiekis_su_lauko_tualetu = 0
        self.zmoniu_kiekis_su_kompiuteriu = 0
        self.read()
        self.gyv_prisk_apskr()
        self.algu_sk()
        self.namu_ukiu_skaiciavimas()
             

    def read(self):
        with open(self.fname, "r", encoding="utf-8") as t, open(self.fname2, "r", encoding="utf-8") as t2:
            lines = t.readlines()
            antraste = lines[0].split(",")
            as_id = antraste.index("PB030")
            nu_id = antraste.index("HB030")
            issil = antraste.index("PE040")
            alga = antraste.index("PY010G")
            m_k = antraste.index("M_K\n")
            apskr = antraste.index("AP")
            for line in lines[1:]:
                line_text = line.split(",")
                if line_text[issil] != "":
                    x = float(line_text[issil])
                    y = float(line_text[m_k])
                    lst = []
                    lst2 = []
                    if (x > 4 and x < 100 and y == 1) or (x > 400 and y == 1):
                        lst.append(line_text[as_id])
                        lst.append(line_text[nu_id])
                        lst.append(y)
                        lst.append(line_text[apskr])
                        lst.append(line_text[alga])
                        self.zmones_a_m.append(lst)
                        self.apskrities_kodai.append(line_text[apskr])
                        self.auks_is_zmones_mieste +=1
                        self.zmones_nu.append(line_text[nu_id])
                    elif (x > 4 and x < 100 and y == 2) or (x > 400 and y == 2):
                        lst2.append(line_text[as_id])
                        lst2.append(line_text[nu_id])
                        lst2.append(y)
                        lst2.append(line_text[apskr])
                        lst2.append(line_text[alga])
                        self.zmones_a_k.append(lst2)
                        self.apskrities_kodai.append(line_text[apskr])
                        self.auks_is_zmones_kaime += 1
                        self.zmones_nu.append(line_text[nu_id])        
            lines2 = t2.readlines()
            antraste2 = lines2[0].split(",")
            nu_id2 = antraste2.index("HB030")
            kanal = antraste2.index("HH081")
            tual = antraste2.index("HH091")
            kompiuteris = antraste2.index("HS090")
            for line in lines2[1:]:
                line_text = line.split(",")
                if line_text[kanal] == "1" or line_text[kanal] == "2":
                    self.nu_su_kanalizacija.append(line_text[nu_id2])
                if line_text[tual] == "3":
                    self.nu_su_lauko_tualetu.append(line_text[nu_id2])
                if line_text[kompiuteris] == "1" or line_text[kompiuteris] == "1.0":
                    self.nu_su_kompiuteriu.append(line_text[nu_id2])

       
    def gyv_prisk_apskr(self):
        for sk in self.apskrities_kodai:
            if sk == "1":
                self.alytaus_g += 1
            elif sk == "2":
                self.kauno_g += 1
            elif sk == "3":
                self.klaipedos_g += 1
            elif sk == "4":
                self.marijampoles_g += 1
            elif sk == "5":
                self.panevezio_g += 1
            elif sk == "6":
                self.siauliu_g += 1
            elif sk == "7":
                self.taurages_g += 1
            elif sk == "8":
                self.telsiu_g += 1
            elif sk == "9":
                self.utenos_g += 1
            elif sk == "10":
                self.vilniaus_g += 1


    def algu_sk(self):
        for elem in self.zmones_a_k:
            if float(elem[-1]) > 0 and elem[3] == "1":              
                self.algos_alytus.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "2":
                self.algos_kaunas.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "3":
                self.algos_klaipeda.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "4":
                self.algos_marijampole.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "5":
                self.algos_panevezys.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "6":
                self.algos_siauliai.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "7":
                self.algos_taurage.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "8":
                self.algos_telsiai.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "9":
                self.algos_utena.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "10":
                self.algos_vilnius.append(elem[-1])
        for elem in self.zmones_a_m:
            if float(elem[-1]) > 0 and elem[3] == "1":              
                self.algos_alytus.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "2":
                self.algos_kaunas.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "3":
                self.algos_klaipeda.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "4":
                self.algos_marijampole.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "5":
                self.algos_panevezys.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "6":
                self.algos_siauliai.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "7":
                self.algos_taurage.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "8":
                self.algos_telsiai.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "9":
                self.algos_utena.append(elem[-1])
            elif float(elem[-1]) > 0 and elem[3] == "10":
                self.algos_vilnius.append(elem[-1])

        
    def namu_ukiu_skaiciavimas(self):
        for i in self.zmones_nu:
            if i in self.nu_su_kanalizacija:
                self.zmoniu_kiekis_su_kanalizacija +=1
        for i in self.zmones_nu:
            if i in self.nu_su_lauko_tualetu:
                self.zmoniu_kiekis_su_lauko_tualetu +=1
        for i in self.zmones_nu:
            if i in self.nu_su_kompiuteriu:
                self.zmoniu_kiekis_su_kompiuteriu +=1

        
