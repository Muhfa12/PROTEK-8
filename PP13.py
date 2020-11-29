# 13
nilaiMhs = [{"nim" : "A01", "nama" : "Amir", "mid" : 50, "uas" : 80},
                {"nim" : "A02", "nama" : "Budi", "mid" : 40, "uas" : 90},
                {"nim" : "A03", "nama" : "Cici", "mid" : 50, "uas" : 50},
                {"nim" : "A04", "nama" : "Dedi", "mid" : 20, "uas" : 30},
                {"nim" : "A05", "nama" : "Fifi", "mid" : 70, "uas" : 40}]
def nilaiAkhirTertinggi(nilaiList):
    mid = []
    uas = []
    nilaiAkhir = []
    tertinggi = {}
    for x in nilaiList:
        k = (x["mid"] + (2 * x["uas"])) / 3
        nilaiAkhir.append(k)
    tertinggi = nilaiAkhir.index(max(nilaiAkhir))
    result = {"nim" : nilaiList[tertinggi]["nim"],
                "nama" : nilaiList[tertinggi]["nama"]}    
    return result
a = nilaiAkhirTertinggi(nilaiMhs)
print("Mahasiswa dengan nilai tertinggi yaitu", a["nama"], "dengan NIM", a["nim"])
