from math import pow, sqrt
def adc(Vt, alt):
    rho0    = 2.377e-3               # slugs/ft3, seal-level density
    TFAC    = 1.0 - 0.703e-5*alt
    T       = 519.0*TFAC
    if(alt > 35000.0):
        T = 390.0
    rho     = rho0 * (pow(TFAC, 4.14))  # density
    Mach    = Vt/sqrt(  1.4*1716.3*T )
    qbar    = 0.5*rho*Vt*Vt
    return (Mach,qbar)

def transp(t,x,u):
    S      = 2170.0   # wing area, ft2
    cbar   =   17.5   # ft
    mass   =    5.0e3 # slugs
    Iyy    =    4.1e6 # slug-ft2
    Tstat  =    6.0e4
    dTdV   =  -38.0
    ZE     =    2.0     # ft, distance from Thrust to cgt
    cdcls  =    0.042
    CLA    =    0.085   # per degree, stability-axis aero derivative
    CMA    =   -0.022   # per degree, stability-axis aero derivative
    CMDE   =   -0.016   # per degree, stability-axis aero derivative
    CMQ    =  -16.0     # per radian, pitch damping coeff.
    CMADOT =   -6.0     # per radian, pitch damping coeff. per radian
    CLADOT =    0.0     # per radian
    RTOD   =   57.29578 # degrees/radian, radians to degrees conversion factor.
    GD     =   32.17    # ft/s2, gravity
