# Algorithmic Logical Cafelator (ALC) v1.0

Manhattan Cafe temalı, geceleri arkada müzik çalarken çay yudumlanarak geliştirilmiş **8-Bitlik bir Arithmetic Logic Unit Emülatörü** ve onun üzerine inşa edilmiş bir hesap makinesi. 

## Özellikler ve Menü (Reçeteler)

Sıradan ALU'ları unutun. Burada bitler kahve çekirdekleri gibi harmanlanır:

• 0 = ADD (Kahve Ekleme): İki farklı dozu birbirine karıştırır [Toplama İşlemi].
• 1 = SUB (Kahve Eksiltme): Bardaktan büyük bir yudum alır [Çıkarma İşlemi].
• 2 = AND (Aroma Kesişimi): Sadece ortak tat notalarını filtreler [Bitwise AND / VE İşlemi].
• 3 = OR (Harmanlama): Tüm aromaları tek bir bardakta birleştirir [Bitwise OR / VEYA İşlemi].
• 4 = XOR (Özel Harman): Birbirine zıt, eşsiz aromaları seçer [Bitwise XOR / Özel VEYA İşlemi].
• 5 = NOT (Ters Demleme): Kahveyi tersine çevirir ve kafeinsizleştirir [Bitwise NOT / Tersini Alma İşlemi].
• 6 = SHL (Sola Süzme): Şurubu ve yoğunluğu iki katına çıkarır [Bitwise Sola Kaydırma / Sola Bit Shift].
• 7 = SHR (Sağa Süzme): Yoğunluğu yarıya indirir, dışarı sızan damlaları sayar [Bitwise Sağa Kaydırma / Sağa Bit Shift].

## Barista Sensörleri (Durum Bayrakları)

ALC v1.0, işlemlerin durumunu takip etmek için 4 özel donanım sensörüne sahiptir:

| Sensör | Orijinal Flag | Anlamı | Tetiklenme Şartı |
| :--- | :--- | :--- | :--- |
| **E** | Zero (Z) | **Empty** | Bardak tamamen boşaldığında (Sonuç = 0) tetiklenir. |
| **S** | Carry (C) | **Spill** | Kahve bardaktan taştığında (8-bit sınırını aşınca: >255 veya <0) tetiklenir. |
| **D** | Negative (N) | **Debt** | Hesap eksiye düştüğünde (İşaret biti / MSB = 1) tetiklenir. |
| **O** | Overflow (V) | **Overbrew** | Kahve aşırı demlenip asitliği bozulduğunda (Donanım seviyesi taşma) tetiklenir. |

## Not:`Overbrew (O)` bayrağı, iki pozitif veya iki negatif kahve dozunun toplanıp işaret değiştirmesini `((a ^ res) & (b ^ res) & 0x80)` formülüyle donanımsal olarak yakalar. 

## Nasıl Çalıştırılır?

Doğrudan terminale python3 yazıp dosyayı terminal'inize sürekleyin ve enter tuşuna basın.
## 📜 Lisans ve Teşekkür
Bu yazılım, *Manhattan Cafe* kuralları ve *Filipinler Esintisi* altında tamamen eğlence ve kafa dağıtma amacıyla geliştirilmiştir. 7 yazılım kitabının bilgisi ve bitmeyen çay bardaklarının gücü adına! 🫖✨
