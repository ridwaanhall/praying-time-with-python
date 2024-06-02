import math

def Waktu(Number):
    D = int(abs(Number))
    M = int((abs(Number) - D) * 60)
    S = (abs(Number) - D - M / 60) * 3600
    if S == 60:
        S = 0
        M = M + 1
    if M == 60:
        M = 0
        D = D + 1
    if format(S, '1f') == '60':
        S = 0
        M = M + 1
    if format(M, '.1f') == '60':
        M = 0
        D = D + 1
    Data = str(D).zfill(2) + ':' + str(M).zfill(2) + ':' + str(format(S, '.0f')).zfill(2)
    return Data

print("Konversi Hari Julian")
tgl = float(input("Tanggal Masehi = "))
bulan = float(input("Bulan Masehi = "))
tahun = float(input("Tahun Masehi = "))
lintang = float(input("Lintang Tempat = "))
bujur = float(input("Bujur Tempat = "))
tz = float(input("Zona Waktu = "))

a = 3
b = bulan
# Mulai perhitungan cak Thomas Zuhur
N = ((275 * bulan) / 9) - ((bulan + 9) / 12) * (1 + (tahun / 4) - (3 * ((tahun / 100) + 1) / 4)) + tgl - 30
Nn = round(N, 0)
Lamb = bujur / 360 * 24
rad = 0.017453293
Tt = Nn + (12 - Lamb) / 24
M = (0.9856 * Tt - 3.289) * rad

L = M + 1.916 * rad * math.sin(M) + 0.02 * rad * math.sin(2 * M) + 282.634 * rad
Lh = L / 3.14159 * 12
Qi = int(Lh / 6) + 1

if int(Qi / 2) * 2 == Qi:
    Qqq = int(Qi / 2) * 2 - Qi
else:
    Qqq = Qi - 1

Ra = math.atan(0.91746 * math.tan(L)) / 3.14159 * 12
Ra1 = Ra + Qqq * 6
Tloc = (Ra1 - 0.06571 * Tt - 6.622) + 24
Tloc1 = Tloc - int(Tloc / 24) * 24
Cek = (Tloc1 + 2 / 60) - Lamb + tz
if Cek < 0:
    Zhr = Cek + 12
else:
    Zhr = Cek

# Awal Subuh
Tsbh = Nn + (6 - Lamb) / 24
Msbh = (0.9856 * Tsbh - 3.289) * rad
Lsbh = Msbh + 1.916 * rad * math.sin(Msbh) + 0.02 * rad * math.sin(2 * Msbh) + 282.634 * rad
Lhsbh = Lsbh / 3.14159 * 12
Qisbh = int(Lhsbh / 6) + 1

if int(Qisbh / 2) * 2 == Qisbh:
    Qqqsbh = int(Qisbh / 2) * 2 - Qisbh
else:
    Qqqsbh = Qisbh - 1

Rasbh = math.atan(0.91746 * math.tan(Lsbh)) / 3.14159 * 12
Ra1sbh = Rasbh + Qqqsbh * 6
SinDesbh = 0.39782 * math.sin(Lsbh)
CosDesbh = math.sqrt(abs(1 - SinDesbh * SinDesbh))
Ysbh = (math.cos(110.018 * rad) - SinDesbh * math.sin(lintang * rad)) / (CosDesbh * math.cos(lintang * rad))
Y1sbh = math.atan(math.sqrt(1 - Ysbh * Ysbh) / Ysbh) / rad
if Y1sbh < 0:
    ATNXsbh = Y1sbh + 180
else:
    ATNXsbh = Y1sbh
Hsbh = (360 - ATNXsbh) * 24 / 360
Tlocsbh = Hsbh + Ra1sbh - 0.06571 * Tsbh - 6.622 + 24
Tloc1sbh = Tlocsbh - int(Tlocsbh / 24) * 24
Ceksbh = (Tloc1sbh + 2 / 60) - Lamb + tz
if Ceksbh > 12:
    Sbh = Ceksbh - 12
