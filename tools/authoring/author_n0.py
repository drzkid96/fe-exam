"""Base questions for problem types the recorded review sessions cover and the bank lacked. Run after author_d2.py and
before the version scripts; author_v6.py then turns each into a four-version family."""
from author_dsl import *
N('fluids-d', "A 50 mm diameter water jet moving at 20 m/s is turned through 60° by a fixed, smooth vane without changing speed. What is the horizontal force the jet exerts on the vane?", 393, 'N',
  "The momentum equation gives the force as mass flow rate times the change in velocity.", "F = (density) Q V (1 - cos 60°) = 393 N.", "1000*pi*0.05**2/4*20**2*(1-cos(rad(60)))")
N('surveying-b', "Offsets from a straight baseline to a curved boundary, measured every 10 m, are 3.2, 4.5, 5.1, 4.0 and 2.6 m. Using the trapezoidal rule, what is the area between the baseline and the boundary?", 165, 'm^{2}',
  "The trapezoidal rule treats each strip as a trapezoid.", "A = 10((3.2 + 2.6)/2 + 4.5 + 5.1 + 4.0) = 165 m^{2}.", "10*((3.2+2.6)/2+4.5+5.1+4.0)")
N('surveying-d', "Point A has coordinates N 1,000.00, E 2,000.00 and point B has coordinates N 1,400.00, E 2,300.00, in metres. What is the azimuth of the line from A to B?", 36.87, '°',
  "The direction between two points comes from the differences in easting and northing.", "Azimuth = arctan(300 / 400) = 36.87°.", "atan((2300-2000)/(1400-1000))*180/pi", tol=0.005)
N('water-i', "A wastewater has a 5-day BOD of 180 mg/L and a BOD rate constant of 0.23 per day (base e). What is its ultimate BOD?", 263, 'mg/L',
  "BOD is exerted as a first-order reaction.", "L_{0} = 180 / (1 - e^{-0.23(5)}) = 263 mg/L.", "180/(1-exp(-0.23*5))")
N('water-b', "Water flows at 2.5 m/s and 0.80 m deep in a wide rectangular channel. What is the Froude number? Use g = 9.81 m/s^{2}.", 0.89, '',
  "The Froude number compares flow velocity with the speed of a small surface wave.", "Fr = 2.5 / sqrt(9.81 × 0.80) = 0.89.", "2.5/sqrt(g*0.80)")
N('geotech-b', "A soil sample has a mass of 245.0 g when moist and 210.0 g after oven drying. What is its water content?", 16.67, '%',
  "Water content is the mass of water divided by the mass of dry solids.", "w = (245 - 210) / 210 × 100 = 16.67%.", "(245-210)/210*100")
N('structural-e', "A beam fixed at both ends spans 6 m and carries a 60 kN point load 2 m from the left support. What is the fixed-end moment at the left support?", 53.33, 'kN·m',
  "Fixed-end moments are the support moments of a beam held against rotation at both ends.", "M = P a b^{2} / L^{2} = 60(2)(4)^{2} / 6^{2} = 53.33 kN·m.", "60*2*4**2/6**2")
N('dynamics-b', "A slender rod of mass 6 kg and length 2 m is pivoted at one end. A small 4 kg mass is fixed to its free end. What is the mass moment of inertia of the assembly about the pivot?", 24, 'kg·m^{2}',
  "Moments of inertia about the same axis add.", "I = 6(2)^{2}/3 + 4(2)^{2} = 24 kg·m^{2}.", "6*2**2/3+4*2**2")
N('mechmat-c', "A solid steel shaft 50 mm in diameter and 2 m long carries a torque of 1.5 kN·m. The shear modulus is 80 GPa. What is the angle of twist, in degrees?", 3.50, '°',
  "A shaft in torsion twists by T L / (G J).", "Angle = T L / (G J) = 0.0611 rad = 3.50°.", "1.5e6*2000/(80000*pi*50**4/32)*180/pi")
save('n0')
