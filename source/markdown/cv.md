```#yaml
title: Curriculum Vitae
author: Don Willcox
template: cv.j2
encoding: utf-8
enable_jinja: true
```

```#yaml
cvdata:
  Employment:
    - name: "Most Recent Position"
      division: "Applied Mathematics and Computational Research Division"
      location: "Lawrence Berkeley National Laboratory"
      address: |
        1 Cyclotron Road Mailstop 50A3111
        Berkeley, CA 94720
      positions:
        - ystart: 2022
          yend: 2024
          title: "Project Scientist"
          division: "Center for Computational Sciences and Engineering"
          location: "Lawrence Berkeley National Laboratory"
        - ystart: 2018
          yend: 2022
          title: "Postdoctoral Researcher"
          division: "Center for Computational Sciences and Engineering"
          location: "Lawrence Berkeley National Laboratory"
  Education:
    - institution: "Stony Brook University"
      location: "Stony Brook, NY, USA"
      achievements:
        - title: "Ph.D., Physics, August 2018"
    - institution: "LeTourneau University"
      location: "Longview, TX, USA"
      achievements:
        - title: "B.S., Engineering Physics, May 2011"
        - title: "B.S., Electrical Engineering, May 2011"
        - title: "Minors: Mathematics, Applied Sciences"
  Fellowships:
    - ystart: 2011
      yend: 2018
      title: "Turner Fellow"
      institution: "Stony Brook University Center for Inclusive Education"
    - ystart: 2007
      yend: 2011
      title: "Heritage Scholarship"
      institution: "LeTourneau University"
  FundingProposals:
    - year: 2023
      status: "Partially Funded"
      authorship: "Principal Investigator"
      institution: "Berkeley Lab FY 2024 Multi-Area LDRD"
      coauthors: "Co-Investigator: Hector Garcia Martin (LBNL, Biosciences Area)"
      name: "Bioreactor digital twinning - Accelerating bioprocess scaling by combining computational fluid dynamics with metabolic modeling"
    - year: 2023
      status: "Not Funded"
      authorship: "Principal Investigator"
      institution: "DOE Wind Energy Technologies Office"
      coauthors: "Co-Investigators: Adam Lavely (LBNL), Ganesh Vijayakumar (NREL)"
      name: "Advancing AMR-Wind Turbine Simulations With Machine Learning"
    - year: 2023
      status: "Not Funded"
      authorship: "Principal Investigator"
      institution: "DOE Wind Energy Technologies Office"
      coauthors: ""
      name: "Artificial Intelligence for Multiscale Wind Modeling with the ERF Simulation Code"
  ComputingAllocations:
    - year: 2023
      status: "Awarded: 400 k node-hours on Summit, 300 k node-hours on Frontier, 100 k node-hours on Polaris"
      authorship: "Co-Investigator"
      institution: "INCITE 2023 award"
      name: "Exascale Models of Astrophysical Thermonuclear Explosions"
    - year: 2022
      status: "Awarded: 590 k node-hours on Summit"
      authorship: "Co-Investigator"
      institution: "INCITE 2022 award at OLCF"
      name: "Approaching Exascale Models of Astrophysical Explosions"
    - year: 2021
      status: "Awarded: 30 M MPP hours"
      authorship: "Senior Investigator"
      institution: "NERSC 2021 Allocation"
      name: "Three-dimensional studies of white dwarfs, massive stars, and neutron star systems"
    - year: 2021
      status: "Awarded: 18 M MPP hours"
      authorship: "Senior Investigator"
      institution: "NERSC 2021 Allocation"
      name: "Neutrino Flavor Transformation in Neutron Star Mergers"
    - year: 2021
      status: "Awarded: 13 M MPP hours"
      authorship: "Senior Investigator"
      institution: "NERSC 2021 Allocation"
      name: "Astrophysics of Supernova Progenitors"
    - year: 2020
      status: "Awarded: 30 M MPP hours"
      authorship: "Senior Investigator"
      institution: "NERSC 2020 Allocation"
      name: "Three-dimensional studies of white dwarfs, massive stars, and neutron star systems"
    - year: "2019-2020"
      status: "Awarded 2019: 1.5 M node-hours on Titan, 105 k node-hours on Summit; Awarded 2020: 300 k node-hours on Summit"
      authorship: "Co-Investigator"
      institution: "INCITE 2019 award at OLCF"
      name: "Approaching Exascale Models of Astrophysical Explosions"
    - year: 2018
      status: "Awarded: 20.8 M MPP hours"
      authorship: "Senior Investigator"
      institution: "NERSC 2018 Allocation"
      name: "Three-dimensional studies of white dwarf and neutron star systems"
    - year: 2018
      status: "Awarded: 40 Mh"
      authorship: "Co-Investigator"
      institution: "INCITE 2018 award at OLCF"
      name: "Approaching Exascale Models of Astrophysical Explosions"
  ScientificSoftware:
    - year: ongoing
      description: "Co-creator of the Emu simulation code for astrophysical neutrino quantum kinetics in 6-dimensional phase space"
      link: "https://github.com/amrex-astro/Emu"
    - year: ongoing
      description: "Core developer of the Castro simulation code for astrophysical radiation-hydrodynamics on adaptive meshes"
      link: "https://github.com/amrex-astro/Castro"
    - year: ongoing
      description: "Core developer of the StarKiller Microphysics code, a collection of publicly-available astrophysical microphysics routines and nuclear reaction network integrators"
      link: "https://github.com/starkiller-astro/Microphysics"
    - year: ongoing
      description: "Co-developer of pynucastro, a publicly-available Python interface to the JINA Reaclib nuclear reaction rate database for rate visualization and ODE right hand side code generation in Python and C++"
      link: "https://github.com/pynucastro/pynucastro"
    - year: ongoing
      description: "Co-creator of the StarSTRUQ github organization for publicly-available code implementing uncertainty quantification algorithms useful for stellar evolution calculations"
      link: "https://github.com/StarSTRUQ"
    - year: ongoing
      description: "Core developer of the ERF simulation code for large-scale (ie. mesoscopic) weather modeling"
      link: "https://github.com/erf-model/erf"
  ResearchAdvising:
    - year: "2019–2021"
      role: "Co-mentor for LBNL intern"
      name: "Eloise Yang"
    - year: "2020–2021"
      role: "Associate mentor for Fall 2020 & Spring 2021 DOE SULI intern at LBNL"
      name: "Nicole Ford"
    - year: "Summer 2021"
      role: "Mentor for NSF MSGI intern at LBNL"
      name: "Chris Degrendele"
    - year: "Summer 2020"
      role: "Mentor for LBNL summer intern"
      name: "Chris Degrendele"
    - year: "Summer 2020"
      role: "Mentor for NSF MSGI intern at LBNL"
      name: "Ty Frazier"
    - year: "Summer 2019"
      role: "Co-mentor for LBNL summer intern"
      name: "Chris Degrendele"
    - year: "Summer 2019"
      role: "Co-mentor for LBNL summer intern"
      name: "Kiran Eiden"
  ProfessionalService:
    - year: ongoing
      service: "Referee for the Astrophysical Journal"
    - year: ongoing
      service: "Referee for Communications in Applied Mathematics and Computational Science"
    - year: 2021
      service: "Organizer for SIAM CSE 2021 Minisymposium MS137: Machine Learning Approaches in Computational Astrophysics and Cosmology"
  ProfessionalDevelopment:
    - year: 2019
      task: "Participated in GPU Hackathon organized by NERSC"
    - year: 2018
      task: "Participated in GPU Hackathon at Brookhaven National Laboratory"
    - year: 2018
      task: "Participated in GPU Hackathon at University of Colorado, Boulder"
    - year: 2018
      task: "Achieved Software Carpentry instructor certification"
    - year: 2017
      task: "Participated in GPU Hackathon at Brookhaven National Laboratory"
    - year: 2016
      task: "Participated in GPU Hackathon hosted by the Oak Ridge Leadership Computing Facility"
    - year: 2015
      task: "Participated in GPU Hackathon hosted by the Oak Ridge Leadership Computing Facility"
    - year: 2015
      task: "Studied at the Argonne Training Program on Extreme-Scale Computing"
    - year: 2014
      task: "Studied at the MESA Summer School for simulating massive stars, accreting white dwarfs, stellar mixing processes and more at UC Santa Barbara"
    - year: 2014
      task: "Studied at the JINA TALENT Course on Nuclear Theory for Astrophysics at Michigan State University"
  CommunityOutreach:
    - year: "10/20/2020"
      task: "Panelist at CAUSE Career Panel, University of Minnesota"
    - year: "06/18/2019"
      task: "How to Simulate a Thermonuclear Supernova - public talk at the Berkeley Public Library"
    - year: "01/2019"
      task: "Judge for Chambliss poster competition at the 233rd Meeting of the American Astronomical Society"
    - year: "02/21/2018"
      task: "Saturn in 13 Years: the Cassini-Huygens Mission - public talk at the Astronomical Society of Long Island, Vanderbilt Museum and Planetarium"
    - year: "11/03/2017"
      task: "Saturn in 13 Years: the Cassini-Huygens Mission - public talk in the Astronomy Open Night Series, Stony Brook University"
  TeachingExperience:
    - institution: LBNL
      courses:
        - year: "2019,2020,2021"
          name: "ATPESC Lecturer Support Staff"
          description: "Designed and presented hands-on exercises for the AMReX code at the Argonne Training Program on Extreme-Scale Computing."
    - institution: Stony Brook University
      courses:
        - year: "Spring 2017"
          name: "WISE Computational Astrophysics"
          description: "Co-instructor for a computational astrophysics course for the Women In Science and Engineering program."
        - year: "Summer 2015"
          name: "IACS Computes!"
          description: "Teaching assistant for a Python programming workshop for high school students by the Institute for Advanced Computational Sciences."
        - year: "Spring 2014"
          name: "Astronomy"
          description: "Teaching assistant for an undergraduate astronomy course."
        - year: "Spring 2013"
          name: "Modern Physics"
          description: "Instructor for an undergraduate laboratory on relativity and quantum mechanics."
        - year: "Summer 2012"
          name: "Introduction to Calculus II"
          description: "Instructor for a 3-week course on integral calculus for incoming freshman students."
        - year: "2012"
          name: "Introductory Physics"
          description: "Instructor for undergraduate laboratory on electricity and magnetism."
    - institution: LeTourneau University
      courses:
        - year: "Fall, 2008-2010"
          name: "Electricity and Magnetism"
          description: "Recitation instructor for undergraduates taking the physics course on electricity and magnetism."
        - year: "Spring 2010"
          name: "Classical Mechanics"
          description: "Recitation instructor for undergraduates taking the physics course on classical mechanics."
```