else:
    Sbh = Ceksbh

# Awal Waktu Terbit
Ttrbt = Nn + (6 - Lamb) / 24
Mtrbt = (0.9856 * Ttrbt - 3.289) * rad
Ltrbt = Mtrbt + 1.916 * rad * math.sin(Mtrbt) + 0.02 * rad * math.sin(2 * Mtrbt) + 282.634 * rad
Lhtrbt = Ltrbt / 3.14159 * 12
Qitrbt = int(Lhtrbt / 6) + 1

if int(Qitrbt / 2) * 2 == Qitrbt:
    Qqqtrbt = int(Qitrbt / 2) * 2 - Qitrbt
else:
    Qqqtrbt = Qitrbt - 1

Ratrbt = math.atan(0.91746 * math.tan(Ltrbt)) / 3.14159 * 12
Ra1trbt = Ratrbt + Qqqtrbt * 6
SinDetrbt = 0.39782 * math.sin(Ltrbt)
CosDetrbt = math.sqrt(abs(1 - SinDetrbt * SinDetrbt))
Ytrbt = (math.cos(90.83333333 * rad) - SinDetrbt * math.sin(lintang * rad)) / (CosDetrbt * math.cos(lintang * rad))
Y1trbt = math.atan(math.sqrt(1 - Ytrbt * Ytrbt) / Ytrbt) / rad
if Y1trbt < 0:
    ATNXtrbt = Y1trbt + 180
else:
    ATNXtrbt = Y1trbt
Htrbt = (360 - ATNXtrbt) * 24 / 360
Tloctrbt = Htrbt + Ra1trbt - 0.06571 * Ttrbt - 6.622 + 24
Tloc1trbt = Tloctrbt - int(Tloctrbt / 24) * 24
CekTrbt = (Tloc1trbt - 2 / 60) - Lamb + tz
if CekTrbt > 12:
    Trbt = CekTrbt - 12
else:
    Trbt = CekTrbt

# Awal Waktu Ashar
Tasr = Nn + (15 - Lamb) / 24
Masr = (0.9856 * Tasr - 3.289) * rad
Ltasr = Masr + 1.916 * rad * math.sin(Masr) + 0.02 * rad * math.sin(2 * Masr) + 282.634 * rad
Lhasr = Ltasr / 3.14159 * 12
Qiasr = int(Lhasr / 6) + 1

if int(Qiasr / 2) * 2 == Qiasr:
    Qqqasr = int(Qiasr / 2) * 2 - Qiasr
else:
    Qqqasr = Qiasr - 1

Raasr = math.atan(0.91746 * math.tan(Ltasr)) / 3.14159 * 12
Ra1asr = Raasr + Qqqasr * 6
SinDeasr = 0.39782 * math.sin(Ltasr)
CosDeasr = math.sqrt(abs(1 - SinDeasr * SinDeasr))
Dek = math.atan(SinDeasr / CosDeasr)
Zd = abs(Dek - (lintang * rad))
Za = math.atan(math.tan(Zd) + 1)
Yasr = (math.cos(Za) - SinDeasr * math.sin(lintang * rad)) / (CosDeasr * math.cos(lintang * rad))
Y1asr = math.atan(math.sqrt(1 - Yasr * Yasr) / Yasr) / rad
if Y1asr < 0:
    ATNXasr = Y1asr + 180
else:
    ATNXasr = Y1asr
Hasr = (360 - ATNXasr) * 24 / 360
Tlocasr = Hasr + Ra1asr - 0.06571 * Tasr - 6.622 + 24
Tloc1asr = Tlocasr - int(Tlocasr / 24) * 24
Cekasr = (Tloc1asr + 2 / 60) - Lamb + tz
if Cekasr > 12:
    Asr = Cekasr - 12
else:
    Asr = Cekasr

