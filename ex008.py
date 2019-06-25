medida = float(input("Uma distância em metros: "))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print("A medida de {} metros corresponde a \n{} kilômetros \n{} hectômetros \n{} decâmetro \n{:.0f} decímetro \n{:.0f} centímetro \n{:.0f} milímitros".format(medida, km, hm,dam, dm, cm, mm))