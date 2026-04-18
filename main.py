def hisobla(investitsiya, foiz):
    majburiy_qiymat = investitsiya * (1 + foiz / 100) ** 10
    return majburiy_qiymat

investitsiya_summasi = [1000, 2000, 3000, 4000, 5000]
yillik_daromad_foizi = [5, 7, 10, 12, 15]

for i in range(len(investitsiya_summasi)):
    print(f"Investitsiya: {investitsiya_summasi[i]}, Foiz: {yillik_daromad_foizi[i]}, Majburiy qiymat: {hisobla(investitsiya_summasi[i], yillik_daromad_foizi[i])}")
