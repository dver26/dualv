from dualv import Dual
import dualv as dv
import numpy as np

print(f"TEST DE LLIBRERÍA DUALV\n\n")

# Inicialització

dual1 = Dual(2, 20)
if(dual1.real == 2 and dual1.dual == 20):
    print("Inicilaització OK")
else:
    print("Inicialització Malament")

# Inicialització automàtica

dual2 = Dual.diff_dual(2)
if(dual2.real == 2 and dual2.dual == 1):
    print("Inicialització automàtica OK")
else:
    print("Inicialització automàtica Malament")

# Suma / Resta

dual1 = Dual(3, 4)
dual2 = Dual(4, 3)

dual_suma = dual1 + dual2
dual_suma_escalar = 1 + dual1
dual_suma_escalar2 = dual1 + 1

if(dual_suma.real == 7 and dual_suma.dual == 7 and
    dual_suma_escalar.real == 4 and dual_suma_escalar.dual == 4 and
       dual_suma_escalar2.real == 4 and dual_suma_escalar2.dual ==4 ):
    print("Suma OK")
else:
    print("Suma Malament")

dual_resta = dual1 - dual2
dual_resta_escalar = dual1 - 1
dual_resta_escalar2 = 1 - dual1

if(dual_resta.real == -1 and dual_resta.dual == 1 and
    dual_resta_escalar.real == 2 and dual_resta_escalar.dual == 4 and
       dual_resta_escalar2.real == -2 and dual_resta_escalar2.dual == -4 ):
    print("Resta OK")
else:
    print("Resta Malament")

# Multiplicació

dual1 = Dual(1, 2)
dual2 = Dual(2, 3)

dual_mult = dual1 * dual2
dual_mult_esc = 2*dual1
dual_mult_esc2 = dual1*2

if(dual_mult.real == 2 and dual_mult.dual == 7 and
   dual_mult_esc.real == 2 and dual_mult_esc.dual == 4 and
       dual_mult_esc2.real == 2 and dual_mult_esc2.dual == 4):
    print("Multiplicació OK")
else:
    print("Multiplicació Malament")


dual1 = Dual(3, 2)
dual2 = Dual(2, 1)

dual_div = dual1 / dual2
dual_div_esc = dual1 / 2
dual_div_esc2 = 2 / dual1

if (dual_div.real == 3/2 and dual_div.dual == 1/4 and
   dual_div_esc.real == 3/2 and dual_div_esc.dual == 1 and
       dual_div_esc2.real == 2/3 and dual_div_esc2.dual == -4/9) :
    print("Divisió OK")
else:
    print("Divisió Malament")

# Potència

dual1 = Dual(1, 2)
dual_pow_1 = dv.pot(3, dual1)
dual_pow_2 = dv.pot(6, dual1)
x = 5
x_pow = dv.pot(3, x)

if(dual_pow_1 == Dual(1, 6) and dual_pow_2 == Dual(1, 12) and x_pow == 125):
    print("Potència OK")
else:
    print("Potència Malament")

# Trigonomètriques

sin_pi = dv.sin(np.pi)
sin_dual_pi = dv.sin(Dual(np.pi, 1))

cos_pi = dv.cos(np.pi)
cos_dual_pi = dv.cos(Dual(np.pi, 1))

tan_pi = dv.tan(np.pi)
tan_dual_pi = dv.tan(Dual(np.pi, 1))

if (np.isclose(sin_pi, 0) and 
    np.isclose(sin_dual_pi.real, 0) and np.isclose(sin_dual_pi.dual, -1)):
    print("Sinus OK")
else:
    print("Sinus Malament")

if (np.isclose(cos_pi, -1) and
    np.isclose(cos_dual_pi.real, -1) and np.isclose(cos_dual_pi.dual, 0)):
    print("Cosinus OK")

else:
    print("Cosinus Malament")

if (np.isclose(tan_pi, 0) and 
        np.isclose(tan_dual_pi.real, 0) and np.isclose(tan_dual_pi.dual, 1)):
    print("Tangent OK")
else:
    print("Tangent Malament")
