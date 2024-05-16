# A quick introduction...

Traffic kills a _lot_ of people, particularly boys and men between ages 5-49. Also, within Chicago, there
are more crashes (and more severe crashes) in historically redlined areas than there are in blue lined
areas. Why should redlining -- a practice from 100 years ago -- impact health outcomes in modern times?

<p align='center'>
   <img src="https://github.com/bucketteOfIvy/traffic-talk/blob/main/figures/injuries_per_redlined_areas.png?raw=true" data-canonical-src="https://github.com/bucketteOfIvy/traffic-talk/blob/main/figures/injuries_per_redlined_areas.png?raw=true" width="600" alt="Bar chart of median visible injuries in crashes per HOLC area grade in 2022-2023 Chicago. A and B graded areas (i.e blue and greenlined areas) have about half as many injuries per square kilometer as C and D graded areas (i.e. yellow and red lined areas)." />
  <br>
  <em>Sometimes a bar chart is enough...</em>
</p>
This talk (and slightly messy repo) contains notebooks and data I used to provide a plausible explanation
of this trend to a lay audience at the Chicago History Museum on May 11th, 2024. In the talk, I sketched
out the connection between traffic fatalities and the built environment, highlighting how the ways we
construct roads and traffic networks heavily influence health outcomes. This leads to a simple but tentative
explanation: disinvestment in redlined areas may have led to less safe infrastructure, leading to the
disparities we observe today.

_*But unfortunately unproveable with current data_

## A quick file structure and setup

The key files in this repo are:

* `Wimer Traffic Lightning Talk` : the actual slides of my lightning talk

* `data/` : the actual data for my repository

* `notebooks/` : EDA and figure creation notebooks

* `scripts/` : python scripts used for data collection (namely for interaction with the Chicago Data Portal).

* `figures/` : figures used in my presentation, and from some of the draft versions of the presentation.

If attempting to run my notebooks, be sure to run `scripts/get_crash_data.py` first to acquire full crash datasets.
