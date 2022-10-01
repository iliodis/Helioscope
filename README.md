# Helioscope
This is a repository for the project Helioscope, participating in the NASA Spaceapps Challenge 2022, Thessaloniki.

## Aim
Helioscope is an application designed for visualising data from *Parker Solar Probe* (PSP), in an interactive and creative way. It aims to display data from selected instruments of PSP;
- Electromagnetic Fields Investigation (FIELDS)
- Solar Probe Cup (SPC)

## Data used
Redarding the data, we used *pyspedas* to download the desired data in Common Data Format (cdf). For FIELDS, we downloaded the magnetic field data in the RTN coordinate system, downsampled to 1 measurement per minute, provided by Level l2. We also kept the "flags" which indicate if there is any issue in the in situ measurements (binary). For SPC, we downloaded the data in the same format, choosing Level l3 and proceeded to downsampling them to the same resolution as the magnetic field data, keeping the proton velocity moment in three dimensions in RTN $(vp_r, vp_t, vp_n)$, the proton thermal velocity moment $(wp)$ and the proton number density moment $(np)$.

## Choosing the date
The data downloaded refer to 22 days around Encounter 4, a time period where at least three PSP instruments were working properly. During this encounter, the PSP reached perihelion on 2020-01-29/09:37, with its distance to the Sun being 0.13 au (27.8 RS).

## Data manipulation
Afte downloading the data and downsampling them where needed to achieve relatively high resolution and small volume at the same time, we saved them in csv format, keeping only the numerical data in order to reduce space and manipulate it easily with python and c#.

### FIELDS Data
For FIELDS data $(B_r, B_t, B_n)$ we calculated the total magnetic field $|B|$ and matched it to an rgba number in order to quantify the total field with a colorbar. These quadruplets (rgba) were saved in the same csv, concluding to $(B_r, B_t, B_n, flags, r, g, b, a)$. A sample of the colorbar used is given below, for the date 19/01/2022

![fields20-01-19_20-01-20](https://user-images.githubusercontent.com/80003772/193410177-aeadc82d-1b7b-41f7-b9a7-288cf14e12be.png)

Finally, for educational purposes, the coherent structures of the magnetic field were superficially studied. Partial Variance of Increments (PVI) is a measure of how "strong" a structure is, and was introduced by Greco et al 2008 (Intermittent MHD structures and classical discontinuities - https://ui.adsabs.harvard.edu/abs/2008GeoRL..3519111G). Thus, in each csv, the columns represent $(B_r, B_t, B_n, flags, r, g, b, a, PVI)$ respectively.

### SPC Data
The data from SPC saved in the corresponding file were $(vp_r, vp_t, vp_n, wp, np)$. No more analysis were implemented here.

## Sources
- https://pyspedas.readthedocs.io/en/latest/psp.html
- https://ui.adsabs.harvard.edu/abs/2008GeoRL..3519111G/abstract
- https://sppgway.jhuapl.edu/
- http://sweap.cfa.harvard.edu/sweap_data_user_guide.pdf
