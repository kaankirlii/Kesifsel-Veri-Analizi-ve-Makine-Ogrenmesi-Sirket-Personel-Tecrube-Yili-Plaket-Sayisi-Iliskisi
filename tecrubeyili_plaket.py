# -*- coding: utf-8 -*-
"""

**Proje Konusu: Şirket Personel No-Yıl Sayısı-Plaket Türü-Plaket Sayısı**

Plaket Türü: 0-4 Yıl (YOK), 5-9 Yıl (BRONZ), 10-19 Yıl (GUMUS), 20+ Yıl (ALTIN) 

Plaket sayısı: 0 (YOK), 1 (BRONZ), 2 (GUMUS + BRONZ), 3 (ALTIN + GUMUS +BRONZ)

**Keşifsel Veri Analizi Konuları**
"""

#1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2
sirketdata = pd.read_csv("/content/sample_data/sirket_verisi.txt")
sirketdata

#3
#Personel yıl ortalaması
print("Yıl Ortalaması: ",sirketdata["YIL"].mean())
#ortadaki deger (sıralı hesap)
print("Medyan: ",sirketdata["YIL"].median())
#En sık görünen yıl
print("Mod: ",int(sirketdata["YIL"].mode()))

#4
#Personel- Yıl sayısı grafiği
plt.figure(figsize=(15,7))
plt.title("PERSONEL-YIL SAYISI GRAFİĞİ",size=20,color="brown")
plt.xlabel("PERSONEL_NO",size=18,color="red")
plt.ylabel("YIL",size=18,color="blue")
plt.plot(sirketdata.PERSONEL_NO,sirketdata.YIL,"o",color="green")

#5 #Yıl Sıklık Grafiği
plt.figure(figsize=(18,6))
sns.countplot(sirketdata.YIL)
plt.title("YIL-SIKLIK GRAFİĞİ",size=20,color="darkgreen")
plt.xlabel("YIL",size=16,color="blue")
plt.ylabel("SIKLIK",size=16,color="darkblue")
plt.show()

#6 #piechart #Yıl yüzdelik dilimi
plt.figure(figsize=(13,13))
plt.title("YIL SAYISI YÜZDELİK DİLİMİ",size=18)
sirketdata['YIL'].value_counts().plot(kind="pie", autopct="%.2f%%")
plt.show()

#7 #Plaket Sayısı-Sıklık grafiği 
plt.figure(figsize=(18,6))
sns.countplot(sirketdata.PLAKET_SAYISI)
plt.title("PLAKET SAYISI-SIKLIK GRAFİĞİ",size=20,color="darkgreen")
plt.xlabel("PLAKET SAYISI",size=17,color="blue")
plt.ylabel("SIKLIK",size=17,color="darkblue")
plt.show()

#8 #Plaket Sayısı-Yüzdelik dilimi
plt.figure(figsize=(12,12))
plt.title("PLAKET SAYISI YÜZDELİK DİLİMİ",size=18)
sirketdata['PLAKET_SAYISI'].value_counts().plot(kind="pie", autopct="%.2f%%")
plt.show()

#9 #Personel No-Yıl-Plaket Sayısı Grafiği
#MOR->YOK,LACİVERT-> 1 PLAKET,YEŞİL-> 2 PLAKET, SARI -> 3 PLAKET
plt.figure(figsize=(16,7))
plt.title("PERSONEL NO-YIL-PLAKET SAYISI GRAFİĞİ",size=18,color="brown")
plt.xlabel("PERSONEL_NO",size=18,color="green")
plt.ylabel("YIL",size=18,color="blue")
scatter=plt.scatter(sirketdata["PERSONEL_NO"],sirketdata["YIL"],s=100,c=sirketdata["PLAKET_SAYISI"])

"""---------------------------------------------

**Makine Öğrenmesi Konuları :**
"""

#10
import numpy as np2
import matplotlib.pyplot as plt2
import pandas as pd2

#11
sirketdata2 = pd2.read_csv("/content/sample_data/sirket_verisi.txt")
sirketdata2

#12
plt2.figure(figsize=(12,6))
plt2.plot(sirketdata2.PERSONEL_NO,sirketdata2["YIL"],"o")

pip install category_encoders

#14 #Plaket türü verilerini dönüştürüp kategorilendirir 
import category_encoders as ce
encoder = ce.OneHotEncoder(use_cat_names=True) 
sirketdata_ml = encoder.fit_transform(sirketdata2)
sirketdata_ml.head()

#15
personel_bilgisi=sirketdata_ml[["PERSONEL_NO","YIL","PLAKET_TURU_YOK","PLAKET_TURU_BRONZ","PLAKET_TURU_GUMUS","PLAKET_TURU_ALTIN"]]
plaket=sirketdata_ml[["PLAKET_SAYISI"]]
personel_bilgisi

#16
plaket

#17 #sklearn-> Algoritma ve ML ile ilgili işleri kolayca yapar
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(personel_bilgisi,plaket,test_size=0.25)

#18
X_train

#19
X_test

#20
y_train

#21
y_test

#22 #KNN (bir veriye en yakın n tane veriden sınıflandırma seçimi yapılır)
from sklearn.neighbors import KNeighborsClassifier
KnModel=KNeighborsClassifier(n_neighbors=3)
KnModel.fit(X_train,y_train)

#23 #tahminleri yazar
y_pred=KnModel.predict(X_test)
y_pred

#24 #gercek degerleri yazar
y_test.values

#25 sklearn metrik 
from sklearn import metrics

#26 #doğruluk oranı #gerçek değer, tahminler
metrics.accuracy_score(y_test,y_pred)

#27 matris gösterimi
metrics.confusion_matrix(y_test,y_pred)

#28 #sınıflandırma raporu
print(metrics.classification_report(y_test,y_pred))
