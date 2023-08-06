from veros.variables import Variable


grid = ("xt", "yt")
VARIABLES = dict(
    # sea ice
    hIceMean=Variable("Mean ice thickness", grid, "m"),
    hSnowMean=Variable("Mean snow thickness", grid, "m"),
    Area=Variable("Sea ice cover fraction", grid, " "),
    TSurf=Variable("Ice/ snow surface temperature", grid, "K"),
    SeaIceMassC=Variable("Sea ice mass centered around c point", grid, "kg"),
    SeaIceMassU=Variable("Sea ice mass centered around u point", grid, "kg"),
    SeaIceMassV=Variable("Sea ice mass centered around v point", grid, "kg"),
    SeaIceStrength=Variable("Ice Strength", grid, "N/m"),
    os_hIceMean=Variable("Overshoot of ice thickness from advection", grid, "m"),
    os_hSnowMean=Variable("Overshoot of snow thickness from advection", grid, "m/s"),
    AreaW=Variable("Sea ice cover fraction centered around u point", grid, " "),
    AreaS=Variable("Sea ice cover fraction centered around v point", grid, " "),
    uIce=Variable("Zonal ice velocity", grid, "m/s"),
    vIce=Variable("Merdidional ice velocity", grid, "m/s"),
    WindForcingX=Variable("Zonal forcing on ice by wind stress", grid, "N"),
    WindForcingY=Variable("Meridional forcing on ice by wind stress", grid, "N"),
    recip_hIceMean=Variable("1 / hIceMean", grid, "1/m"),
    SeaIceLoad=Variable("Load of sea ice on ocean surface", grid, "kg/m2"),
    IcePenetSW=Variable(
        "Shortwave radiation that penetrates through the ice", grid, "W/m2"
    ),
    # ocean
    uOcean=Variable("Zonal ocean surface velocity", grid, "m/s"),
    vOcean=Variable("Merdional ocean surface velocity", grid, "m/s"),
    theta=Variable("Ocean surface temperature", grid, "K"),
    ocSalt=Variable("Ocean surface salinity", grid, "g/kg"),
    Qnet=Variable("Net heat flux out of the ocean", grid, "W/m2"),
    OceanStressU=Variable("Zonal stress on ocean surface", grid, "N/m2"),
    OceanStressV=Variable("Meridional stress on ocean surface", grid, "N/m2"),
    saltflux=Variable("Salt flux into the ocean", grid, "m/s"),
    R_low=Variable("Sea floor depth (<0)", grid, "m"),
    ssh_an=Variable("Sea surface height anomaly", grid, "m"),
    # atmosphere
    Qsw=Variable("Surface shortwave heatflux (+ = upwards)", grid, "W/m2"),
    uWind=Variable("Zonal wind velocity", grid, "m/s"),
    vWind=Variable("Merdional wind velocity", grid, "m/s"),
    wSpeed=Variable("Total wind speed", grid, "m/s"),
    surfPress=Variable("Surface pressure", grid, "P"),
    SWdown=Variable("Downward shortwave radiation", grid, "W/m2"),
    LWdown=Variable("Downward longwave radiation", grid, "W/m2"),
    ATemp=Variable("Atmospheric temperature", grid, "K"),
    aqh=Variable("Atmospheric specific humidity", grid, "kg/kg"),
    precip=Variable("Precipitation rate (freshwater flux)", grid, "m/s"),
    snowfall=Variable("Snowfall rate", grid, "m/s"),
    evap=Variable(
        "Evaporation rate over open ocean (freshwater flux, <0 increases salinity)",
        grid,
        "m/s",
    ),
    runoff=Variable("Runoff into ocean", grid, "m/s"),
    EmPmR=Variable("Evaporation minus precipitation minus runoff", grid, "kg/m2 s"),
    # masks
    maskInC=Variable("Mask at c-points, used for open boundaries", grid, " "),
    maskInU=Variable("Mask at u-points, used for open boundaries", grid, " "),
    maskInV=Variable("Mask at v-points, used for open boundaries", grid, " "),
    iceMask=Variable("Mask at c-points", grid, " "),
    iceMaskU=Variable("Mask at u-points", grid, " "),
    iceMaskV=Variable("Mask at v-points", grid, " "),
    k1AtC=Variable(" ", grid, " "),
    k2AtC=Variable(" ", grid, " "),
    k1AtZ=Variable(" ", grid, " "),
    k2AtZ=Variable(" ", grid, " "),
    Fu=Variable("u-component of form factor", grid, " "),
    Fv=Variable("v-component of form factor ", grid, " "),
    # grid
    fCori=Variable("Coriolis parameter", grid, "1/s"),
    dxC=Variable("Zonal spacing of cell centers across western cell wall", grid, "m"),
    dyC=Variable(
        "Meridional spacing of cell centers across southern cell wall", grid, "m"
    ),
    dxG=Variable("Zonal spacing of cell faces along southern cell wall", grid, "m"),
    dyG=Variable("Meridional spacing of cell faces along western cell wall", grid, "m"),
    dxU=Variable("Zonal spacing of u-points through cell center", grid, "m"),
    dyU=Variable(
        "Meridional spacing of u-points through south-west corner of the cel", grid, "m"
    ),
    dxV=Variable(
        "Zonal spacing of v-points through south-west corner of the cell", grid, "m"
    ),
    dyV=Variable("Meridional spacing of v-points through cell center", grid, "m"),
    recip_dxC=Variable("1 / dxC", grid, "1/m"),
    recip_dyC=Variable("1 / dyC", grid, "1/m"),
    recip_dxG=Variable("1 / dxG", grid, "1/m"),
    recip_dyG=Variable("1 / dyG", grid, "1/m"),
    recip_dxU=Variable("1 / dxU", grid, "1/m"),
    recip_dyU=Variable("1 / dyU", grid, "1/m"),
    recip_dxV=Variable("1 / dxV", grid, "1/m"),
    recip_dyV=Variable("1 / dyV", grid, "1/m"),
    rA=Variable("Grid cell area centered around c-point", grid, "m2"),
    rAu=Variable("Grid cell area centered around u-point", grid, "m2"),
    rAv=Variable("Grid cell area centered around v-point", grid, "m2"),
    rAz=Variable("Grid cell area centered around z-point", grid, "m2"),
    recip_rA=Variable("1 / rA", grid, "1/m2"),
    recip_rAu=Variable("1 / rAu", grid, "1/m2"),
    recip_rAv=Variable("1 / rAv", grid, "1/m2"),
    recip_rAz=Variable("1 / rAz", grid, "1/m2"),
)
