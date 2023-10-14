#operacii s data_types / chislovimi_znachenijami
answ = (3 * 2) + (2 / 2) - 3
print("(3 * 2) + (2 / 2) - 3 =",int(answ))

answ1 = 3**2
print("3^2 =",answ1,type(answ1))

#vehestvennie chisla / chisla s plavajushei tochkoj
answ2 = 1.3 + 0.2
print(answ2)

answ2_1 = 0.2 + 0.1
print(answ2_1)

#simvoli podcherkivanija v chislah
#|Python 3.6| & >
print(14_000_000,"=",14000000)
print(10_00)
print(10_0)
print(1.0_05)


#mnozestvennoe prisvoenie
x,y,z = 0,"one",2
print(x,z,y)


#konstanti
STATIC_VALUE = 10
STATIC_VALUE = 1 #mozem izmenjat, no schitaetsa esli imja peremennoj zaglavnimi to eto konstanta - ne izmenjaemoe znachenie(v python izmenjaetsa)
print(STATIC_VALUE)
import constant #posle sozdanija class "constant" i zapuska programmi sozdalas papka _pycache_ (uskaraet rabotu s modulami i importiravanem bibleotek) 
print(constant.PI)