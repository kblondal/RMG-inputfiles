#!/usr/bin/env python
# encoding: utf-8

name = "Seed_edge"
shortDesc = u""
longDesc = u"""

"""
autoGenerated=True
entry(
    index = 0,
    label = "[Pt]OO[Pt] <=> OX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 1,
    label = "X + CH3 <=> CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 2,
    label = "X + CO[Pt] <=> OX + CH3X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (162.416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 3,
    label = "X + X + C2H6 <=> CH3X + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 4,
    label = "X + X + CH3OH <=> CH3X + HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 5,
    label = "X + X + HOOH <=> HOX + HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 6,
    label = "[Pt]CO[Pt] <=> OX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 7,
    label = "X + CC[Pt] <=> CH3X + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (211.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 8,
    label = "X + OC[Pt] <=> HOX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (294.514, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 9,
    label = "[Pt]CC[Pt] <=> CH2X + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 10,
    label = "[Pt]OC=[Pt] <=> OX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 11,
    label = "X + CC=[Pt] <=> CH3X + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (157.671, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 12,
    label = "X + OC=[Pt] <=> HOX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (210.284, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 13,
    label = "[Pt]CC=[Pt] <=> CH2X + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 14,
    label = "[Pt]=CC=[Pt] <=> CHX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 15,
    label = "[Pt]OC#[Pt] <=> OX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 16,
    label = "X + CC#[Pt] <=> CH3X + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (263.776, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 17,
    label = "X + OC#[Pt] <=> HOX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (308.909, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 18,
    label = "[Pt]CC#[Pt] <=> CX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 19,
    label = "[Pt]=CC#[Pt] <=> CX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 20,
    label = "[Pt]#CC#[Pt] <=> CX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 21,
    label = "O=C([Pt])O[Pt] <=> OX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 22,
    label = "acetylX + X <=> CH3X + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (58.9312, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 23,
    label = "O=C([Pt])C[Pt] <=> CH2X + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 24,
    label = "O=C([Pt])C=[Pt] <=> OCX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 25,
    label = "O=C([Pt])C#[Pt] <=> CX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 26,
    label = "OCCOX <=> OCX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+09, '1/s'),
        n = 0,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined]\nEuclidian distance = 0\nfamily: Surface_Bidentate_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 27,
    label = "HOCO + X <=> HOCOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 28,
    label = "O=C(O)O[Pt] + X <=> HOCOX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (199.239, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 29,
    label = "acetic_acid + X + X <=> HOCOX + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 30,
    label = "O=C(O)O + X + X <=> HOCOX + HOX",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
        A = 0.02,
        n = 0,
        Ea = (98.4676, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 31,
    label = "formic_acid + X + X <=> HOCOX + HX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 32,
    label = "HOCOX + CH2X <=> OCX + OC[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 33,
    label = "CH2COOHX + X <=> HOCOX + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (227.842, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 34,
    label = "HOCOX + CHX <=> OCX + OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 35,
    label = "O=C(O)C=[Pt] + X <=> HOCOX + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (150.519, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 36,
    label = "HOCOX + CX <=> OCX + OC#[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 37,
    label = "O=C(O)C#[Pt] + X <=> HOCOX + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (291.948, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 38,
    label = "O=C(O)C(=O)[Pt] + X <=> HOCOX + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (47.8598, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 39,
    label = "O=C(O)C(=O)O + X + X <=> HOCOX + HOCOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 40,
    label = "OOO[Pt] + X <=> OX + OO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (41.2826, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 41,
    label = "CH3OOH + X + X <=> CH3X + OO[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 42,
    label = "OOO + X + X <=> HOX + OO[Pt]",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
        A = 0.02,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 43,
    label = "X + X + HOOH <=> HX + OO[Pt]",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
        A = 0.02,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 44,
    label = "CH2X + OO[Pt] <=> OX + OC[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 45,
    label = "OOC[Pt] + X <=> CH2X + OO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (170.423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 46,
    label = "CHX + OO[Pt] <=> OX + OC=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 47,
    label = "OOC=[Pt] + X <=> CHX + OO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (79.7586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 48,
    label = "CX + OO[Pt] <=> OX + OC#[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+15, 'm^2/(mol*s)'),
        n = 0,
        Ea = (80, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]\nEuclidian distance = 2.0\nfamily: Surface_Abstraction',
    ),
    longDesc = 
u"""
Estimated using template [Abstracting;Donating] for rate rule [Abstracting;R-OH]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 49,
    label = "OOC#[Pt] + X <=> CX + OO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (272.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 50,
    label = "O=C([Pt])OO + X <=> OCX + OO[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (67.2106, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 51,
    label = "O=C(O)OO + X + X <=> HOCOX + OO[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (129.506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 52,
    label = "OOOO + X + X <=> OO[Pt] + OO[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 53,
    label = "HCO + X <=> O=C[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Single',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 54,
    label = "formyloxyX + X <=> O=C[Pt] + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (107.88, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 55,
    label = "CH3CHO + X + X <=> O=C[Pt] + CH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 56,
    label = "formic_acid + X + X <=> O=C[Pt] + HOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 57,
    label = "CH2O + X + X <=> O=C[Pt] + HX",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(
        A = 0.02,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nMultiplied by reaction path degeneracy 2.0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 58,
    label = "vinoxyX + X <=> O=C[Pt] + CH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (128.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 59,
    label = "ketene(T)X + X <=> O=C[Pt] + CHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (138.786, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 60,
    label = "O=CC#[Pt] + X <=> O=C[Pt] + CX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (238.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 61,
    label = "OCHCOX + X <=> O=C[Pt] + OCX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(
        A = (1e+17, 'm^2/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Combined;VacantSite]\nEuclidian distance = 0\nfamily: Surface_Dissociation',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_Dissociation
""",
)

entry(
    index = 62,
    label = "O=CC(=O)O + X + X <=> O=C[Pt] + HOCOX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 63,
    label = "OCHOOH + X + X <=> O=C[Pt] + OO[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 64,
    label = "glyoxal + X + X <=> O=C[Pt] + O=C[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(
        A = 0.01,
        n = 0,
        Ea = (41.84, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
        comment = 'Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]\nEuclidian distance = 0\nfamily: Surface_Adsorption_Dissociative',
    ),
    longDesc = 
u"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
family: Surface_Adsorption_Dissociative
""",
)

