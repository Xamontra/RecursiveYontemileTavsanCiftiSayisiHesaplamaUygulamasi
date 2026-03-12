"""Olay şu başlangıçta 1 tavşan çifti var bu tavşanlar 1 ayda büyüyorlar 1ayda doğuruyorlar
bu şekilde çoğalıyorlar.İstenen aydaki tavşna çifti sayısını bulan program yazınız."""

def tavsanhesapla(n):
    if n==1 or n==2:
        return 1
    else:
        return tavsanhesapla(n-1)+tavsanhesapla(n-2)




ay=int(input("Hangi Aydaki tavşan çifti sayısını istiyorsunuz? :"))
print("Tavşan Çifti Sayısı:",tavsanhesapla(ay))
