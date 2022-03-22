# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:38:04 2021

@author: siirias
"""
articles = \
"""
A1	Jonsson, P. R., J. Kotta, H. C. Andersson, K. Herkül, E. Virtanen, A. N. Sandman, and K. Johannesson (2018). High climate velocity and population fragmentation may constrain climate-driven range shift of the key habitat former Fucus vesiculosus. Diversity and Distributions 24:892-905.		https://onlinelibrary.wiley.com/doi/full/10.1111/ddi.12733					K				1
A1	Kaikkonen, L., Virtanen, E. A., Kostamo, K., Lappalainen, J., & Kotilainen, A. T. (2019). Extensive coverage of marine mineral concretions revealed in shallow shelf sea areas. Frontiers in Marine Science, 6, 541. 		https://doi.org/10.3389/fmars.2019.00541					K				1
A1	Kaikkonen, L., Parviainen, T., Rahikainen, M., Uusitalo, L., & Lehikoinen, A. (2020). Bayesian Networks in Environmental Risk Assessment: A review. Integrated Environmental Assessment and Management. DOI: 10.1002/ieam.4332		 https://doi.org/10.1002/ieam.4332					K				1
B3	Kaskela, A.M., Hämäläinen, J., Kotilainen, A.T., Virtasalo, J. (2016). Marine geological data as a basis for sustainable growth, an example from the Gulf of Bothnia, Finland (Poster). 35th International Geological Congress, 27th August – 2nd September 2016, Cape Town, South Africa.											1
A1	Kaskela, A.M., Kotilainen, A.T., (2017). Seabed geodiversity in a glaciated shelf area, the Baltic Sea. Geomorphology, 295, 419–435.		https://doi.org/10.1016/j.geomorph.2017.07.014					E				1
B3	Kaskela, A.M., Kotilainen, A.T. (2017). Seabed geodiversity of the Baltic Sea. In: Todd, B.J. et al. (Eds.), The GeoHab 2017 Conference: marine geological and biological habitat mapping, 1-5 May, 2017, Dartmouth, Nova Scotia, Canada: Program and Abstracts, 63.											1
B3	Kaskela, A.M., Kotilainen, A.T. (2017). Quantifying seabed geodiversity of the Baltic Sea. In: 11th Baltic Sea Science Congress, 12-16, June 2017, Rostock, Germany: Abstract Book. 37. (Oral).											1
A1	Kaskela, A.M., Kotilainen, A.T., Alanen, U., Cooper, R., Green, S., Guinan, J., van Heteren, S., Kihlman, S., Van Lancker, V., Stevenson, A., the EMODnet Geology Partners, (2019). Picking Up the Pieces—Harmonising and Collating Seabed Substrate Data for European Maritime Areas. Geosciences 2019, 9, 84. doi:10.3390/geosciences9020084		https://doi.org/10.3390/geosciences9020084					K				1
B3	Kotilainen, A.T., Alvi, K., Boman, A., Hämäläinen, J., Kaskela, A.M., Rantataro, J., Vallius, H., Virtasalo, J., SmartSea project partners, (2016). SmartSea - Gulf of Bothnia as Resource for Blue Growth. (Poster). In: The 13th Colloquium on Baltic Sea Marine Geology, September 12 – 16, 2016, Gdansk, Poland. Abstract Volume. 385, 250–259.							E				1
B3	Kotilainen, A.T., Alvi, K., Boman, A., Hämäläinen, J., Kaskela, A.M., Rantataro, J., Vallius, H., Virtasalo, J., SmartSea project partners, (2017). The Gulf of Bothnia as resource for Blue Growth: SmartSea. In Hölttä, P., Nenonen, K. & Eerola, T. (eds) 2017. 3rd Finnish National Colloquium of Geosciences, Espoo, 15−16 March 2017, Abstract Book. Geological Survey of Finland, Guide 63, 55. (Poster presentation).											1
B3	Kotilainen, A.T., Alvi, K., Boman, A., Hämäläinen, J., Kaskela, A.M., Rantataro, J., Vallius, H., Virtasalo, J. (2017). Coastal seas as resource for Blue Growth – SmartSea project. Geophysical Research Abstracts, Vol. 19, EGU2017-15357, 2017. EGU General Assembly 2017. (Poster).											1
A1	Denderen, van, PD, Bolam, SG, Friedland, R, Hiddink, JG, Norén, K., Rijnsdorp, AD., Sköld, M., Törnroos, A., Virtanen, EA., & Valanko, S. (2019). Evaluating impacts of bottom trawling and hypoxia on benthic communities at the local, habitat and regional scale using a modelling approach. ICES Journal of Marine Science, fsz219		https://doi.org/10.1093/icesjms/fsz219					K				2
A1	Gagnon, K., Virtanen, E. A., Rusanen, P., Nurmi, M., Viitasalo, M., & Jormalainen, V. (2020). Cormorants have negligible seascape-scale impacts on benthic vegetation communities. Marine Ecology Progress Series, 654, 195-207. 							E				2
A1	Fransner, F., Gustafsson, E., Tedesco, L., Vichi, M., Hordoir, R., Roquet, F., … Nycander, J. (2018). Non-Redfieldian dynamics explain seasonal pCO2 drawdown in the Gulf of Bothnia. Journal of Geophysical Research: Oceans, 123. 		https://doi.org/10.1002/2017JC013019					K				2
A1	Kallasvuo, M., Vanhatalo, J., & Veneranta, L. (2017). Modeling the spatial distribution of larval fish abundance provides essential information for management. Canadian Journal of Fisheries and Aquatic Sciences. 74(5): 636-649.		https://doi.org/10.1139/cjfas-2016-0008					E				2
A1	Kallio-Nyberg, I.,  Saloniemi, I., Koljonen, M.-L. (2020). Increasing temperature associated with increasing grilse proportion and smaller grilse size of Atlantic salmon. Journal of Applied Ichthyology. doi: 10.1111/jai.14033		https://doi.org/10.1111/jai.14033					K				2
A1	Kallio-Nyberg, I., Veneranta, L., Saloniemi, I., Salminen, M. (2018). Anadromous trout threatened by whitefish gill-net fisheries in the northern Baltic Sea. Journal of Applied Ichthyology. doi: 10.1111/jai.13771		 https://doi.org/10.1111/jai.13771					K				2
A1	Kotilainen, A.T., Kotilainen, M.M., Vartti, V.-P., Hutri, K.-L., Virtasalo, J.J. (2021). Chernobyl still with us: 137Caesium activity contents in seabed sediments from the Gulf of Bothnia, northern Baltic Sea. Marine Pollution Bulletin. 172. 		https://doi.org/10.1016/j.marpolbul.2021.112924					K				2
A1	Kotta, J., Futter, M., Kaasik, A., Liversage, K., Rätsep, M., Barboza, F. R., . . . Virtanen, E. (2020). Cleaning up seas using blue growth initiatives: Mussel farming for eutrophication control in the Baltic Sea. Science of The Total Environment, 709, 136144. 		https://doi.org/10.1016/j.scitotenv.2019.136144					K				2
A1	Lappalainen, J., Virtanen, E., Kallio, K., Junttila, S., Viitasalo, M. (2019). Substrate limitation of a habitat-forming genus Fucus under different water clarity scenarios in the northern Baltic Sea. Estuarine, Coastal and Shelf Science 218: 31-38. 		https://www.sciencedirect.com/science/article/pii/S027277141730940X					K				2
A1	Mitchell, P.J., Spence, M.A., Aldridge, J., Kotilainen, A.T., Diesing, M. (2021). Sedimentation rates in the Baltic Sea: A machine learning approach. Continental Shelf Research, 214. https://doi.org/10.1016/j.csr.2020.104325. ISSN 0278-4343		https://doi.org/10.1016/j.csr.2020.104325					E				2
A1	Repka, S., Erkkilä-Välimäki, A. Jonson, J.A., Posch, M., Törrönen, J. and Jalkanen, J-P. (2021). IMO regulation of ship-originated SOx and NOx in the Baltic Sea: Assessing the costs and environmental impacts. Ambio, published online		https://doi.org/10.1007/s13280-021-01500-6					K				2
A1	Rahikainen, M., Hoviniemi, K., Mäntyniemi, S., Vanhatalo, J., Helle, I., Lehtiniemi, M., Pönni, J., Kuikka, S. (2017). Impacts of eutrophication and oil spills on the Gulf of Finland herring stock. Canadian Journal of Fisheries and Aquatic Sciences. DOI 10.1139/cjfas-2016-0108		https://doi.org/10.1139/cjfas-2016-0108					E				2
A1	Virtanen, E. A., Moilanen, A., & Viitasalo, M. (2020). Marine connectivity in spatial conservation planning: analogues from the terrestrial realm. Landscape Ecology, 35(5), 1021-1034. doi:10.1007/s10980-020-00997-8		https://doi.org/10.1007/s10980-020-00997-8					K				2
A1	Virtasalo, J.J., Korpinen, S., Kotilainen, A.T. (2018). Assessment of the influence of dredge spoil dumping on the seafloor geological integrity. Frontiers in Marine Science 5:131. doi: 10.3389/fmars.2018.00131		https://doi.org/10.3389/fmars.2018.00131					K				2
B3	Virtasalo, J.J., Kotilainen, A.T. (2017). Assessment of human and climate change impacts on the coastal Baltic Sea floor. In: 11th Baltic Sea Science Congress, 12-16, June 2017, Rostock, Germany: Abstract Book. (Poster).											2
A1	Virtasalo, J.J., Österholm, P., Kotilainen, A.T., Åström, M.E. (2020). Enrichment of trace metals from acid sulphate soils in sediments of the Kvarken Archipelago, eastern Gulf of Bothnia, Baltic Sea. Biogeosciences 17, 6097-6113.		https://doi.org/10.5194/bg-17-6097-2020					K				2
A1	Björkqvist, Jan-Victor & Rikka, Sander & Alari, Victor & Männik, Aarne & Tuomi, Laura & Pettersson, Heidi. (2020). Wave height return periods from combined measurement–model data: A Baltic Sea case study. 10.5194/nhess-2020-190. 		https://doi.org/10.5194/nhess-2020-190					K				3
A1	Björkqvist, Jan-Victor & Tuomi, Laura & Tollman, Niko & Kangas, Antti & Pettersson, Heidi & Marjamaa, Riikka & Jokinen, Hannu & Fortelius, Carl. (2017). Brief communication: Characteristic properties of extreme wave events in the Baltic Sea. Natural Hazards and Earth System Sciences Discussions. 17. 1-8. 10.5194/nhess-17-1653-2017. 		https://doi.org/10.5194/nhess-17-1653-2017					K				3
A1	Gröger, M., Dieterich, C., Haapala, J., Ho-Hagemann, H. T. M., Hagemann, S., Jakacki, J., May, W., Meier, H. E. M., Miller, P. A., Rutgersson, A., and Wu, L.: Coupled regional Earth system modelling in the Baltic Sea region, Earth Syst. Dynam., 12, 939–973, https://doi.org/10.5194/esd-12-939-2021, 2021		https://esd.copernicus.org/articles/12/939/2021/					K				3
A1	Haavisto N, Tuomi L, Roiha P, Siiria SM, Alenius P, Purokoski T. 2018.  Argo floats as a novel part of the monitoring the hydrography of the Bothnian Sea. Frontiers in Marine Science. 5:324. 		https://www.frontiersin.org/article/10.3389/fmars.2018.00324					K				3
A1	Höglund A., Pemberton P., Hordoir R. & Schimanke S. 2017. Ice conditions for maritime traffic in the Baltic Sea in future climate. Boreal Environment Research 22: 245–265.		http://www.borenv.net/BER/archive/pdfs/ber22/ber22-245-265.pdf					K				3
A1	Hordoir, R., Axell, L., Höglund, A., Dieterich, C., Fransner, F., Gröger, M., Liu, Y., Pemberton, P., Schimanke, S., Andersson, H., Ljungemyr, P., Nygren, P., Falahat, S., Nord, A., Jönsson, A., Lake, I., Döös, K., Hieronymus, M., Dietze, H., Löptien, U., Kuznetsov, I., Westerlund, A., Tuomi, L., Haapala, J. (2019)  "Nemo-Nordic 1.0: a NEMO-based ocean model for the Baltic and North seas – research and operational applications", Geosci. Model Dev., 12, 363–386, 2019		https://doi.org/10.5194/gmd-12-363-2019					K				3
A1	Hordoir, R., Höglund, A., Pemberton, P., & Schimanke, S. (2017). Sensitivity of the overturning circulation of the Baltic Sea to climate change, a numerical experiment. Climate Dynamics, 1-13. DOI 10.1007/s00382-017-3695-9. "Nemo-Nordic 1.0: a NEMO-based ocean model for the Baltic and North seas - research and operational applications", 2019, Geoscientific Model Development, vol 12, no. 1, p. 363-386. DOI: 10.5194/gmd-12-363-2019		https://doi.org/10.5194/gmd-12-363-2019					K				3
A1	Hordoir R., Samuelsson P., Schimanke S., Fransner F. Changes of the overturning of a fjord-type estuary in a warmer climate, a test case in the Northern Baltic sea, Continental Shelf Research, Volume 191, 2019, 104007, ISSN 0278-4343. 		https://doi.org/10.1016/j.csr.2019.104007					E				3
A1	Kaikkonen, L., Venesjärvi, R., Nygård, H., Kuikka, S. (2018). Assessing the impacts of seabed mineral extraction in the deep sea and coastal marine environments: Current methods and recommendations for environmental risk assessment. Marine Pollution Bulletin, 135, 1183–1197. 		https://doi.org/10.1016/j.marpolbul.2018.08.055					K				3
A1	Kotta, J., Vanhatalo, J., Jänes, H., Orav-Kotta, H., Rugiu, L., Jormalainen, V., Bobsien, I., Viitasalo, M., Virtanen, E., Sandman Nyström, A., Isaeus, M., Leidenberger, S., Jonsson, P., Johannesson, K. (2019). Integrating experimental and distribution data to predict future species patterns. Scientific Reports 9(1), 1821. 		https://doi.org/10.1038/s41598-018-38416-3					K				3
A1	"H. E. Markus Meier, Madline Kniebusch, Christian Dieterich, Matthias Gröger, Eduardo Zorita, Ragnar Elmgren, Kai Myrberg, Markus Ahola, Alena Bartosova, Erik Bonsdorff, Florian Börgel, Rene Capell, Ida Carlén, Thomas Carlund, Jacob Carstensen, Ole B. Christensen, Volker Dierschke, Claudia Frauen, Morten Frederiksen, Elie Gaget, Anders Galatius, Jari J. Haapala, Antti Halkka, Gustaf Hugelius, Birgit Hünicke, Jaak Jaagus, Mart Jüssi, Jukka Käyhkö, Nina Kirchner, Erik Kjellström, Karol Kulinski, Andreas Lehmann, Göran Lindström, Wilhelm May, Paul Miller, Volker Mohrholz, Bärbel Müller-Karulis, Diego Pavón-Jordán, Markus Quante, Marcus Reckermann, Anna Rutgersson, Oleg P. Savchuk, Martin Stendel, Laura Tuomi, Markku Viitasalo, Ralf Weisse, and Wenyan Zhang
Earth Syst. Dynam. Discuss., https://doi.org/10.5194/esd-2021-67, 2021"		https://esd.copernicus.org/preprints/esd-2021-67/					K				3
A1	Moros, M., Kotilainen, A.T., Snowball, I., Neumann, T., Perner, K., Meier, H.E.M., Leipe, T., Zillén, L., Sinninghe Damsté, J.S., Schneider, R., (2020). Is ‘deep-water formation’ in the Baltic Sea a key to understanding seabed dynamics and ventilation changes over the past 7,000 years? Quaternary International, 550, 55-65.		https://doi.org/10.1016/j.quaint.2020.03.031					E				3
A1	Ø. Paasche, H. Österblom, S. Neuenfeldt, E. Bonsdorff, K. Brander, D. Conley, J. Durant, A. Eikeset, A. Goksøyr, S. Jónsson, O. Kjesbu, A. Kuparinen & N. Stenseth, (2015), "Connecting the Seas of Norden", Nature Climate Change volume 5, pages 89–92.		http://dx.doi.org/10.1038/nclimate2471					E				3
A1	Pemberton, P., Löptien, U., Hordoir, R., Höglund, A., Schimanke, S., Axell, L., and Haapala, J.: Sea-ice evaluation of NEMO-Nordic 1.0: a NEMO–LIM3.6-based ocean–sea-ice model setup for the North Sea and Baltic Sea, Geosci. Model Dev., 10, 3105–3123, 2017.		https://doi.org/10.5194/gmd-10-3105-2017					K				3
A1	Roiha P, Siiria SM, Haavisto N, Alenius P, Westerlund A, Purokoski T. 2018. Estimating currents from Argo trajectories in the Bothnian Sea, Baltic Sea. Frontiers in Marine Science. 5:308.		https://www.frontiersin.org/articles/10.3389/fmars.2018.00308/full					K				3
A1	Rutgersson, Anna & Kjellström, Erik & Haapala, Jari & Stendel, Martin & Danilovich, Irina & Drews, Martin & Jylhä, Kirsti & Kujala, P. & Larsén, Xiaoli & Halsnæs, Kirsten & Lehtonen, Ilari & Luomaranta, Anna & Nilsson, Erik & Olsson, Taru & Särkkä, Jani & Tuomi, Laura & Wasmund, N.. (2022). Natural Hazards and Extreme Events in the Baltic Sea region. Earth Syst. Dynam., 13, 251–301, https://doi.org/10.5194/esd-13-251-2022, 2022 		https://www.researchgate.net/publication/350669024_Natural_Hazards_and_Extreme_Events_in_the_Baltic_Sea_region					K				3
A1	Tedesco L, Miettunen E, An BW, Haapala J, Kaartokallio H. Long-term mesoscale variability of modelled sea-ice primary production in the northern Baltic Sea. Elem Sci Anth. 2017;5:29.		http://doi.org/10.1525/elementa.223									3
A1	Tuomi L, Kanarik H, Björkqvist J-V, Marjamaa R, Vainio J, Hordoir R, Höglund A and Kahma KK (2019) Impact of Ice Data Quality and Treatment on Wave Hindcast Statistics in Seasonally Ice-Covered Seas. Front. Earth Sci. 7:166. doi: 10.3389/feart.2019.00166		https://www.frontiersin.org/articles/10.3389/feart.2019.00166/full					K				3
A1	Vanhatalo, J. Hartmann, M., Veneranta, L. 2019. Joint species distribution modeling with additive multivariate Gaussian process priors and heterogenous data. Bayesian analysis, doi:0.1214/19-BA1158		https://doi.org/10.1214/19-BA1158					K				3
A1	Vanhatalo, J. P., Hartmann, M., & Veneranta, L. (2019). Additive multivariate Gaussian processes for joint species distribution modeling with heterogeneous data. Bayesian analysis.		https://doi.org/doi:10.1214/19-BA1158					K				3
A1	Veneranta, L., Vanhatalo, J., & Urho, L. (2016). Detailed temperature mapping–Warming characterizes archipelago zones. Estuarine, Coastal and Shelf Science, 182, 123-135.		https://doi.org/10.1016/j.ecss.2016.09.011					K				3
A4	Venesjärvi R, Carson R, Jolma J & Kuikka S, Decision analysis between the use of marine resources and ecosystem conservation, Submitted abstract											3
A3	Viitasalo, M. (2019). Impacts of climate change on the ecosystem of the Baltic Sea. Oxford Research Encyclopedia of Climate Change. Oxford University Press. 32 pp.		https://doi.org/10.1093/acrefore/9780190228620.013.692					E				3
A1	Virtanen, E.A., Norkko, A., Nyström Sandman, A., Viitasalo, M. (2019). Identifying areas prone to coastal hypoxia - the role of topography. Biogeosciences 16: 3183-3195. 		https://doi.org/10.5194/bg-16-3183-2019					K				3
A1	Whitlock R. E., Kopra, J., Pakarinen, T., Jutila, E., Leach, A., Levontin, P., Kuikka, S. and Romakkaniemi, A. (2016) Mark-recapture estimation of mortality and migration rates for sea trout (Salmo trutta) in the northern Baltic Sea doi:10.1093/icesjms/fsw152.		https://doi.org/10.1093/icesjms/fsw152					K				3
A1	Weigel, B., Mäkinen, J., Kallasvuo, M., Vanhatalo, J. 2021. Exposing changing phenology of fish larvae by modeling climate effects on temporal early life-stage shifts. Marine Ecology Progress Series 666:135-148. 		https://doi.org/10.3354/meps13676					K				3
B1	Haapala, J. 2016. Blue Growth – a facelift or a new model to utilize marine resources?  Baltic Rim Economics Review, 4/2016, p.45		https://sites.utu.fi/bre/wp-content/uploads/sites/227/2019/04/BRE_4_2016.pdf					K				4
A4	Heinonen, J & Rissanen, S 2016, Simulation of drifting sea ice interaction with an offshore wind turbine: feasibility study of FAST simulation software. in Proceedings of ICSOS 2016. Hamburg University of Technology, pp. 173-182, International Conference on Ships and Offshore Structures, ICSOS 2016, Hamburg, Germany, 31/08/16Structures		https://cdn.website-editor.net/s/a88a366fb4174f939aa349fe67bc7d1e/files/uploaded/ICSOS2016_proceedings_contents.pdf?Expires=1647202832&Signature=CumxHi1l2OrhGy-BDDVp9HvGbbvSsSi~l46qZ1Uh04xZNpy8vRpHNsyx620Cf8aOiA7ZjrHLvazKOUp~bXJTbkguR8lFGL~~qa2AKaL387o-zoBDw6FbHBFxjQ5z0mvw195Q-JeWvb81Sg2PW8Tw6-kDQRgw4ZBvXpFzkeDGrBKz6nfj5jZ~9QQAxga7i83zCALO9Zmd0NF6wVU-dtZWmkjnOnt69sYQTliZW2RYOirMyDdnxAQ8wfhBgRVu68JoS~PgoHLKEmEottDTbpGvMi7Db5iaXP~yAdJWqDDursX8l52LrGJZmh2nRzKXvnM5f-Vb04juj3bZBhEZwbJ9ow__&Key-Pair-Id=K2NXBXLF010TJW					E				4
A4	Heinonen, J. CEL-Analysis of Punch Shear Tests to Evaluate Mechanical Properties of Ice Rubble, 23nd  IAHR International Symposium on Ice, Ann Arbor, Michigan USA, May 31 to June 3, 2016		https://www.iahr.org/library/infor?pid=18453					K				4
A1	Heinonen, J., Rissanen, S. 2017. Coupled-crushing analysis of a sea ice-wind turbine interaction – feasibility study of FAST simulation software, Ships and Offshore Structures		https://doi.org/10.1080/17445302.2017.1308782					E				4
A4	Heinonen, J & Rissanen, S 2016, 'Numerical comparison of drifting sea ice and wave loads on different offshore wind turbine support structures', Paper presented at WindEurope Summit 2016, HamburgGermany, 27/09/16 - 29/09/16		http://windeurope.org/summit2016/conference/submit-an-abstract/pdf/97525490176.pdf									4
A4	Heinonen, J, Tikanmäki, M, Kurkela, J, Klinge, P, Hekkala, T, Koskela, J, Montonen, A & Eriksson, PB. 2018, Ice load design portal for sub-structures in offshore wind turbines in ice-covered sea areas. in Proceedings of the 28th International Ocean and Polar Engineering Conference, ISOPE 2018. vol. 2018-June, pp. 475-482, 28th International Ocean and Polar Engineering Conference, ISOPE 2018, Sapporo, Japan, 10/06/18		http://publications.isope.org/proceedings/ISOPE/ISOPE%202018/data/index.html									4
B3	Heinonen, J., Klinge, P., Kolari, K., Kurkela J. 2018. Modelling structural performance of offshore wind turbine support structures in ice-infested waters by using design load portal, The Tenth International Conference on Engineering Computational Technology (ECT2018), Sitges, Barcelona, Spain, 4-6 September 2018							E				4
A3	Heinonen, J.. 2020. Ridge Load on the Monopile - a Comparison Between FEM-CEL – Simulations and ISO 19906,  IUTAM SYMPOSIUM ON PHYSICS AND MECHANICS OF SEA ICE - JUNE 3-7, 2019, Espoo, Finland		DOI: 10.1007/978-3-030-80439-8_11					E				4
A4	Heinonen, J., Tikanmäki, M., Mikkola, E., Perälä, I., Shestov, A., Høyland, K.V., Salganik, E., van den Berg, M., Li, H., Jiang, Z., Ervik, Å.,  Puolakka, O. 2021. Scale-model ridges and interaction with narrow structures, Part 3 Analysis of Ridge Keel Punch Tests, Port and Ocean Engineering under Arctic Conditions (POAC) 2021		https://poac.com/Proceedings/2021/publications.html#h					K				4
A4	Jiang, Z., Heinonen, J., Tikanmäki, M., Mikkola, M., Perälä, I., Shestov, A., Høyland, K.V. Salganik, E., van den Berg, M.,  Li, H. 2021. Scale-model ridges and interaction with narrow structures, Part 4 Global loads and failure mechanisms, Port and Ocean Engineering under Arctic Conditions (POAC) 2021		https://poac.com/Proceedings/2021/publications.html					K				4
A4	Jussila, V. (2018). General principles of the procedure for ice-structure-interaction (PSSII). In Proceedings of the 28th International Ocean and Polar Engineering Conference, ISOPE 2018 (Vol. 2018-June, pp. 1630-1637)		http://publications.isope.org/proceedings/ISOPE/ISOPE%202018/data/index.html					E				4
A1	Kallio-Nyberg, I., Veneranta, L.,  Saloniemi, I., Jokikokko, E., Leskelä, A. (2019). Different growth trends of whitefish (Coregonus lavaretus) forms in the northern Baltic Sea. Journal of Applied Ichthyology 2019: 1-9. doi: 10.1111/jai.13898		https://doi.org/10.1111/jai.13898					K				4
A1	Kotilainen, A.T., Kaskela, A.M., (2017). Comparison of airborne LiDAR and shipboard acoustic data in complex shallow water environments: Filling in the white ribbon zone. Marine Geology 385, 250–259.		https://doi.org/10.1016/j.margeo.2017.02.005					E				4
A1	Makkonen, L., Tikanmäki, M. (2018). Modelling frazil and anchor ice on submerged objects. Cold Regions Science and Technology 151:64-74.		https://doi.org/10.1016/j.coldregions.2018.03.001					K				4
A4	Mikkola, E., Heinonen, J., Kankainen, M., Hekkala, T., & Kurkela, J. (2018). Multi-platform concepts for combining offshore wind energy and fish farming in freezing sea areas: Case study in the Gulf of Bothnia. In ASME 2018 37th International Conference on Ocean, Offshore and Arctic Engineering: Ocean Space Utilization (Vol. 6). [OMAE2018-77677] American Society of Mechanical Engineers ASME. https://doi.org/10.1115/OMAE2018-77677		https://doi.org/10.1115/OMAE2018-77677					E				4
A1	Sae-Lim P, Kause A, Mulder HA & Olesen I. (2017). Climate change and selective breeding in aquaculture. Journal of Animal Science. 95(4): 1801-1812. 		https://doi.org/10.2527/jas.2016.1066					E				4
A4	Sae-Lim P, Kause A, Mulder HA & Olesen I. 2016. Selective breeding in aquaculture for future environments under climate change. In Proceedings: The Role of Agicultural Biotechnologies in Sustainable Feed Systems and Nutrition’, p. 45-46. FAO International Symposium. 15-17 February, 2016, Rome, Italy.											4
A4	"Salganik, E., Ervik, Å, Heinonen, J., Høyland, K.V., Perälä, I., Puolakka, O., Shestov, A., van den Berg M., 2021. Scale-model ridges and interaction with narrow structures, Part 2:
thermodynamics of ethanol ice, Port and Ocean Engineering under Arctic Conditions (POAC) 2021"		https://poac.com/Proceedings/2021/publications.html					K				4
A4	Shestov, A., Ervik, Å, Heinonen, J., Perälä, I., Høyland, K.V., Salganik, E., Li, H., van den Berg, M., Jiang, Z., Puolakka, O. 2021. Scale model ridges and interaction with narrow structures, Part 1: Overview and scaling. 25th IAHR International Symposium on Ice, 2020		https://www.iahr.org/library/technical?pid=304					K				4
A1	Sorsimo, A., & Heinonen, J. (2019). Modelling of ice rubble in the punch shear tests with cohesive 3D discrete element method. Engineering Computations, 36(2), 378-399. 		https://doi.org/10.1108/EC-11-2017-0436					K				4
A4	Tikanmäki, M. (2019) Ice condition parameters of the Gulf of Bothnia with relation to offshore wind turbine design, POAC conference, Delft Netherlands		https://poac.com/Papers/2019/author_index.htm					K				4
A1	Tikanmäki, M., Jaakko Heinonen, J. 2021. Estimating extreme level ice and ridge thickness for offshore wind turbine design: Case study Kriegers Flak. Wind Energy		https://doi.org/10.1002/we.2690					K				4
A4	Zvyagin, P., & Heinonen, J. (2017). Application of Confidence Regions to Ice Ridge Keel Data Statistical Assessment. In ASME 2017 36th International Conference on Ocean, Offshore and Arctic Engineering: Polar and Arctic Sciences and Technology, Petroleum Technology (Vol. 8). [OMAE2017-62253] American Society of Mechanical Engineers ASME.		https://doi.org/10.1115/OMAE2017-62253					E				4
A4	Jolma A., Karvinen V., Viitasalo M., Venesjärvi R. & Haapala J. Information System as a Tool for Marine Spatial Planning: the SmartSea vision and prototype. IFIP Advances in Information and Communication Technology, 2018											5
A1	Katila, J. K. Ala-Rämi, S. Repka, E. Rendon, J.Törrönen, "Defining and quantifying the sea-based economy to support regional blue growth strategies – Case Gulf of Bothnia, Marine Policy", Volume 100, 2019, Pages 215-225, ISSN 0308-597X, https://doi.org/10.1016/j.marpol.2018.11.035. 		https://doi.org/10.1016/j.marpol.2018.11.035					E				5
C2	Lähteenmäki-Uutela, A.; Repka, S., Haukioja, T., Pohjola, T. : Sustainable blue growth and maritime spatial planning. Chapter in "Sustainable Engagement in the Indian and Finnish Business". CIMO Finland, in press. Sustainable Engagement in the Indian and Finnish Business Sustainable Engagement in the Indian and Finnish Business An Omnibus in the Finland-India Project (2016-18)  ‘Responsible Business Partners for Finland and India Trade’ Centre for International Mobility (CIMO), Finland		http://julkaisut.turkuamk.fi/isbn9789522167040.pdf					K				5
A1	Laurila-Pant , M , Mäntyniemi , S , Venesjärvi , R & Lehikoinen , A 2019 , ' Incorporating stakeholders' values into environmental decision support : A Bayesian Belief Network approach ' , The Science of the Total Environment , vol. 697 , 134026 . 		https://www.sciencedirect.com/science/article/pii/S0048969719340033?via%3Dihub					K				5
A1	Virtanen, E.A., Viitasalo, M., Lappalainen, J., Moilanen, A. (2018). Evaluation, gap analysis, and potential expansion of the Finnish Marine Protected Area network. Frontiers in Marine Science 5(402): 1-19. 		https://doi.org/10.3389/fmars.2018.00402					K				5
A1	Virtanen, E., Lappalainen, J., Nurmi, M., Viitasalo, M., Tikanmäki, M., Heinonen, J., Atlaskin, E., Kallasvuo, M., Tikkanen, H., Moilanen, A. 2022. Balancing profitability of energy production, societal impacts and biodiversity in offshore wind farm design. Renewable and Sustainable Energy Reviews 158		https://doi.org/10.1016/j.rser.2022.112087					K				5"""

conv_type = "plaintext"  #"webpage" "plaintext"

if conv_type == "webpage":
    link_style =\
    """
    <li style="font-weight: 400;" aria-level="1"><span style="font-weight: 400;"> {0}</span><a href="{1}"><span style="font-weight: 400;"> {1}</span></a></li>
    """
if conv_type == "plaintext":
    link_style = "{0} {1}"
last_num = 1
for line in articles.split("\n"):
    l = line.split("\t")
    if(len(l)>3 and l[0] == "A1" and len(l[3])>1):  #not empty
        if last_num != l[-1]:
            print(l[-1])
            last_num = l[-1]
        print(link_style.format(l[1],l[3]))
        print()