# Awal Waktu Maghrib
Tmgh = Nn + (18 - Lamb) / 24
Mmgh = (0.9856 * Tmgh - 3.289) * rad
Ltmgh = Mmgh + 1.916 * rad * math.sin(Mmgh) + 0.02 * rad * math.sin(2 * Mmgh) + 282.634 * rad
Lhmgh = Ltmgh / 3.14159 * 12
Qimgh = int(Lhmgh / 6) + 1

if int(Qimgh / 2) * 2 == Qimgh:
    Qqqmgh = int(Qimgh / 2) * 2 - Qimgh
else:
    Qqqmgh = Qimgh - 1

Ramgh = math.atan(0.91746 * math.tan(Ltmgh)) / 3.14159 * 12
Ra1mgh = Ramgh + Qqqmgh * 6
SinDemgh = 0.39782 * math.sin(Ltmgh)
CosDemgh = math.sqrt(abs(1 - SinDemgh * SinDemgh))
Ymgh = (math.cos(90.83333333 * rad) - SinDemgh * math.sin(lintang * rad)) / (CosDemgh * math.cos(lintang * rad))
Y1mgh = math.atan(math.sqrt(1 - Ymgh * Ymgh) / Ymgh) / rad
if Y1mgh < 0:
    ATNXmgh = Y1mgh + 180
else:
    ATNXmgh = Y1mgh
Hmgh = (360 - ATNXmgh) * 24 / 360
Tlocmgh = Hmgh + Ra1mgh - 0.06571 * Tmgh - 6.622 + 24
Tloc1mgh = Tlocmgh - int(Tlocmgh / 24) * 24
Cekmgh = (Tloc1mgh + 2 / 60) - Lamb + tz
if Cekmgh > 12:
    Mgh = Cekmgh - 12
else:
    Mgh = Cekmgh

# Awal Waktu Isya
Tisy = Nn + (18 - Lamb) / 24
Misy = (0.9856 * Tisy - 3.289) * rad
Lisy = Misy + 1.916 * rad * math.sin(Misy) + 0.02 * rad * math.sin(2 * Misy) + 282.634 * rad
Lhisy = Lisy / 3.14159 * 12
Qiisy = int(Lhisy / 6) + 1

if int(Qiisy / 2) * 2 == Qiisy:
    Qqqisy = int(Qiisy / 2) * 2 - Qiisy
else:
    Qqqisy = Qiisy - 1

Raisy = math.atan(0.91746 * math.tan(Lisy)) / 3.14159 * 12
Ra1isy = Raisy + Qqqisy * 6
SinDeisy = 0.39782 * math.sin(Lisy)
CosDeisy = math.sqrt(abs(1 - SinDeisy * SinDeisy))
Yisy = (math.cos(108 * rad) - SinDeisy * math.sin(lintang * rad)) / (CosDeisy * math.cos(lintang * rad))
Y1isy = math.atan(math.sqrt(1 - Yisy * Yisy) / Yisy) / rad
if Y1isy < 0:
    ATNXisy = Y1isy + 180
else:
    ATNXisy = Y1isy
Hisy = (360 - ATNXisy) * 24 / 360
Tlocisy = Hisy + Ra1isy - 0.06571 * Tisy - 6.622 + 24
Tloc1isy = Tlocisy - int(Tlocisy / 24) * 24
Cekisy = (Tloc1isy + 2 / 60) - Lamb + tz
if Cekisy > 12:
    Isy = Cekisy - 12
else:
    Isy = Cekisy

# Menampilkan Hasil
print(f"Tanggal, bulan dan tahun = {tgl}/{bulan}/{tahun}")
print(f"Lintang dan bujur tempat = {lintang}, {bujur}")
print(f"Zona waktu = {tz}")
print(f"Waktu Dzuhur = {Waktu(Zhr)}")
print(f"Waktu Shubuh = {Waktu(Sbh)}")
print(f"Waktu Terbit = {Waktu(Trbt)}")
print(f"Waktu Ashar = {Waktu(Asr)}")
print(f"Waktu Maghrib = {Waktu(Mgh)}")
print(f"Waktu Isya = {Waktu(Isy)}")
